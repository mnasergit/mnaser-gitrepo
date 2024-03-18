import sqlite3

# Get input from user
input_value = input("Enter a value: ")

# Connect to SQLite database (or create if not exists)
conn = sqlite3.connect('shared_data.db')
cursor = conn.cursor()

# Create a table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS shared_data1 (value TEXT PRIMARY KEY)''')

# Insert value into DB
try:
    # Try to update the value if it already exists
    cursor.execute("UPDATE shared_data1 SET value = ? WHERE rowid = 1", (input_value,))
    if cursor.rowcount == 0:
        # If no rows were updated, insert the new value
        cursor.execute("INSERT INTO shared_data1 (value) VALUES (?)", (input_value,))
except sqlite3.OperationalError:
    # Handle case where the table may not exist yet
    pass

conn.commit()

# Close the connection
conn.close()
