import getpass
import telnetlib
import time

USER = input("Enter your username: ")
PASSWORD = getpass.getpass()

RouterList = ["10.99.1.1", "10.99.2.1"]
HostList = ["G1-R1", "G2-R1"]


for IP, HOST in zip(RouterList, HostList):
    print (f"Executing script on {HOST} ({IP})...")
    tn = telnetlib.Telnet(IP)

    tn.read_until(b"Username: ")
    tn.write(USER.encode('ascii') + b"\n")
    if PASSWORD:
        tn.read_until(b"Password: ")
        tn.write(PASSWORD.encode('ascii') + b"\n")

    command = f"copy running-config tftp://10.99.99.11/{HOST}.txt\n"
    tn.write(command.encode('utf-8'))
    tn.write(b"\n")
    tn.write(b"\n")
    time.sleep(5)

    #tn.write(b"conf t\n")
    #tn.write(b" hostname HOSTNAME\n")
    #tn.write(b" exit\n")
    #tn.write(b"write\n")
    #tn.write(b"exit\n")
