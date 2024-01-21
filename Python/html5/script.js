document.addEventListener('DOMContentLoaded', function () {
    // Create a new terminal object
    const term = new Terminal();

    // Attach the terminal to the specified container
    term.open(document.getElementById('terminal-container'));

    // Set the dimensions of the terminal
    term.resize(80, 24);

    // Attach the terminal to a WebSocket for communication
    const socket = new WebSocket('ws://your-server-address'); // Replace with your WebSocket server address

    // Listen for data from the WebSocket and write it to the terminal
    socket.addEventListener('message', function (event) {
        term.write(event.data);
    });

    // Listen for data from the terminal and send it to the WebSocket
    term.onData(function (data) {
        socket.send(data);
    });

    // Handle terminal resizing
    window.addEventListener('resize', function () {
        const rows = Math.floor(window.innerHeight / term.charHeight);
        const cols = Math.floor(window.innerWidth / term.charWidth);
        term.resize(cols, rows);
    });
});
