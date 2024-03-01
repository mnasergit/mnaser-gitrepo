import openpyxl
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from ipaddress import IPv4Interface
import requests
from pprint import pprint
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from netmiko import ConnectHandler
from lab_variable import EVE_1, EVE_USER, EVE_PASSWORD, ROUTER_USER, ROUTER_PASSWORD, ROUTER_TIMEOUT

lab_name = "IPv6-Basic-Connectivity-Lab"
lab_name_check = f"/{lab_name}.unl"

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

for i in range(2, int(num_nodes/2) + 2):
    hostname = sheet.cell(row=i, column=1).value
    IPv4_FA60_Temp = sheet.cell(row=i,column=3).value
    IPv4_FA60_IP = IPv4Interface(IPv4_FA60_Temp)
    IP = str(IPv4_FA60_IP.ip)
    HostnameList.append(hostname)
    IPList.append(IP)

# Create an empty report file
with open("ipv6_basic_report/Lab-Report-Task1-Restore.txt", "w"):
    pass

def task1_restore(hostname, IP):
    result = f"\n"
    try:
        cisco_devices = {
            'device_type': 'cisco_ios',
            'host': IP,
            'username': ROUTER_USER,
            'password': ROUTER_PASSWORD
        }

        with ConnectHandler(**cisco_devices) as ssh:
            #print(f"Executing script on {HOST}...")
            command1 = (f"configure replace tftp://10.99.99.11/ipv6_basic_config_files/{hostname}-task1-config.txt")
            command2 = "Y"
            command3 = "write memory"
            output1 = ssh.send_command_timing(command1, strip_prompt=False, strip_command=False)
            time.sleep(3)
            #print (output1)
            output2 = ssh.send_command_timing(command2, strip_prompt=False, strip_command=False)
            time.sleep(6)
            #print (output2)
            output3 = ssh.send_command_timing(command3, strip_prompt=False, strip_command=False)
            time.sleep(3)
            #print (output3)
            result += f"{hostname}: IPv6 address configuration is restored successfully."
            result += f"\n" 

    except Exception as e:
        result += f"Couldn't connect to {hostname}, check manually!"
        result += f"\n"

    return result

def export_node():
    # Export configs of Node #
    try:
        for i in range (1, int(num_nodes/2) + 1):
            node_export_url = f"http://{EVE_1}/api/labs/IPv6-Basic-Connectivity-Lab.unl/nodes/{i}/export"
            node_export_api = requests.put(url=node_export_url,cookies=cookies,headers=headers)
            # node_export_api_response = node_export_api.json()
            # pprint (node_export_api_response)
        print()
        print("In EVE-NG all router configuration have been successfully exported.")    
    except:
        pass

def main():
    with ThreadPoolExecutor(max_workers=len(HostnameList)) as executor:
        results = list(executor.map(task1_restore, HostnameList, IPList))
    
    # Write the results to the report file in the correct order
    with open("ipv6_basic_report/Lab-Report-Task1-Restore.txt", "a") as savereport:
        for result in results:
            savereport.write(result)

    # Show the report content
    with open("ipv6_basic_report/Lab-Report-Task1-Restore.txt", "r") as showreport:
        print(showreport.read())

    # Call the export_node function
    export_node()

if __name__ == '__main__':
    main()
