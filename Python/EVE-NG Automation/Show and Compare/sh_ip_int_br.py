import getpass
import telnetlib

#HOST = "10.99.1.1"
USER = input("Enter your username: ")
PASSWORD = getpass.getpass()

RouterList = ["10.99.1.1", "10.99.2.1"]

for HOST in RouterList:
    print (f"Saving router configuration IP {HOST}...")
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(USER.encode('ascii') + b"\n")
    if PASSWORD:
        tn.read_until(b"Password: ")
        tn.write(PASSWORD.encode('ascii') + b"\n")

    tn.write(b"show ip interface brief\n")
    #tn.write(b"configure replace tftp://10.99.99.11/G1-R1.txt\n")
    tn.write(b"Y\n")
    tn.write(b"exit\n")
    #print (tn.read_all().decode('ascii'))

    readoutput = tn.read_all()
    saveoutput = open("Router" + HOST, "w")
    saveoutput.write(readoutput.decode("ascii"))
    saveoutput.write("\n")
    saveoutput.close
