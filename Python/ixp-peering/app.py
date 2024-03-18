from flask import Flask, render_template, request
import subprocess
import sys
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/ixp-peering-configuration-generator", methods=["POST"])
def config():
    own_asn = request.form["own_asn"]
    neighbor_asn = request.form["neighbor_asn"]
    bgp_neighbor = request.form["bgp_neighbor"]
    
    # Connect to SQLite database (or create if not exists)
    conn = sqlite3.connect('config_data.db')
    cursor = conn.cursor()

    # Create a table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS table_config_data (id INTEGER PRIMARY KEY, value TEXT)''')
    
    # Insert value into DB
    try:
        # Try to update the value if it already exists
        cursor.execute("UPDATE table_config_data SET value = ? WHERE id = 1", (own_asn,))
        cursor.execute("UPDATE table_config_data SET value = ? WHERE id = 2", (neighbor_asn,))
        cursor.execute("UPDATE table_config_data SET value = ? WHERE id = 3", (bgp_neighbor,))
        if cursor.rowcount == 0:
            # If no rows were updated, insert the new value
            cursor.execute("INSERT INTO table_config_data (id, value) VALUES (?, ?)", (1, own_asn))
            cursor.execute("INSERT INTO table_config_data (id, value) VALUES (?, ?)", (2, neighbor_asn))
            cursor.execute("INSERT INTO table_config_data (id, value) VALUES (?, ?)", (3, bgp_neighbor))
    except sqlite3.OperationalError:
        pass

    conn.commit()

    # Close the connection
    conn.close()

    # Run your Python script and capture the output
    result = subprocess.check_output(["python", "ixp_peering_configuration_generator.py"], text=True)
    return result

### Main Function ###
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, debug=True)