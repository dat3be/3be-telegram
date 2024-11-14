import sqlite3

db_path = "database.sqlite"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check if the 'type' column exists
cursor.execute("PRAGMA table_info(transactions)")
columns = [column[1] for column in cursor.fetchall()]

if "type" not in columns:
    # Add the 'type' column to the 'transactions' table
    cursor.execute("ALTER TABLE transactions ADD COLUMN type TEXT NOT NULL DEFAULT 'Unknown'")
    print("'type' column added to 'transactions' table.")
else:
    print("'type' column already exists in 'transactions' table.")

conn.commit()
conn.close()

print("Database migration completed.")
