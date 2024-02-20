#import getpass
import telnetlib
from netmiko import ConnectHandler
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import PatternFill
import ipaddress
#from ipaddress import IPv6Interface
#from ipaddress import IPv6Address
#from ipaddress import IPv6Network
from ipaddress import IPv4Interface
#from ipaddress import IPv4Address
#from ipaddress import IPv4Network
import requests
import json
from pprint import pprint
import time
import sys
import app
import re
from datetime import datetime
from lab_variable import EVE_1, EVE_USER, EVE_PASSWORD, ROUTER_USER, ROUTER_PASSWORD, ROUTER_TIMEOUT

#USER = input("Enter your username: ")
#PASSWORD = getpass.getpass()
#EVE_1 = "192.168.30.12"
#USER = "apnic"
#PASSWORD = "training"
#TIMEOUT = 6

### User Input ###
#lab_name = str(input("Enter lab name : "))
lab_name = "IPv6-Basic-Connectivity-Lab"
lab_name_check = f"/{lab_name}.unl"
#num_group = int(input("Enter number Group for Basic IPv6 Connectivity Lab: "))

### Login ###
login_url = f"http://{EVE_1}/api/auth/login"
cred = '{{"username":"{}","password":"{}","html5":"-1"}}'.format(EVE_USER, EVE_PASSWORD)
headers = {"Accept":"application/json"}

login_api = requests.post(url=login_url, data=cred)
cookies = login_api.cookies

# Check Status of Node #
node_status_url = f"http://{EVE_1}/api/labs/IPv6-Basic-Connectivity-Lab.unl/nodes"
node_status_api = requests.get(url=node_status_url,cookies=cookies,headers=headers)

node_status_api_response = node_status_api.json()
#pprint (node_status_api_response)

node_status_dict = node_status_api_response['data']
num_nodes = len(node_status_dict)

# Open Workbook and Sheet 
wb = openpyxl.load_workbook("Device-Info.xlsx")
sheet = wb['IPv6_Basic']

# Iterating Function
max_row = sheet.max_row
max_column = sheet.max_column
HostnameList = []
IPList = []

for i in range(2, int(num_nodes/2)+2):
    hostname = sheet.cell(row=i, column=1).value
    IPv4_FA60_Temp = sheet.cell(row=i,column=3).value
    IPv4_FA60_IP = IPv4Interface(IPv4_FA60_Temp)
    IPv4_FA60_IP = str(IPv4_FA60_IP.ip)    
    HostnameList.append(hostname)
    IPList.append(IPv4_FA60_IP)

savereport = open("ipv6_basic_report/Lab-Report-Task3.txt", "w")

for HOST, IP in zip(HostnameList, IPList):
    try:
        global ssh
        cisco_devices = {
            'device_type': 'cisco_ios',
            'host': IP,
            'username': ROUTER_USER,
            'password': ROUTER_PASSWORD
        }
    
        with ConnectHandler(**cisco_devices) as ssh:
            command1 = (f"ping 2001:db8:abc::2 repeat 5")
            output1 = ssh.send_command_timing(command1, strip_prompt=False, strip_command=False)
            time.sleep(3)

            # Open the file in write mode and write the output to it
            with open(f"ipv6_basic_report/{HOST}-Verify-Connectivity.txt", "w") as saveoutput:
                #saveoutput.write(output1.decode("ascii"))
                saveoutput.write(output1)
                saveoutput.close()

            with open(f"ipv6_basic_report/{HOST}-Verify-Connectivity.txt", "r") as readoutput:
                text = readoutput.read()
            
            RateStart = "Success rate is"
            RateEnd = "percent"

            if RateStart in text and RateEnd in text:
                RateStartIndex = text.index(RateStart)
                RateStartIndexLen = (len(RateStart))
                RateEndIndex = text.index(RateEnd)
                SuccessRate = text[RateStartIndex+RateStartIndexLen:RateEndIndex]
                
                SuccessRate = SuccessRate.strip(" ")
                SuccessRate = int(SuccessRate)
                
                savereport.write("\n")
                
                if SuccessRate > 0:
                    savereport.write(HOST + " can reach host.\n")
                elif SuccessRate == 0: 
                    savereport.write(HOST + " can't reach host.\n")
                else:
                    savereport.write("Couldn't read data")

                #savereport.write("\n")

    except Exception as e:
        print("")
        print (f"Couldn't connect to {HOST}, check manually!")

savereport.close()

showreport = open("ipv6_basic_report/Lab-Report-Task3.txt", "r")
showreport = showreport.read()

print (showreport)
