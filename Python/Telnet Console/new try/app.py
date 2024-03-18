from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import telnetlib

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Replace these with your actual telnet server details
router_ip = "10.99.1.1"
telnet_port = 23
telnet_username = "apnic"
telnet_password = "training"

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('command')
def handle_command(command):
    print(f'Received command: {command}')

    try:
        tn = telnetlib.Telnet(router_ip, telnet_port, timeout=5)
        tn.read_until(b'Username: ', timeout=5)
        tn.write(telnet_username.encode('utf-8') + b'\n')
        tn.read_until(b'Password: ', timeout=5)
        tn.write(telnet_password.encode('utf-8') + b'\n')
        tn.read_until(b'>', timeout=5)
        tn.write(f'{command}\n'.encode('utf-8'))

        while True:
            output = tn.read_until(b'\n', timeout=5).decode('utf-8')
            if output == '':
                break
            socketio.emit('output', output.strip())

        tn.close()

    except Exception as e:
        error_message = f'Error executing command: {str(e)}'
        print(error_message)
        socketio.emit('output', error_message)

if __name__ == '__main__':
    socketio.run(app, debug=True)