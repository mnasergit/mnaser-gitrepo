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
print (login_api_response)


'''
# Start Lab Node ##
for i in range (1, 11):    
    create_lab_url = f"http://192.168.20.12/api/labs/IPv6-Basic-Connectivity-Lab.unl/nodes/{i}/start"
    create_lab_api = requests.get(url=create_lab_url,cookies=cookies,headers=headers)
    time.sleep(5)
    create_lab_response = create_lab_api.json()
    print (create_lab_response)
'''
    
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


# Check Status of Node #


node_status_url = f"http://192.168.20.12/api/labs/IPv6-Basic-Connectivity-Lab.unl/nodes"
node_status_api = requests.get(url=node_status_url,cookies=cookies,headers=headers)

node_status_api_response = node_status_api.json()
pprint (node_status_api_response)

node_status_dict = node_status_api_response['data']

''''
for i in range (1, 11):
    device_status = node_status_dict[f"{i}"]["status"]

    if device_status is 2:
        print (f"Node {i} is running....")
    elif device_status is 0:
        print (f"Node {i} is stopped.")
    else:
        pass

'''