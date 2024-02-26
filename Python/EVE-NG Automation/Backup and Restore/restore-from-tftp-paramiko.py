import paramiko
import time

def run_command(ip, username, password, commands):
    # Connect to the device
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password, look_for_keys=False)

    print (f"Executing script on {HOST} ({IP})...")

    # Start an interactive shell
    shell = ssh.invoke_shell()

    # Send the 'enable' command if needed
    #shell.send("enable\n")
    #time.sleep(1)
    #shell.send(password + "\n")
    #time.sleep(1)

    # Send the 'configure terminal' command
    #shell.send("configure terminal\n")
    #time.sleep(1)

    # Send the actual commands
    for command in commands:
        shell.send(command + '\n')
        time.sleep(12)

    # Save the configuration
    shell.send("write memory\n")
    time.sleep(3)

    # Read and print the output
    output = shell.recv(65535).decode('utf-8')
    print("Command Output:")
    print(output)

    # Close the SSH connection
    shell.close()
    ssh.close()

RouterList = ["10.99.1.1", "10.99.2.1"]
HostList = ["G1-R1", "G2-R1"]

for IP, HOST in zip(RouterList, HostList):

    if __name__ == "__main__":
        device_ip = IP
        device_username = "apnic"
        device_password = "training"

        commands_to_run = [f"configure replace tftp://10.99.99.11/{HOST}.txt", "Y"]
        
        run_command(device_ip, device_username, device_password, commands_to_run)
        





