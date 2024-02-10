#!C:\Users\abdullah.naser\AppData\Local\Programs\Python\Python312\python.exe
# Your Python script starts here

import requests
import paramiko
import xmltodict
import json
import pprint

### Define variables ###
EVE_1 = "192.168.20.12"
EVE_CLI_USER = "root"
EVE_CLI_PASSWORD = "eve"
EVE_WEB_USER = "admin"
EVE_WEB_PASSWORD = "eve"

### Login into EVE-NG ###
login_url = f"http://{EVE_1}/api/auth/login"
cred = f'{{"username":"{EVE_WEB_USER}","password":"{EVE_WEB_PASSWORD}","html5":"-1"}}'

headers = {"Accept":"application/json"}

login_api = requests.post(url=login_url, data=cred)
cookies = login_api.cookies

### Get folder list ###
get_folder_url = f"http://{EVE_1}/api/folders/"
get_folder_api = requests.get(url=get_folder_url,cookies=cookies,headers=headers)

get_folder_response = get_folder_api.json()

get_folder_response_dict = get_folder_response['data']

existing_labs = [lab['path'] for lab in get_folder_response_dict['labs']]

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

# SSH connection details
hostname = f'{EVE_1}'
port = 22
username = f'{EVE_CLI_USER}'
password = f'{EVE_CLI_PASSWORD}'

# Establish SSH connection
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname, port, username, password)

# Open an SSH session
ssh_session = ssh_client.open_sftp()

'''
###########################################################
# Source and destination file paths
source_path = f'/opt/unetlab/labs/{file_name}'
destination_path = f'{file_name}'

# Download file from source host to local destination
ssh_session.get(source_path, destination_path)

# Close SCP and SSH clients
ssh_session.close()
ssh_client.close()

with open(f"{file_name}", "r") as unl:
    read_unl = unl.read()
###########################################################
'''

###########################################################
# Remote file path
remote_path = f'/opt/unetlab/labs/{file_name}'

with ssh_session.open(remote_path, 'r') as remote_file:
    read_unl = remote_file.read()

# Close SCP and SSH clients
ssh_session.close()
ssh_client.close()
###########################################################

# Convert XML to OrderedDict
read_unl_dict = xmltodict.parse(read_unl)

'''
### If it is required to see the file ###
# Convert OrderedDict to JSON string
read_unl_json = json.dumps(read_unl_dict)
# Convert JSON string to pprint format
read_unl_json = json.loads(read_unl_json)
read_unl_json_pprint = pprint.pformat(read_unl_json)
with open(f"{file_name}.json", "w") as unl_file:
    unl_file.write(read_unl_json_pprint)
'''

# Open a file to store output #
node_ip_config = open(f"{file_name}-ip-config.txt", "w")

# Define pair of nodes connected to same P2P link #
node_pair = []

# Find dict for nodes #
nodes = read_unl_dict["lab"]["topology"]["nodes"]["node"]

# Start to iterate nodes #
for item in range(0, len(nodes)):
    node = nodes[item]
    node_id = node["@id"]
    node_name = node["@name"]
    node_type = node["@type"]
    interfaces = node["interface"]

    if node_type == "dynamips":
        node_commands = "\n"
        node_commands += "!\n"
        node_commands += "conf t\n"

        # Start to iterate node > interface #
        for i in range (0, len(interfaces)):
            interface = interfaces[i]
            interface_name = interface["@name"]
            interface_net_id = interface["@network_id"]

            # Find dict for networks #
            networks = read_unl_dict["lab"]["topology"]["networks"]["network"]
            
            # Start to iterate networks #
            for item in range(0, len(networks)):
                network = networks[item]
                main_net_id = network["@id"]
                main_net_type = network["@type"]

                if main_net_id is interface_net_id and "pnet" not in main_net_type:
                    node_commands += f" interface {interface_name}\n"

                    next_nodes = read_unl_dict["lab"]["topology"]["nodes"]["node"]
                    # Start to iterate next nodes #
                    for item in range(0, len(next_nodes)):
                        next_node = next_nodes[item]
                        next_node_id = next_node["@id"]
                        next_node_name = next_node["@name"]
                        next_node_type = next_node["@type"]
                        next_node_interfaces = next_node["interface"]
                        
                        # Self node id not eq to next node id #
                        if next_node_id is not node_id and next_node_type != "qemu":                                
                            for i in range (0, len(next_node_interfaces)):
                                #print(f"{next_node_id} : {len(next_node_interfaces)}") #########################
                                next_node_interface = next_node_interfaces[i]        
                                next_node_net_id = next_node_interface["@network_id"]
                                if next_node_net_id is interface_net_id:
                                    node_pair1 = node_id + next_node_id ### 12
                                    node_pair2 = next_node_id + node_id  ### 21       
                                    if node_pair1 not in node_pair and node_pair2 not in node_pair:
                                        if int(node_pair1) < int(node_pair2):
                                            node_pair.append(node_pair1)
                                            node_commands += f"  ip address 10.0.{node_pair1}.1 255.255.255.252\n"
                                            node_commands += f"  description ** Connected to {next_node_name} **\n"           
                                        elif int(node_pair2) < int(node_pair1):
                                            node_pair.append(node_pair2)
                                            node_commands += f"  ip address 10.0.{node_pair2}.2 255.255.255.252\n"
                                            node_commands += f"  description ** Connected to {next_node_name} **\n"
                                    elif node_pair1 in node_pair or node_pair2 in node_pair:
                                        if int(node_pair1) < int(node_pair2):
                                            node_commands += f"  ip address 10.0.{node_pair1}.1 255.255.255.252\n"
                                            node_commands += f"  description ** Connected to {next_node_name} **\n"    
                                        elif node_pair2 < node_pair1:
                                            node_commands += f"  ip address 10.0.{node_pair2}.2 255.255.255.252\n"
                                            node_commands += f"  description ** Connected to {next_node_name} **\n"
                                            
                    node_commands += f"  no shutdown\n"
                    node_commands += f"!\n"

                elif main_net_id is interface_net_id and "pnet" in main_net_type:
                    node_commands += f" interface {interface_name}\n"
                    node_commands += f"  ip address 10.99.99.{node_id} 255.255.0.0\n"
                    node_commands += f"  description ** Connected to MGMT **\n"
                    node_commands += f"  no shutdown\n"
                    node_commands += f"!\n"

    else:
        node_commands = f"\n"
        node_commands += f"{node_name} node type: '{node_type}'\n"
        node_commands += f"Note type not supported by this script.\n"
        node_commands += f"\n"

    node_ip_config.write(f"{node_name}\n")
    node_ip_config.write('=' * len(node_name) + '\n')
    node_ip_config.write(f"{node_commands}")
    node_ip_config.write(f"\n")

node_ip_config.close()