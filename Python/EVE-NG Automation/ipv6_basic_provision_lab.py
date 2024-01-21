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

        print ("")
        if login_api:
            print("Login into EVE-NG is successful.")
        else:
            print("Login into EVE-NG is not successful.")
        print ("")

        #print(f"Login cookies: {cookies}")

        #login_api_response = login_api.json()
        #print (login_api_response)

        ### Get folder list ###

        get_folder_url = "http://192.168.20.12/api/folders/"
        get_folder_api = requests.get(url=get_folder_url,cookies=cookies,headers=headers)

        get_folder_response = get_folder_api.json()

        get_folder_response_dict = get_folder_response['data']
        #pprint (get_folder_response_dict)

        existing_labs = [lab['path'] for lab in get_folder_response_dict['labs']]

       
        ### Create New Lab ###
        ### This verson can't check labs under folders ###

        if lab_name_check not in existing_labs:
            def create_lab(lab_name):
                lab_data = {"author":"","description":"","scripttimeout":300,"version":1,"name":f"{lab_name}","body":"","path":"/"}
                lab_data = json.dumps(lab_data)
                
                create_lab_url = "http://192.168.20.12/api/labs"
                create_lab_api = requests.post(url=create_lab_url,data=lab_data,cookies=cookies,headers=headers)

                #create_lab_response = create_lab_api.json()
                #print (create_lab_response)
            
            create_lab(lab_name)

            print (f"{lab_name} is created.")
            print ("")

            ### Create Nodes in New Lab ###

            def create_node(ios_num, slax_num):
                left_position = 100
                for i in range(1, ios_num + 1):
                    ios_data = {"template":"c7200","type":"dynamips","count":"1","image":"c7200-adventerprisek9-mz.152-4.S6.image","name":f"Group{i}-Host1","icon":"Router.png","idlepc":"0x62f21000","nvram":"128","ram":"256","slot1":"PA-FE-TX","slot2":"PA-FE-TX","slot3":"PA-FE-TX","slot4":"PA-FE-TX","slot5":"PA-FE-TX","slot6":"PA-FE-TX","config":"0","delay":"0","left":f"{left_position}","top":"150","postfix":0}

                    left_position = left_position + 120
                    ios_data = json.dumps(ios_data)

                    create_node_url = f"http://192.168.20.12/api/labs/{lab_name_check}/nodes"
                    create_node_api = requests.post(url=create_node_url,data=ios_data,cookies=cookies,headers=headers)

                #     if create_node_api:
                #         print(f"IOS node Group{i}-Router1 is created.")
                #     else:
                #         print(f"IOS node Group{i}-Router1 creation is not successful")
                
                # print ("")

                left_position = 100
                for j in range(1, slax_num + 1):
                    slax_data = {"template":"linux","type":"qemu","count":"1","image":"linux-slax-9.11.0","name":f"Group{j}-Host1","icon":"Server.png","uuid":"","cpulimit":"undefined","cpu":"1","ram":"512","ethernet":"1","firstmac":"","qemu_version":"","qemu_arch":"","qemu_nic":"","qemu_options":"-machine type: pc,accel=kvm -vga std -usbdevice tablet -boot order=cd -cpu host","ro_qemu_options":"-machine type=pc,accel=kvm -vga std -usbdevice tablet -boot order=cd -cpu host","config":"0","delay":"0","console":"vnc","left":f"{left_position}","top":"350","postfix":0}

                    left_position = left_position + 120
                    slax_data = json.dumps(slax_data)

                    create_node_url = f"http://192.168.20.12/api/labs/{lab_name_check}/nodes"
                    create_node_api = requests.post(url=create_node_url,data=slax_data,cookies=cookies,headers=headers)

                #     if create_node_api:
                #         print(f"SLAX node Group{j}-Host1 is created")
                #     else:
                #         print(f"SLAX node Group{j}-Host1 creation is not successful")
                    
                #     #create_node_api_response = create_node_api.json()
                #     #print (create_node_api_response)
                
                # print ("")        

            #num_ios = int(input("Enter number IOS router: "))
            #num_slax = int(input("Enter number SLAX host: "))

            create_node(num_ios, num_slax)

            ### Create BRIDGE Network ###
                
            left_position = 100
            for i in range(1, num_slax + 1):
                bridge_data = {"type":"bridge","visibility":1,"left":f"{left_position}","top":"250","postfix":0}
                bridge_data = json.dumps(bridge_data)
                left_position = left_position + 120

                create_bridge_url = f"http://192.168.20.12/api/labs/{lab_name_check}/networks"
                create_bridge_api = requests.post(url=create_bridge_url,data=bridge_data,cookies=cookies)

                #create_bridge_url_response = create_bridge_api.json()
                #print (create_bridge_url_response)

            #     if create_bridge_api:
            #         print(f"Bridge network{i} is created")
            #     else:
            #         print(f"Bridge network{i} creation is not successful")

            # print ("")

            ### Connect IOS Interfaces to Bridges ###

            for i in range (1, num_ios + 1):
                add_intf_url = f"http://192.168.20.12/api/labs/{lab_name_check}/nodes/{i}/interfaces"
                int_map = {"0":f"{i}"} # "intf_id_of_node":"net_id"
                int_map = json.dumps(int_map)
                
                add_intf_api = requests.put(url=add_intf_url,data=int_map,cookies=cookies,headers=headers)

                #add_intf_api_response = add_intf_api.json()
                #print (add_intf_api_response)

            #     if add_intf_api:
            #         print(f"IOS node Group{i}-Router1 is connected to Bridge network{i}")
            #     else:
            #         print(f"IOS node Group{i}-Router1 couldn't connected to Bridge network{i}")

            # print ("")    

            ### Connect SLAX Interfaces to Bridges ###

            j = 1    
            for i in range (num_ios + 1, num_ios + num_slax + 1):
                add_intf_url = f"http://192.168.20.12/api/labs/{lab_name_check}/nodes/{i}/interfaces"
                int_map = {"0":f"{j}"} # "intf_id_of_node":"net_id"
                int_map = json.dumps(int_map)
                
                add_intf_api = requests.put(url=add_intf_url,data=int_map,cookies=cookies,headers=headers)

                #add_intf_api_response = add_intf_api.json()
                #print (add_intf_api_response)

            #     if add_intf_api:
            #         print(f"SLAX node Group{j}-Host1 is connected to Bridge network{j}")
            #     else:
            #         print(f"SLAX node Group{j}-Host1 couldn't connected to Bridge network{j}")
                
            #     j = j + 1
                
            # print ("")  

            ### Create PNET1 Network ###

            pnet_data = {"count":"1","visibility":"1","name":"Net","type":"pnet1","left":"600","top":"50","postfix":0}
            pnet_data = json.dumps(pnet_data)

            create_pnet_url = f"http://192.168.20.12/api/labs/{lab_name_check}/networks"
            create_pnet_api = requests.post(url=create_pnet_url,data=pnet_data,cookies=cookies)

            #create_pnet_url_response = create_pnet_api.json()
            #print (create_pnet_url_response)

            # if create_bridge_api:
            #     print(f"MGMT network is created")
            # else:
            #     print(f"MGMT network creation is not successful")

            # print ("")  

            ### Connect MGMT Interface to PNET1 network ###

            for i in range (1, num_ios + 1):
                add_mgmt_url = f"http://192.168.20.12/api/labs/{lab_name_check}/nodes/{i}/interfaces"
                mgmt_map = {"96":f"{num_group+1}"} # "intf_id_of_node":"net_id"
                mgmt_map = json.dumps(mgmt_map)
                add_mgmt_api = requests.put(url=add_mgmt_url,data=mgmt_map,cookies=cookies,headers=headers)

                #add_mgmt_api_response = add_mgmt_api.json()
                #print (add_mgmt_api_response)

            #     if add_mgmt_api:
            #         print(f"IOS node Group{i}-Router1 is connected to MGMT network")
            #     else:
            #         print(f"IOS node Group{i}-Router1 couldn't connected to MGMT network")

            # print ("")  

            ### Push startup-configs ###
            
            for i in range (1, num_group + 1):    
                # Read the contents of the text file
                json_data = {"id": "1", "data": ""}

                with open(f"ipv6_basic_out_files/Group{i}-Router1-startup-config.txt", "r") as file:
                    #print (f"Reading {HOST}-startup-config.txt")
                    json_data["data"] = file.read()
        
                    # Convert the Python dictionary to a JSON string
                    json_string = json.dumps(json_data, indent=2)
                    #print (json_string)
                    #print (type(json_string))

                    # Save the JSON string to a new file
                    #with open('output.json', 'w') as json_file:
                    #    json_file.write(json_string)

                    #print("Conversion complete. JSON file saved as 'output.json'.")


                    ### Push Config ###

                    #def create_lab(lab_name):
                    push_config_data = json_string

                    #print ("Lab data: " + lab_data)
                    #lab_data = json.dumps(lab_data)
                            
                    push_config_url = f"http://192.168.20.12/api/labs/{lab_name_check}/configs/{i}"
                    push_config_api = requests.put(url=push_config_url,data=push_config_data,cookies=cookies,headers=headers)

                    #create_lab_response = create_lab_api.json()
                    #print (create_lab_response)


                    ### Set Config Bit ###

                    #def create_lab(lab_name):
                    #lab_data = {"id":"1","count":"1","postfix":0,"config":"1"}
                    config_bit_data = {"id":1,"count":1,"postfix":0,"config":1}
                    config_bit_data = json.dumps(config_bit_data)
                            
                    config_bit_url = f"http://192.168.20.12/api/labs/{lab_name_check}/nodes/{i}"
                    config_bit_api = requests.put(url=config_bit_url,data=config_bit_data,cookies=cookies,headers=headers)

                    #create_lab_response = create_lab_api.json()
                    #print (create_lab_response)

                    # if push_config_api and config_bit_api:
                    #     print(f"IOS node Group{i}-Router1 is set with startup-config")
                    # else:
                    #     print(f"IOS node Group{i}-Router1 couldn't set with startup-config")
            
            print ("Lab is provisioned successfully.")
                    

        else:
            print("Existing labs:")
            print (existing_labs)
            print ("")
            print ("Lab name confilcts with existing one. Delete that lab and try again.")

    except:
        print("Error: Lab provisioning is not successful!")