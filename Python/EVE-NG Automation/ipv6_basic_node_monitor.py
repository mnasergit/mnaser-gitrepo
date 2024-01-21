import requests
import json
from pprint import pprint
import time
import sys
import app
import re
from datetime import datetime


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

        # Check Status of Node #

        node_status_url = f"http://192.168.20.12/api/labs/IPv6-Basic-Connectivity-Lab.unl/nodes"
        node_status_api = requests.get(url=node_status_url,cookies=cookies,headers=headers)

        node_status_api_response = node_status_api.json()
        #pprint (node_status_api_response)

        node_status_dict = node_status_api_response['data']

        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"Node status last updated on: {formatted_time}")
        print()

        for i in range (1, num_group + 1):
            device_status = node_status_dict[f"{i}"]["status"]
            
            
            if device_status == 2:
                print (f"Group{i}-Router1 is is running....")
            elif device_status == 0:
                print (f"Group{i}-Router1 is stopped.")
            else:
                pass
        
        for i in range (num_group + 1, num_group*2 + 1 ):
            device_status = node_status_dict[f"{i}"]["status"]

            if device_status == 2:
                print (f"Group{i - num_group}-Host1 is is running....")
            elif device_status == 0:
                print (f"Group{i - num_group}-Host1 is stopped.")
            else:
                pass


        
    except:
        print("Error: Lab provisioning is not successful!")