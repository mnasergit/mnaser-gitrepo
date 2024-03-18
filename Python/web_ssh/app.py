from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import paramiko

app = Flask(__name__)
socketio = SocketIO(app)

# Define device information
device = {
    'hostname': '10.99.1.1',
    'port': 22,
    'username': 'apnic',
    'password': 'training'
}

# Function to establish SSH connection and execute command
def execute_ssh_command(command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=device['hostname'], port=device['port'], username=device['username'], password=device['password'])
    _, stdout, _ = client.exec_command(command)
    output = stdout.read().decode('utf-8')
    client.close()
    return output

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('input')
def handle_input(data):
    command = data['text']
    output = execute_ssh_command(command)
    emit('output', {'text': output})

if __name__ == '__main__':
    socketio.run(app, debug=True)
