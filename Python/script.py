'''
import ipaddress
from ipaddress import IPv6Address
from ipaddress import IPv6Network
from ipaddress import IPv6Interface
from ipaddress import IPv4Address
from ipaddress import IPv4Network
from ipaddress import IPv4Interface


#IPv4 = (input("Enter your IPv4 Netwok with / formatted CIDR (example: 192.168.1.0/24): "))
IPv4 = "192.168.0.1/24"

#IPv6 = "2001:db8::0/32"

#IPv6_Address = IPv4Address(IPv6)
#IPv6_Interface = IPv6Interface(IPv6)
#IPv6_Network = IPv6Network(IPv6)

try:
    #IPv4_Address = IPv4Address(IPv4)
    
    IPv4_Interface = IPv4Interface(IPv4)
    #IPv4_Network = IPv4Network(IPv4)
    IPv4_Network = IPv4_Interface.network

    print()
    print ("You have entered", IPv4)

    if IPv4_Interface.is_private == True:
        print ("Your IP address", IPv4_Interface.ip, "belongs to IP version", IPv4_Interface.version, "Private Address space")
    else:
        print ("Your IP address", IPv4_Interface.ip, "belongs to IP version",IPv4_Interface.version, "Public Address space")

    print ("Your IP address is", IPv4_Interface.ip,"and Mask is", IPv4_Interface.netmask,"where Network address is", IPv4_Interface.network, "and Broadcast address is", IPv4_Network.broadcast_address)
    print ("Total number of usable host IPs are", IPv4_Network.num_addresses-2, "where the first usable IP is",IPv4_Network[1],"and last usable IP is", IPv4_Network[-2])
    print()

    #for X in IPv4_Network.hosts():
    #   print(X)  
    
except ValueError:
    print()
    print('The address/netmask you entered is invalid for IPv4:', ipaddress)
    print()



#print ("IPv6 Address is", IPv6_Interface.ip, "and Prefix Length is", IPv6_Interface._prefixlen,"and Network is", IPv6_Interface.network)
#print ("IPv6_Interface is", IPv6_Interface)
#print ("IPv6_Network is ", IPv6_Network)
'''
'''
Interface = "GigabitEthernet0/0"
IPv4Address = "192.168.0.1"
IPv4Mask = "255.255.255.0"

InterfaceConfig = "conf t\n interface {}\n ip address {} {}\n no shutdown\n exit"
print(InterfaceConfig.format (Interface, IPv4Address, IPv4Mask))
'''
#######################


'''
Text = """
You have entered 192.168.0.1/24
Your IP address 192.168.0.1 belongs to IP version 4 Private Address space
Your IP address is 192.168.0.1 and Mask is 255.255.255.0 where Network address is 192.168.0.0/24 and Broadcast address is 192.168.0.255
Total number of usable host IPs are 254 where the first usable IP is 192.168.0.1 and last usable IP is 192.168.0.254
"""

IP = "192.168.0.1"

if IP in Text:
    print ("Yes")

StartPoint = Text.find("255.255.255.0")
EndPoint = Text.index("where Network")

#print (StartPoint)
#print (EndPoint)

print (Text[StartPoint:EndPoint])
#print (Text[18:31])

Count = Text.count("IP")
print (Count)

CaseChange = Text.lower().count("ip is")
print (CaseChange)
print(len(Text))

Partition = Text.partition("space")
print (Partition)
print (Partition[0])
print (Partition[1])
print (Partition[2])
print (type(Partition))

Partition = list(Partition)
print (type(Partition))
Partition[2] = " ...CHANGED"
print (Partition[2])
Partition = tuple(Partition)

JoinText = "".join(Partition) 
print (JoinText)
'''

###########################

Position = ["1", "2", "3"]
DeviceName = ["R1", "R2", "R3"]
DeviceIP = ["10.99.1.1", "10.99.2.1", "10.99.3.1"]
DeviceBrand = ["Cisco", "MikroTik", "Juniper"]


'''
print (Position)
print (DeviceName)
print (type(DeviceName))
print (DeviceIP)
print (type(DeviceIP))

DeviceName.insert(2, "R0")
print (DeviceName)
DeviceName.append("R4")
print (DeviceName)
Position.extend(DeviceIP)
print (Position)
'''
'''
for SL in range(len(DeviceBrand)):
    print (SL, DeviceBrand[SL])

[print (SL, DeviceBrand[SL]) for SL in range(len(DeviceBrand))]

SL = 0
while SL < len(DeviceBrand):
    print(SL, DeviceBrand[SL])
    SL = SL+1
'''
'''
DeviceBrand.sort()
print (DeviceBrand)

DeviceBrand.sort(reverse=True)
print (DeviceBrand)

DeviceBrand.reverse()
print (DeviceBrand)


Address = ["H01", "R02", "KC", "DHK", "BD"]

(*PS, District, Country) = Address

print (PS, District, Country)

#print (Address)
'''


#################

# Dictionary
'''
Router1 = {
    "IPAddress" : "10.99.1.1",
    "Username" : "cisco1",
    "Password" : "cisco1",
    "SSH_Port" : 22
}

Router2 = dict(IPAddress = "10.99.2.1", Username = "cisco2", Password = "cisco2", SSH_Port = 22)

print (f"Username1 is {Router1["Username"]}")

print (f"Username2 is {Router2["Username"]}")

print(type(Router1["SSH_Port"]))

Router1Keys = Router1.keys()

Router1Values = Router1.values()

#print (Router1Keys)
#print (Router1Values)

for Router1Key in Router1Keys:
    print (Router1Key)

for Router1Value in Router1Values:
    print (Router1Value)

Router1["Pub_Key"] = "12345678"
Router1["Password"] = "cisco111"
print (Router1)

Router1.update({"Hostname" : "R1", "Location" : "BD"})
print (Router1)

del Router1["Password"]
print (Router1)

Router1.update(Router2)
print (Router1)

Router1.pop("Password")
print (Router1)

Router1.popitem()
print (Router1)

'''

'''
Router1 = {
    "IPAddress" : "10.99.1.1",
    "Username" : "cisco1",
    "Password" : "cisco1",
    "SSH_Port" : 22
}

Router2 = dict(IPAddress = "10.99.2.1", Username = "cisco2", Password = "cisco2", SSH_Port = 22)


for i in Router1:
    print (i)
    print (Router1[i])

for i in Router1.keys():
    print (i)

for i in Router1.values():
    print (i)

print ()

for i, j in Router1.items():
    x = i, j
    print (list(x))



Router1 = Router2.copy()

'''

###################

'''
Interfaces = {
    "eth0/1" : {
        "IPAddress" : "10.99.1.1",
        "Mask" : "255.255.255.0",
        "Status" : "UP"
    },
    "eth0/2" : {
        "IPAddress" : "10.99.2.1",
        "Mask" : "255.255.255.0",
        "Status" : "DOWN"
    },
    "eth0/3" : {
        "IPAddress" : "10.99.3.1",
        "Mask" : "255.255.255.0",
        "Status" : "UP"
    }
}

#print (type(Interfaces))
#print (Interfaces)
#print (Interfaces["eth0/2"]["Status"])


for i, j in Interfaces.items():
    x = i, j
    print (x)
    for m, n in j.items():
        o = m, n
        print (o)



DeviceName = ("R1", "R2", "R3")
DNS = ("8.8.8.8")
DeviceConf = dict.fromkeys(DeviceName, DNS)
print (DeviceConf)

'''

'''
Marks = 70
while Marks < 80:
    print (Marks) 
    Marks = Marks + 2
    if Marks == 76:
        break


Marks = 70
while Marks < 80:
    Marks = Marks + 2
    if Marks == 76:
        continue
    print (Marks) 
'''


# define function

# def message():
#     print("Hello World !")
# name = message()
# print (name)


# def message(name):
#     return (f"Hello {name} !")
# x = message("World")
# print (x)

# def message(fname, lname, salutation="Mr."):
#     return (f"Hello {salutation} {fname} {lname} !")
# x = message("Ayan", "Masrur")
# print (x)

'''
def VALUES(num1, num2, *extra):
    result = num1 + num2
    for i in extra:
        result = result + i
    return result
SUM = VALUES(10, 20, 30, 40, 50)
print (SUM)

import math
b=2
a= math.pow(4, 2)
print(a)
'''

# import getpass
# import telnetlib

# HOST = "10.99.1.1"
# USER = input("Enter your username: ")
# PASSWORD = getpass.getpass()

# tn = telnetlib.Telnet(HOST)

# tn.read_until(b"Username: ")
# tn.write(USER.encode('ascii') + b"\n")
# if PASSWORD:
#     tn.read_until(b"Password: ")
#     tn.write(PASSWORD.encode('ascii') + b"\n")

# tn.write(b"show ip interface brief\n")
# tn.write(b"exit\n")

# print (tn.read_all().decode('ascii'))


'''

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
    tn.write(b"exit\n")
    #print (tn.read_all().decode('ascii'))

    readoutput = tn.read_all()
    saveoutput = open("Router" + HOST, "w")
    saveoutput.write(readoutput.decode("ascii"))
    saveoutput.write("\n")
    saveoutput.close

'''

'''
filename = open("File1.txt", "r")
text = filename.read()

# print (filename)

# newfilename_cache = str(filename)
# print (type(newfilename_cache))


# #newfilename_partition = newfilename_cache.partition(.)
# #print (type(newfilename_partition))
# # Partition = list(Partition)
# # Partition[1] = Expected_Name
# # NewText = "".join(Partition)


# # print (newfilename)
# # print (type(newfilename))

#print (text)
#print (type(text))

FirstText = "name is"
LastText = "I'm from"

# StartPoint = int()
# EndPoint = int()

if FirstText in text:
    StartPoint = text.index(FirstText)
else:
    pass

if LastText in text:
    EndPoint = text.index(LastText)
else:
    pass

#print (StartPoint)
#print(len(FirstText))
#print (EndPoint)

Name = (text[StartPoint+len(FirstText)+1:EndPoint-1])
print ("-----------------------")
print ("The name found in the file:", Name)
#print (len(Name))

Expected_Name = "Md Abdullah Al Naser"

#print (len(Expected_Name))
# if Name == Expected_Name:
#     print ("Identical")

if Name != Expected_Name:
    Partition = text.partition(Name)
    Partition = list(Partition)
    Partition[1] = Expected_Name
    NewText = "".join(Partition) 
    #NewText = Partition[0] + Partition[1] + Partition[2]
    print ("-----------------------")
    print (NewText)
    print ("-----------------------")
    with open("File1_New.txt", 'w') as newtext:
        newtext.write(NewText)
        print ("This new name has been written in a new file named File1_New.txt")
    newtext.close()
else:
    print("Your name is okay")

filename.close()

'''

'''
ipaddress = "192.168.1.1/24"

for x in ipaddress:
    if x == "/":
        break
    print(x, end="")
'''



'''
def SUM(num1, num2):
    result = num1 + num2
    return result

OUTPUT1 = SUM(10, 20)
print (OUTPUT1)

OUTPUT2 = SUM(20, 30)
print (OUTPUT2)

'''

'''
import datetime

time_now = datetime.datetime.now()
day = time_now.strftime("%A")

print (time_now)
print (day)

'''

def ioxxe_interface_config(interface_name, vlan_id, ipv4_address, subnet_mask):
    line1 = f"interface {interface_name}\n"
    line2 = f" service instance {vlan_id} ethernet\n"
    line3 = f"  encapsulation dot1q {vlan_id}\n"
    line4 = f"  rewrite ingress tag pop 1 symmetric\n"
    line5 = f"  bridge-domain {vlan_id}\n"
    line6 = f" exit\n"
    line7 = f"exit\n"
    line8 = f"!\n"
    line9 = f"interface BDI{vlan_id}\n"
    line10 = f" ip address {ipv4_address} {subnet_mask}\n"
    line11 = f" no shutdown\n"
    line12 = f"exit"

    total_line = ""
    for x in range(1, 13):
        total_line = total_line + f"{locals()[f'line{x}']}"
    
    #total_line = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8 + line9 + line10 + line11 + line12

    return total_line

interface_name = "GigabitEthernet0/0/1"
vlan_id = 123
ipv4_address = "172.16.1.1"
subnet_mask = "255.255.255.252"

r1_iosxe_config = ioxxe_interface_config(interface_name, vlan_id, ipv4_address, subnet_mask)
print (r1_iosxe_config)






