import requests
import json
from pprint import pprint
import time

### Login ###

login_url = "http://192.168.20.12/api/auth/login"
cred = '{"username":"admin","password":"eve","html5":"-1"}'
headers = {"Accept":"application/json"}

login_api = requests.post(url=login_url, data=cred)
cookies = login_api.cookies

if login_api:
    print("Login: successful")
else:
    print("Login: Not successful")

#print(f"Login cookies: {cookies}")

login_api_response = login_api.json()
#print (login_api_response)



# Start Lab Node ##

# 1. Count number of nodes
node_status_url = f"http://192.168.20.12/api/labs/IPv6-Basic-Connectivity-Lab.unl/nodes"
node_status_api = requests.get(url=node_status_url,cookies=cookies,headers=headers)

node_status_api_response = node_status_api.json()
#pprint (node_status_api_response)

node_status_dict = node_status_api_response['data']
num_nodes = len(node_status_dict)

print (num_nodes)

# 1. Start nodes that are not running
j = 0
for i in range (1, int(num_nodes/2 + 1)):
    device_status = node_status_dict[f"{i}"]["status"]
    print (device_status)
    
    if device_status == 2:
        j = j + 1
    if device_status != 2 and device_status != 0:
        pass
    elif device_status == 0:
        node_start_url = f"http://192.168.20.12/api/labs/IPv6-Basic-Connectivity-Lab.unl/nodes/{i}/start"
        node_start_api = requests.get(url=node_start_url,cookies=cookies,headers=headers)
        j = j + 1
        time.sleep(5)

        node_start_response = node_start_api.json()
        print (node_start_response)

    else:
        pass

if j == int(num_nodes/2):
    print (f"All  nods are already running.")    
if j == 0:
    print (f"No node found to be started.")
    print()
if j != int(num_nodes/2) and j >= 1:
    print(f"Nodes are started. Click on Monitor Node to check latest status of all node.")
    print()



    
'''
# Stop Lab Node ##
for i in range (1, 11):    
    create_lab_url = f"http://192.168.20.12/api/labs/IPv6-Basic-Lab.unl/nodes/{j}/stop"
    create_lab_api = requests.get(url=create_lab_url,cookies=cookies,headers=headers)
    time.sleep(1)
    create_lab_response = create_lab_api.json()
    print (create_lab_response)

'''


'''
### Delete Nodes ###

def delete_node(*args):
    for node_id in args:
        delete_node_url = f"http://192.168.20.12/api/labs/{lab_name_check}/nodes/{node_id}"
        delete_node_api = requests.delete(url=delete_node_url,cookies=cookies,headers=headers)

        response = delete_api.json()
        print (response)

node_id = (input("Enter node id: ").split(","))
delete_node(*node_id)

    
'''


'''

# Check Status of Node #


node_status_url = f"http://192.168.20.12/api/labs/IPv6-Basic-Connectivity-Lab.unl/nodes"
node_status_api = requests.get(url=node_status_url,cookies=cookies,headers=headers)

node_status_api_response = node_status_api.json()
pprint (node_status_api_response)

node_status_dict = node_status_api_response['data']
num_nodes = len(node_status_dict)

print (num_nodes)

for i in range (1, num_nodes + 1):
    device_status = node_status_dict[f"{i}"]["status"]

    if device_status is 2:
        print (f"Node {i} is running....")
    elif device_status is 0:
        print (f"Node {i} is stopped.")
    else:
        pass

'''