import requests
import json
from pprint import pprint
import time
import sys
import app
import re

def process_variable(input_value):
    #print(f"Processing input value: {input_value}")
    # Your processing logic here
    #num_group = f"Processed variable: {input_value}"
    #num_group = int(input_value)
    #print(f"Result: {num_group}")
    #return num_group

    match = re.search(r'\b\d+\b', input_value)
    if match:
        num_group = match.group()
        return num_group
    else:
        return "0"  # Return a default value if no numeric part is found


if __name__ == "__main__":
    try:
        # Get the input value from the command line argument
        input_value = sys.argv[1]
        num_group = process_variable(input_value)
        num_group = int(num_group)

        ### User Input ###

        #lab_name = str(input("Enter lab name : "))
        lab_name = "IPv6-Basic-Connectivity-Lab"
        lab_name_check = f"/{lab_name}.unl"
        #num_group = int(input("Enter number Group for Basic IPv6 Connectivity Lab: "))
        num_ios = num_group
        num_slax = num_group

        ### Login ###

        login_url = "http://192.168.20.12/api/auth/login"
        cred = '{"username":"admin","password":"eve","html5":"-1"}'
        headers = {"Accept":"application/json"}

        login_api = requests.post(url=login_url, data=cred)
        cookies = login_api.cookies

        # Start Lab Node ##
        
        for i in range (1, num_group + 1):
            node_start_url = f"http://192.168.20.12/api/labs/IPv6-Basic-Connectivity-Lab.unl/nodes/{i}/start"
            node_start_api = requests.get(url=node_start_url,cookies=cookies,headers=headers)

            #node_start_api_response = node_start_api.json()
            #pprint (node_start_api_response)

            # if node_start_api:
            #     print (f"Group{i}-Router1 is started....")
            # else:
            #     print (f"Group{i}-Router1 is not started.")

        
        j = 1        
        for i in range (num_group + 1, num_group*2 + 1 ):
            node_start_url = f"http://192.168.20.12/api/labs/IPv6-Basic-Connectivity-Lab.unl/nodes/{i}/start"
            node_start_api = requests.get(url=node_start_url,cookies=cookies,headers=headers)

            #node_start_api_response = node_start_api.json()
            #pprint (node_start_api_response)

            # if node_start_api:
            #     print (f"Group{j}-Host1 is started....")
            # else:
            #     print (f"Group{j}-Host1 is not started.")
            j = j + 1
       
        print(f"Nodes are started. Click on Monitor Node to check latest status of all node.")
        print()
        
        
    except:
        print("Error: Lab provisioning is not successful!")