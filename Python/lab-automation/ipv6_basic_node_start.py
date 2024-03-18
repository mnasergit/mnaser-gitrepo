import requests
from pprint import pprint
import time
from lab_variable import EVE_1, EVE_USER, EVE_PASSWORD

lab_name = "IPv6-Basic-Connectivity-Lab"
lab_name_check = f"/{lab_name}.unl"

### Login ###

login_url = f"http://{EVE_1}/api/auth/login"
cred = '{{"username":"{}","password":"{}","html5":"-1"}}'.format(EVE_USER, EVE_PASSWORD)
headers = {"Accept":"application/json"}

login_api = requests.post(url=login_url, data=cred)
cookies = login_api.cookies

# Start Lab Node ##

# 1. Count number of nodes
node_status_url = f"http://{EVE_1}/api/labs/IPv6-Basic-Connectivity-Lab.unl/nodes"
node_status_api = requests.get(url=node_status_url,cookies=cookies,headers=headers)

node_status_api_response = node_status_api.json()
#pprint (node_status_api_response)

node_status_dict = node_status_api_response['data']
num_nodes = len(node_status_dict)

print()

if node_status_api:
    try:
        # Start nodes that are not running
        j = 0
        for i in range (1, int(num_nodes + 1)):
            device_status = node_status_dict[f"{i}"]["status"]
            #print (device_status)
            
            if device_status == 2:
                j = j + 1
            if device_status != 2 and device_status != 0:
                pass
            elif device_status == 0:
                node_start_url = f"http://{EVE_1}/api/labs/IPv6-Basic-Connectivity-Lab.unl/nodes/{i}/start"
                node_start_api = requests.get(url=node_start_url,cookies=cookies,headers=headers)
                j = j + 1
                time.sleep(3)

                #node_start_response = node_start_api.json()
                #print (node_start_response)

            else:
                pass

        if j == int(num_nodes):
            print (f"Nodes are already running.")
            print (f"")
            print (f"Click on 'Monitor Node' button to check latest status of all node.")   
        elif j == 0:
            print (f"No node found to be started.")
        elif j != int(num_nodes) and j >= 1:
            print(f"Nodes are started. Click on Monitor Node to check latest status of all node..")
        else:
            pass

    except:
        print("No node couldn't be started")

else:
    print ("No node couldn't be started")
