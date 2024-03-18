from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import telnetlib
import time

app = Flask(__name__)
socketio = SocketIO(app)
#socketio = SocketIO(app, namespace='/console')
command = "show runn"

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    #print('Client connected')
    emit('output', 'Connected to the server.')

@socketio.on('command')
def handle_command(command):
    #print(f'Received command: {command}')
    execute_command(f"{command}\n")

def execute_command(command):
    #print(f'Executing command: {command}')

    try:
        host = '192.168.20.12'
        port = 32769
        username = 'apnic'
        password = 'training'

        tn = telnetlib.Telnet(host, port, timeout=5)

        # tn.read_until(b'>', timeout=5)
        # time.sleep(2)
        # tn.write(username.encode('utf-8') + b'\n')
        # time.sleep(2)
        # tn.read_until(b'>', timeout=5)
        # time.sleep(2)
        # tn.write(password.encode('utf-8') + b'\n')
        # time.sleep(2)
        # tn.read_until(b'>', timeout=5)
        # time.sleep(5)
        # tn.write(f'{command}\n'.encode('utf-8'))
        # time.sleep(2)

        # # Send the command line by line
        # for line in command.split('\n'):
        #     tn.write(line.encode('utf-8'))
        #     tn.write(b'\n')



        # Read the output line by line and send each line to the client
        while True:
            output = tn.read_until(b'\n', timeout=5).decode('utf-8')
            if output == '':
                break
            emit('output', output)

        tn.close()

    except Exception as e:
        error_message = f'Error executing command: {str(e)}'
        print(error_message)
        emit('output', error_message)


if __name__ == '__main__':
    socketio.run(app, debug=True)
