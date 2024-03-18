import ipaddress
from ipaddress import IPv6Address
from ipaddress import IPv6Network
from ipaddress import IPv6Interface
from ipaddress import IPv4Address
from ipaddress import IPv4Network
from ipaddress import IPv4Interface


#IPv4 = (input("Enter your IPv4 Netwok with / formatted CIDR (example: 192.168.1.0/24): "))
IPv4 = "192.168.0.0/24"

#IPv6 = "2001:db8::0/32"
#a = "192.168.1.1/24"

#IPv6_Address = IPv4Address(IPv6)
#IPv6_Interface = IPv6Interface(IPv6)
#IPv6_Network = IPv6Network(IPv6)

try:
    IPv4_Interface = IPv4Interface(IPv4)
    IPv4_Network = IPv4Network(IPv4)
    #IPv4_Address = IPv4Address(IPv4)

    print()
    print ("You have entered", IPv4)

    if IPv4_Interface.is_private == True:
        print (IPv4_Interface.ip, "belongs to IP version", IPv4_Interface.version, "Private Address space")
    else:
        print (IPv4_Interface.ip, "belongs to IP version",IPv4_Interface.version, "Public Address space")

    print ("Your IP address is", IPv4_Interface.ip,"and Mask is", IPv4_Interface.netmask,"and Network is", IPv4_Interface.network)
    print ("Total number of usable host IPs are", IPv4_Network.num_addresses-2, "where the first usable IP is",IPv4_Network[1],"and last usable IP is", IPv4_Network[-2])
    print()

except ValueError:
    print()
    print('The address/netmask you entered is invalid for IPv4:', ipaddress)
    print()

#for X in IPv4_Network.hosts():
#    print(X)  

#print ("IPv6 Address is", IPv6_Interface.ip, "and Prefix Length is", IPv6_Interface._prefixlen,"and Network is", IPv6_Interface.network)
#print ("IPv6_Interface is", IPv6_Interface)
#print ("IPv6_Network is ", IPv6_Network)