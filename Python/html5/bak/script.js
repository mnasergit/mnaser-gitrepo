document.addEventListener("DOMContentLoaded", function() {
    const consoleOutput = document.getElementById("console-output");
    const consoleInput = document.getElementById("console-input");

    // Function to handle command execution
    function executeCommand(command) {
        // Replace this with your logic to handle the command
        consoleOutput.textContent += "> " + command + "\n";
        
        // Example: You might want to send the command to another router using Telnet
        sendCommandToRouter(command);
    }

    // Function to send a command to another router using Telnet
    function sendCommandToRouter(command) {
        // Replace the following variables with your actual Telnet connection details
        const routerIP = "10.99.1.1";
        const routerPort = 23;

        const telnet = new WebSocket(`ws://${routerIP}:${routerPort}`);

        telnet.addEventListener("open", function(event) {
            // Send the command once the WebSocket connection is open
            telnet.send(command);
        });

        // telnet.addEventListener("message", function(event) {
        //     // Handle the response from the router
        //     consoleOutput.textContent += event.data + "\n";
        // });

        telnet.addEventListener("message", function(event) {
            consoleOutput.textContent += "Received: " + event.data + "\n";
        });
        

        telnet.addEventListener("close", function(event) {
            consoleOutput.textContent += "Telnet connection closed.\n";
        });
    }

    // Handle Enter key press in the input field
    consoleInput.addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            const command = consoleInput.value.trim();
            consoleInput.value = "";
            executeCommand(command);
        }
    });
});
