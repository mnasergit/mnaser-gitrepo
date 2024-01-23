from flask import Flask, render_template, request, session
#from flask_socketio import SocketIO
import subprocess
import sys
#import app
import ipv6_basic_generate_config
import ipv6_basic_provision_lab
#import ipv6_basic_node_start
#import ipv6_basic_node_monitor
import re

app = Flask(__name__)
#socketio = SocketIO(app)
app.secret_key = "your_secret_key"

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

def process_variable(input_value):
    try:
        # Try to convert the input value to an integer
        #num_group = int(input_value)

        # Your processing logic here
        #num_group = f"Processed variable: {input_value}"
        # Extract the numeric part using regular expression
        #num_group = re.search(r'\d+', num_group).group()

        # Your processing logic here
        # Use regular expression to extract the numeric part
        match = re.search(r'\b\d+\b', input_value)
        if match:
            num_group = match.group()
            return num_group
        else:
            return "0"  # Return a default value if no numeric part is found

        #return num_group

    except ValueError:
        # If conversion fails, return an error message
        return "Error: Please provide a valid integer value."

@app.route("/ipv6-basic-provision", methods=["GET", "POST"])
def lab_provision():
    return render_template("ipv6-basic-provision.html")


@app.route("/ipv6-basic-generate-config", methods=["POST"])
def run_code1():
    try:
        input_value = request.form["input_name"]
    except KeyError:
        return "Error: Form input 'input_name' is missing"

    # Store the input_value in the session
    session["input_value"] = input_value

    # Check if input_value is not empty before proceeding
    if input_value.strip():
        try:
            # Call the process_variable function
            result = ipv6_basic_generate_config.process_variable(input_value)

            # Run your Python script and capture the output
            result = subprocess.check_output(["python", "ipv6_basic_generate_config.py", input_value], text=True)
            return result
            #socketio.emit('script_output', {'output': result})

        except subprocess.CalledProcessError as e:
            # Print the error details to help diagnose the issue
            print(f"Error: {e}")
            print(f"Output: {e.output}")
            #return f"Error: {e}"
            sys.exit(1)

        # You can perform additional processing here if needed
        #return f"Form input received: {input_value}"
    else:
        return "Error: Form input is empty"

@app.route("/ipv6-basic-provision-lab", methods=["POST"])
def run_code2():
    # Retrieve the input_value from the session
    input_value = session.get("input_value")

    if input_value is not None:
        try:
            # Run your Python script and capture the output
            result1 = subprocess.check_output(["python", "ipv6_basic_provision_lab.py", input_value], text=True)
            return result1
        
        except subprocess.CalledProcessError as e:
            # Print the error details to help diagnose the issue
            print(f"Error: {e}")
            print(f"Output: {e.output}")
            sys.exit(1)
    
    else:
        return "No input value found in the session"

@app.route("/ipv6-basic-node", methods=["GET", "POST"])
def node_status():
    return render_template("ipv6-basic-node.html")


@app.route("/ipv6-basic-node-start", methods=["GET", "POST"])
def run_code3():
    try:
        # Run your Python script and capture the output
        result1 = subprocess.check_output(["python", "ipv6_basic_node_start.py"], text=True)
        return result1
        
    except subprocess.CalledProcessError as e:
        # Print the error details to help diagnose the issue
        print(f"Error: {e}")
        print(f"Output: {e.output}")
        sys.exit(1)
    

@app.route("/ipv6-basic-node-monitor", methods=["GET", "POST"])
def run_code4():
    # Retrieve the input_value from the session
    input_value = session.get("input_value")

    if input_value is not None:
        try:
            # Run your Python script and capture the output
            result3 = subprocess.check_output(["python", "ipv6_basic_node_monitor.py", input_value], text=True)
            return result3
        
        except subprocess.CalledProcessError as e:
            # Print the error details to help diagnose the issue
            print(f"Error: {e}")
            print(f"Output: {e.output}")
            sys.exit(1)
    
    else:
        return "No input value found in the session"
    

@app.route("/ipv6-basic-check", methods=["GET", "POST"])
def config_check():
    return render_template("ipv6-basic-check.html")

@app.route("/ipv6-basic-check-task-1", methods=["GET", "POST"])
def check_task_1():
    try:
        # Run your Python script and capture the output
        result1 = subprocess.check_output(["python", "ipv6_basic_check_task_1.py"], text=True)
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
        result2 = subprocess.check_output(["python", "ipv6_basic_restore_task_1.py"], text=True)
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
        result1 = subprocess.check_output(["python", "ipv6_basic_check_task_2.py"], text=True)
        return result1
        
    except subprocess.CalledProcessError as e:
        # Print the error details to help diagnose the issue
        print(f"Error: {e}")
        print(f"Output: {e.output}")
        sys.exit(1)


if __name__ == "__main__":
    app.run(debug=True)
