#!C:\Users\abdullah.naser\AppData\Local\Programs\Python\Python312\python.exe
# Your Python script starts here

#import getpass
#import openpyxl
#from openpyxl import Workbook
#from openpyxl.styles import PatternFill
#import ipaddress
#from ipaddress import IPv6Interface
#from ipaddress import IPv6Address
#from ipaddress import IPv6Network
#from ipaddress import IPv4Interface
#from ipaddress import IPv4Address
#from ipaddress import IPv4Network
import requests
import paramiko
import xmltodict
import json
import pprint
import pandas as pd


### Define variables ###

EVE_1 = "192.168.20.12"
EVE_CLI_USER = "root"
EVE_CLI_PASSWORD = "eve"
EVE_USER = "admin"
EVE_PASSWORD = "eve"
ROUTER_USER = "apnic"
ROUTER_PASSWORD = "training"
TIMEOUT = 6

### Login into EVE-NG ###

login_url = f"http://{EVE_1}/api/auth/login"
cred = '{"username":"admin","password":"eve","html5":"-1"}'
headers = {"Accept":"application/json"}

login_api = requests.post(url=login_url, data=cred)
cookies = login_api.cookies

### Get folder list ###

get_folder_url = f"http://{EVE_1}/api/folders/"
get_folder_api = requests.get(url=get_folder_url,cookies=cookies,headers=headers)

get_folder_response = get_folder_api.json()

get_folder_response_dict = get_folder_response['data']

existing_labs = [lab['path'] for lab in get_folder_response_dict['labs']]

#print(existing_labs)
#print(type(existing_labs))

j=1
for i in existing_labs:
    print(f"{j}. {existing_labs[j-1].replace('/', '')}")
    j=j+1

### Select Lab ###
    
if (len(existing_labs)) > 0:
    select_lab = int(input(f"Select your lab (1-{(len(existing_labs))}): "))
else:
    print("No lab found!")

### Open UNL File ###

file_name = existing_labs[select_lab-1].replace('/', '')   

#print(open_file)

# SSH connection details
hostname = f'{EVE_1}'
port = 22
username = f'{EVE_CLI_USER}'
password = f'{EVE_CLI_PASSWORD}'

# Source and destination file paths
source_path = f'/opt/unetlab/labs/{file_name}'
destination_path = f'{file_name}'

# Establish SSH connection
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname, port, username, password)

# Create SCP client
scp_client = ssh_client.open_sftp()

# Download file from source host to local destination
scp_client.get(source_path, destination_path)

# Close SCP and SSH clients
scp_client.close()
ssh_client.close()

with open(f"{file_name}", "r") as unl:
    read_unl = unl.read()
print(type(read_unl))
#print(read_unl)
    
# Convert XML to OrderedDict
read_unl_dict = xmltodict.parse(read_unl)

# Convert OrderedDict to JSON string
read_unl_json = json.dumps(read_unl_dict)

# Print JSON string
#write_unl_json = json.dumps(read_unl_json)
#write_unl_json = json.dumps(write_unl_json)

write_unl_json = json.loads(read_unl_json)
write_unl = pprint.pformat(write_unl_json)

with open(f"{file_name}.json", "w") as unl_json:
     unl_json.write(write_unl)

# Access the "nodes" dictionary under the "topology" dictionary under the "lab" dictionary
nodes = write_unl_json["lab"]["topology"]["nodes"]["node"]
#interface = write_unl_json["lab"]["topology"]["nodes"]["node"]["interface"]
networks = write_unl_json["lab"]["topology"]["networks"]["network"]

# network_id_list = []
mgmt_network_id_list = []

for network in networks:
    network_type = network["@type"]
    # if "pnet" not in network_type:
    #     network_id = network["@id"]
    #     network_id_list.append(network_id)
    if "pnet" in network_type:
        network_id = network["@id"]
        mgmt_network_id_list.append(network_id)
    else:
        pass

#print(network_id_list)
#print(mgmt_network_id_list)

nodes_by_network_id = {}
interfaces_by_network_id = {}

interfaces_by_nodes = {}


# Iterate over each node and print its interfaces
for node in nodes:
    #node_name = node["@name"]
    node_id = node["@id"]
    node_name = node["@name"]
    interfaces = node["interface"]
    for interface in interfaces:
        interface_name = interface["@name"]
        interface_network_id = interface["@network_id"]

        if interface_network_id not in nodes_by_network_id and interface_network_id not in interfaces_by_network_id:
            if interface_network_id not in mgmt_network_id_list:
                nodes_by_network_id[interface_network_id] = {}
                interfaces_by_network_id[interface_network_id] = {}

        if interface_network_id not in mgmt_network_id_list:
            #nodes_by_network_id[interface_network_id].append(node_name)
            nodes_by_network_id[interface_network_id][node_id] = node_name
            interfaces_by_network_id[interface_network_id][node_id] = interface_name
            #interface_name = interface["@name"]
            
            #if interface_network_id in network_id_list:
            
            #bit = True

            #print(f"{node_name} {interface_name} is connected to network {interface_network_id}")

            # interface_id = interface["@id"]
            # interface_name = interface["@name"]
            # print(f"Interface ID: {interface_id}, Interface Name: {interface_name}")
        #else:
            #pass

print(nodes_by_network_id)
#print(len(nodes_by_network_id))

print(interfaces_by_network_id)
#print(len(interfaces_by_network_id))

#print (type(nodes_by_network_id))
#a = json.dumps(nodes_by_network_id)
#print (type(a))

# b = nodes_by_network_id.get(interface_network_id)
# if b is not None:
#     print(b)
# else:
#     pass
#network_ip = 10.0.

# for i in range (1, len(nodes_by_network_id)+1):
#     a = nodes_by_network_id.get(f'{i}', {}).get(f'{i}')
#     print(a)

# keys = nodes_by_network_id.keys()
# for key in keys:
#     print(key)
# values = nodes_by_network_id.values()
# for value in values:
#     print(value)
#     value1 = value.values()
#     print(value1)


for i, j in nodes_by_network_id.items():
    x = i, j
    print (x)
    for m, n in j.items():
        o = m, n
        print (n)




# values1 = values.values()
# print(values1)






# Iterate over key-value pairs and print them
# for node_id, node_name in nodes_by_network_id[nodes].items():
#     with open(f"{node_name}-ip-config.txt", "a") as node_ip_config:
#         interfaces = interfaces_by_network_id.get(network_id, {})
#         print(node_name)

'''
    for node_id, node_name in nodes.items():
        
            if node_id in interfaces:
            #for node_id, node_name in nodes.items():
            
            #if node_id in interfaces_by_network_id.get(network_id, {}):
                interface = interfaces[node_id]
                node_ip_config.write(f"interface {interface}\n")
                node_ip_config.write(f" ip address 10.0.{network_id}.{node_id} 255.255.255.252\n")
                node_ip_config.write(" no shut\n")
'''  
      
            #node_ip_config.write(node_ip_config)

    # for node_id, node_name in nodes.items():
    #     if node_id in interfaces_by_network_id.get(network_id, {}):
    #         interface = interfaces_by_network_id[network_id][node_id]
    #         #print(f"Node: {node_name}, Interface: {interface}")
    #         node_ip_config.write(f"interface {interface}\n")
    #         node_ip_config.write(f" ip address 10.0.{network_id}.{node_id} 255.255.255.252\n")
    #         node_ip_config.write(f" no shut\n")
    
    
    
    
    
    # for node in nodes:
    #     with open(f"{nodes}-ip-config.txt", "w") as node_ip_config:
    #         node_ip_config.write(node_ip_config)

    #         for node_id, interface in nodes.items():
    #             node_ip_config.write(f"interface {interface}\n")
    #             node_ip_config.write(f" ip address 10.0.{network_id}.{node_id} 255.255.255.252\n")
    #             node_ip_config.write(f" no shut\n")
            #print(f"ip address 10.0.{network_id}.{node_id} 255.255.255.252")
        #print()  # Add an empty line for better readability



'''
data = nodes_by_network_id
# Find the maximum length of arrays
max_length = max(len(nodes) for nodes in data.values())

# Pad arrays with empty strings to make them equal in length
for key, value in data.items():
    data[key] += [''] * (max_length - len(value))

# Create DataFrame
df = pd.DataFrame(data)

# Transpose DataFrame
df = df.transpose()

# Print DataFrame
print(df)
'''






#print(interfaces)


'''
### User Input ###

#lab_name = str(input("Enter lab name : "))
lab_name = "IPv6-Basic-Connectivity-Lab"
lab_name_check = f"/{lab_name}.unl"
#num_group = int(input("Enter number Group for Basic IPv6 Connectivity Lab: "))


### Login ###

login_url = f"http://{EVE_1}/api/auth/login"
cred = '{"username":"admin","password":"eve","html5":"-1"}'
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

savereport = open("Lab-Report-Task1.txt", "w")

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
            command1 = (f"show ipv6 interface brief fastEthernet0/0")
            output1 = ssh.send_command_timing(command1, strip_prompt=False, strip_command=False)
            time.sleep(1)
            command2 = (f"show ipv6 interface fastEthernet0/0")
            output2 = ssh.send_command_timing(command2, strip_prompt=False, strip_command=False)
            time.sleep(1)

            # Open the file in write mode and write the output to it
            with open(HOST + "-task1-compare.txt", "w") as saveoutput:
                #saveoutput.write(output1.decode("ascii"))
                saveoutput.write(output1)
                saveoutput.write("\n")
                saveoutput.write(output2)
                saveoutput.write("\n")
                #saveoutput.close()

            with open(HOST + "-task1-compare.txt", "r") as readoutput:
                text = readoutput.read()

            IntStatusStart = "["
            IntStatusEnd = "]"

            if IntStatusStart in text and IntStatusEnd in text:
                IntStatusStartIndex = text.index(IntStatusStart)
                IntStatusEndIndex = text.index(IntStatusEnd)
                IntStatus = text[IntStatusStartIndex+1:IntStatusEndIndex]
            
            else:
                print ("Couldn't read Interface Status of " + HOST)

            GUAStart = "Global unicast address"
            GUAEnd = "Joined group address"

            if GUAStart in text and GUAEnd in text:
                GUAStartIndex = text.index(GUAStart)
                GUAStartIndexLen = (len(GUAStart))
                GUAEndIndex = text.index(GUAEnd)
                GUAAddress = text[GUAStartIndex+GUAStartIndexLen:GUAEndIndex]
                CIDRIndex = GUAAddress.index("/")
                CIDRvalue = GUAAddress[CIDRIndex+1:CIDRIndex+4]
                PrefixLenValue = (int(CIDRvalue))

                GUA = "2001:DB8:ABC::1"
                GUACount = text.count("subnet is")

                savereport.write("\n")

                if GUA in GUAAddress and GUACount == 1 and PrefixLenValue == 64:
                    savereport.write(HOST + " IPv6 address and prefix length are correct.\n")

                elif GUA in GUAAddress and GUACount == 1 and PrefixLenValue != 64:
                    savereport.write(HOST + " IPv6 address is correct but prefix length is not correct.\n")

                elif GUA in GUAAddress and GUACount > 1:
                    savereport.write(HOST + " has multiple IPv6 configured.\n")

                else:
                    savereport.write(HOST + " IPv6 address is not correct.\n")

                if IntStatus == "up/up":
                    savereport.write(HOST + " interface Fa0/0 status is UP.\n")
                else:
                    savereport.write(HOST + " interface Fa0/0 status is DOWN.\n")

            else:
                savereport.write("\n")
                savereport.write(HOST + " IPv6 address is not configured.")
                savereport.write("\n")

    except:
        savereport.write("\n")
        savereport.write(HOST + " Couldn't connect, check manually.")        
        savereport.write("\n")

savereport.close()

showreport = open("Lab-Report-Task1.txt", "r")
showreport = showreport.read()
    
print (showreport)
    
#savereport.close()
#saveoutput.close()
'''