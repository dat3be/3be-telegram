
# 3BE Telegram

**3BE Telegram** is a customized implementation of the [Greed Telegram Bot](https://github.com/Steffo99/greed), tailored specifically for Vietnamese users. The bot provides an intuitive shopping and payment experience with support for local languages and popular payment gateways in Vietnam.

## Features

### General Features
- **Vietnamese Localization**: Fully translated user interface, making it accessible for Vietnamese users.
- **Payment Integration**: Supports popular payment methods in Vietnam:
  - **VietQR**: Convenient banking transfers using QR codes.
  - **MoMo Wallet**: Secure and fast transactions through the MoMo app.
  - **ZaloPay**: Simple payments via the ZaloPay wallet.
- **Cart Management**: Add, remove, and view products in a shopping cart.
- **Order Management**: Place and manage orders with real-time updates.
- **Wallet System**: Allows users to manage their funds efficiently.
- **No Credit Cards or Cash Support**: Focused entirely on local digital payment methods.

### Administrative Features
- Manage products: Add, edit, or delete items.
- Track orders: View live orders in real time.
- Adjust user balances directly from the bot.
- Export transactions as a CSV file for further analysis.

## Requirements

- **Python 3.8+**
- **Telegram Bot API Token**
- Required Python packages (see `requirements.txt`)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/3be-telegram.git
   cd 3be-telegram
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file with the following content:
   ```env
   TELEGRAM_BOT_TOKEN=your-telegram-bot-token
   PAYMENT_PROVIDER_API_KEY=your-payment-api-key
   ```

4. **Run the bot:**
   ```bash
   python bot.py
   ```

## Usage

### For Users
- Start the bot by sending `/start` in Telegram.
- Add products to your cart, view cart details, and place orders.
- Fund your wallet via **VietQR**, **MoMo**, or **ZaloPay**.

### For Admins
- Use the admin menu to:
  - Manage products (add, edit, delete).
  - View and manage user orders.
  - Adjust user balances or resolve payment issues.
  - Export transactions for record-keeping.

## Localization

- The bot is fully localized in Vietnamese.
- Language files are located in the `strings/` directory.
- You can modify or add new language packs to suit your needs.

## Contribution

Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a feature or bugfix branch.
3. Submit a pull request describing your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built on the [Greed](https://github.com/Steffo99/greed) framework by [Steffo99](https://github.com/Steffo99).
- Customizations and Vietnamese localization by Dat 3BE.
