import sys
import subprocess
from flask import Flask, render_template, request
import ipv6_basic_generate_config
import re
import os
import sqlite3
from lab_variable import APP_SECRET_KEY, PYTHON_PATH

app = Flask(__name__)
app.secret_key = APP_SECRET_KEY

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/ipv6-basic-provision", methods=["GET", "POST"])
def lab_provision():
    return render_template("ipv6-basic-provision.html")

@app.route("/ipv6-basic-generate-config", methods=["POST"])
def run_code1():
    try:
        input_value = request.form["input_name"]
    except KeyError:
        return "Error: Form input 'input_name' is missing"

    # Check if input_value is not empty before proceeding
    if input_value.strip():
        try:
            # Call the process_variable function
            result = ipv6_basic_generate_config.process_variable(input_value)

            # Run your Python script and capture the output
            result = subprocess.check_output([PYTHON_PATH, "ipv6_basic_generate_config.py", input_value], text=True)

            # Connect to SQLite database (or create if not exists)
            conn = sqlite3.connect('lab_data.db')
            cursor = conn.cursor()

            # Create a table if not exists
            cursor.execute('''CREATE TABLE IF NOT EXISTS table_basic_ipv6 (value TEXT PRIMARY KEY)''')

            # Insert value into DB
            try:
                # Try to update the value if it already exists
                cursor.execute("UPDATE table_basic_ipv6 SET value = ? WHERE rowid = 1", (input_value,))
                if cursor.rowcount == 0:
                    # If no rows were updated, insert the new value
                    cursor.execute("INSERT INTO table_basic_ipv6 (value) VALUES (?)", (input_value,))
            except sqlite3.OperationalError:
                pass

            conn.commit()

            # Close the connection
            conn.close()
            
            return result

        except subprocess.CalledProcessError as e:
            # Print the error details to help diagnose the issue
            print(f"Error: {e}")
            print(f"Output: {e.output}")
            #return f"Error: {e}"
            sys.exit(1)

    else:
        return "Error: Form input is empty"

@app.route("/ipv6-basic-provision-lab", methods=["POST"])
def run_code2():
    try:
        # Run your Python script and capture the output
        result1 = subprocess.check_output([PYTHON_PATH, "ipv6_basic_provision_lab.py"], text=True)
        return result1
    
    except subprocess.CalledProcessError as e:
        # Print the error details to help diagnose the issue
        print(f"Error: {e}")
        print(f"Output: {e.output}")
        sys.exit(1)

@app.route("/ipv6-basic-node", methods=["GET", "POST"])
def node_status():
    return render_template("ipv6-basic-node.html")

@app.route("/ipv6-basic-node-start", methods=["GET", "POST"])
def run_code3():
    try:
        # Run your Python script and capture the output
        result1 = subprocess.check_output([PYTHON_PATH, "ipv6_basic_node_start.py"], text=True)
        return result1
        
    except subprocess.CalledProcessError as e:
        # Print the error details to help diagnose the issue
        print(f"Error: {e}")
        print(f"Output: {e.output}")
        sys.exit(1)

@app.route("/ipv6-basic-node-monitor", methods=["GET", "POST"])
def run_code4():

    #if input_value is not None:
    try:
        # Run your Python script and capture the output
        result3 = subprocess.check_output([PYTHON_PATH, "ipv6_basic_node_monitor.py"], text=True)
        return result3
        
    except subprocess.CalledProcessError as e:
        # Print the error details to help diagnose the issue
        print(f"Error: {e}")
        print(f"Output: {e.output}")
        sys.exit(1)

@app.route("/ipv6-basic-check", methods=["GET", "POST"])
def config_check():
    return render_template("ipv6-basic-check.html")

@app.route("/ipv6-basic-check-task-1", methods=["GET", "POST"])
def check_task_1():
    try:
        # Run your Python script and capture the output
        result1 = subprocess.check_output([PYTHON_PATH, "ipv6_basic_check_task_1.py"], text=True)
        return result1
        
    except subprocess.CalledProcessError as e:
        # Print the error details to help diagnose the issue
        print(f"Error: {e}")
        print(f"Output: {e.output}")
        sys.exit(1)

@app.route("/ipv6-basic-restore-task-1", methods=["GET", "POST"])
def restore_task_1():
    try:
        # Run your Python script and capture the output
        result2 = subprocess.check_output([PYTHON_PATH, "ipv6_basic_restore_task_1.py"], text=True)
        return result2
        
    except subprocess.CalledProcessError as e:
        # Print the error details to help diagnose the issue
        print(f"Error: {e}")
        print(f"Output: {e.output}")
        sys.exit(1)

@app.route("/ipv6-basic-check-task-2", methods=["GET", "POST"])
def check_task_2():
    try:
        # Run your Python script and capture the output
        result1 = subprocess.check_output([PYTHON_PATH, "ipv6_basic_check_task_2.py"], text=True)
        return result1
        
    except subprocess.CalledProcessError as e:
        # Print the error details to help diagnose the issue
        print(f"Error: {e}")
        print(f"Output: {e.output}")
        sys.exit(1)

@app.route("/ipv6-basic-check-task-3", methods=["GET", "POST"])
def check_task_3():
    try:
        # Run your Python script and capture the output
        result1 = subprocess.check_output([PYTHON_PATH, "ipv6_basic_check_task_3.py"], text=True)
        return result1

    except subprocess.CalledProcessError as e:
        # Print the error details to help diagnose the issue
        print(f"Error: {e}")
        print(f"Output: {e.output}")
        sys.exit(1)

@app.route("/ipv6-basic-stop", methods=["GET", "POST"])
def stop_page():
    return render_template("ipv6-basic-stop.html")

@app.route("/ipv6-basic-node-stop", methods=["GET", "POST"])
def stop_node():
    try:
        # Run your Python script and capture the output
        result1 = subprocess.check_output([PYTHON_PATH, "ipv6_basic_node_stop.py"], text=True)
        return result1

    except subprocess.CalledProcessError as e:
        # Print the error details to help diagnose the issue
        print(f"Error: {e}")
        print(f"Output: {e.output}")
        sys.exit(1)

### Main Function ###
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, debug=True)
