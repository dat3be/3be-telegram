import sys
import os
import logging
import toml
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import database as db

# Load configuration
config = toml.load("./config/config.toml")
bankmate_secret_key = config["Payments"]["VietQR"]["bankmate_secret_key"]
usd_to_vnd_rate = config["Payments"]["VietQR"].get("usd_to_vnd_rate", 25000)

# Add the current directory to system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
log = logging.getLogger("BankMateWebhook")

# Database setup
DATABASE_URI = config["Database"]["engine"]
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


def validate_webhook_data(data):
    """
    Validate incoming webhook data to ensure all required fields are present.
    """
    required_fields = [
        "value", "bank_name", "bank_account", "account_number",
        "created_at", "custom_description", "secret_key"
    ]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise BadRequest(f"Missing required fields: {', '.join(missing_fields)}")

    if data.get("secret_key") != bankmate_secret_key:
        raise BadRequest("Invalid secret key")

    return data


def extract_transaction_id(custom_description):
    """
    Extract the transaction ID from the custom description field.
    """
    if "chuc mung" in custom_description:
        return custom_description.split("chuc mung")[1].strip().split(" ")[0]
    raise ValueError("Transaction ID could not be extracted from custom_description")


def process_transaction(data, session):
    """
    Process the transaction received from the webhook.
    Converts the amount to USD and updates the database.
    """
    try:
        custom_description = data.get("custom_description", "")
        transaction_id = extract_transaction_id(custom_description)
        log.debug(f"Extracted transaction ID: {transaction_id}")

        transaction = session.query(db.Transaction).filter_by(transaction_id=transaction_id).one_or_none()
        if not transaction:
            raise ValueError(f"Transaction {transaction_id} not found in the database")

        value_vnd = data.get("value", 0)
        value_usd = round(value_vnd / usd_to_vnd_rate, 2)

        # Update transaction details
        transaction.value = value_usd
        transaction.status = "Completed"
        transaction.provider = data.get("bank_name", "Unknown")

        user = session.query(db.User).filter_by(user_id=transaction.user_id).one_or_none()
        if user:
            user.credit += value_usd
            log.info(f"Updated balance for user {user.user_id}: +{value_usd:.2f} USD (new balance: {user.credit:.2f} USD).")

        session.commit()
        log.info(f"Transaction {transaction_id} processed successfully.")
        return transaction_id
    except Exception as e:
        log.error(f"Error processing transaction: {e}")
        session.rollback()
        raise


@app.route('/webhook/bankmate', methods=['POST'])
def bankmate_webhook():
    """
    Handle BankMate webhook for VietQR transactions.
    """
    session = Session()
    try:
        log.info("Received webhook request")

        data = request.json or request.form.to_dict()
        if not data:
            raise BadRequest("No data received")

        data = validate_webhook_data(data)
        log.debug(f"Validated webhook data: {data}")

        transaction_id = process_transaction(data, session)
        log.info(f"Transaction {transaction_id} processed successfully.")

        return jsonify({'success': True, 'message': 'Transaction processed successfully', 'transaction_id': transaction_id}), 200
    except BadRequest as e:
        log.warning(f"Bad request: {e}")
        return jsonify({'success': False, 'message': str(e)}), 400
    except Exception as e:
        log.error(f"Error processing webhook: {e}", exc_info=True)
        return jsonify({'success': False, 'message': 'Internal server error'}), 500
    finally:
        session.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333)
