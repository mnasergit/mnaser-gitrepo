import sqlite3

# Connect to the same SQLite database
conn = sqlite3.connect('shared_data.db')
cursor = conn.cursor()

# Retrieve the value from the table
cursor.execute("SELECT value FROM shared_data1")
result = cursor.fetchone()[0]

print("Value received:", result)
print(type(result))

try:
    a = int(result)
    print(type(a))
except:
    print("type ERROR")
# Close the connection
conn.close()