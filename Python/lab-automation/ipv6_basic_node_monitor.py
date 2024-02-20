import requests
import json
from pprint import pprint
import time
import sys
import app
import re
from datetime import datetime
from lab_variable import EVE_1, EVE_USER, EVE_PASSWORD

### User Input ###

#EVE_1 = "192.168.30.12"
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

current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

print()
print(f"Node status: (last updated on {formatted_time})")
print()

if node_status_api:
    try:
        for i in range (1, int(num_nodes/2) + 1):
            device_status = node_status_dict[f"{i}"]["status"]
            
            if device_status == 2:
                print (f"Group{i}-Router1 is is running....")
            elif device_status == 0:
                print (f"Group{i}-Router1 is stopped.")
            else:
                pass

        for i in range (int(num_nodes/2) + 1, num_nodes*2 + 1 ):
            device_status = node_status_dict[f"{i}"]["status"]

            if device_status == 2:
                print (f"Group{i - int(num_nodes/2)}-Host1 is is running....")
            elif device_status == 0:
                print (f"Group{i - int(num_nodes/2)}-Host1 is stopped.")
            else:
                pass

    except:
        #print("Error: Lab provisioning is not successful!")
        pass

else:
    print("Error: Lab provisioning is not successful!")
    pass
