import openpyxl
from openpyxl import Workbook
from openpyxl.styles import PatternFill
import requests
import json
from pprint import pprint
import sqlite3
from lab_variable import EVE_1, EVE_2, EVE_USER, EVE_PASSWORD, EVE_1_IDLE_PC, EVE_2_IDLE_PC, num_group_eve_1

# Connect to the same SQLite database
conn = sqlite3.connect('lab_data.db')
cursor = conn.cursor()

# Retrieve the value from the table
cursor.execute("SELECT value FROM table_basic_ipv6")
input_value = cursor.fetchone()[0]
lab_name = "IPv6-Basic-Connectivity-Lab"
lab_name_check = f"/{lab_name}.unl"
num_group = int(input_value)
num_group_eve_2 = num_group - num_group_eve_1
num_ios = num_group
num_slax = num_group
num_ios_eve_1 = num_group_eve_1
num_slax_eve_1 = num_group_eve_1
num_ios_eve_2 = num_group_eve_2
num_slax_eve_2 = num_group_eve_2
headers = {"Accept":"application/json"}

def eve_ng_login():
    cookies1 = None
    cookies2 = None
    
    ### Login into EVE1 ###
    try:
        login_url = f"http://{EVE_1}/api/auth/login"
        cred = '{{"username":"{}","password":"{}","html5":"-1"}}'.format(EVE_USER, EVE_PASSWORD)

        login_api = requests.post(url=login_url, data=cred, headers=headers)
        cookies1 = login_api.cookies

        if login_api:
            print("Login into EVE-NG-1 is successful.")
        else:
            print("Login into EVE-NG-1 is not successful.")
        print ("")
    
    except:
        print("Login into EVE-NG-1 is not successful.")


    ### Login into EVE2 ###
    if num_group_eve_2 > 0:
        try:
            login_url = f"http://{EVE_2}/api/auth/login"
            cred = '{{"username":"{}","password":"{}","html5":"-1"}}'.format(EVE_USER, EVE_PASSWORD)

            login_api = requests.post(url=login_url, data=cred, headers=headers)
            cookies2 = login_api.cookies

            if login_api:
                print("Login into EVE-NG-2 is successful.")
            else:
                print("Login into EVE-NG-2 is not successful.")
            print ("")
        
        except:
            print("Login into EVE-NG-2 is not successful.")

    return cookies1, cookies2

def check_lab(cookies1, cookies2):
    existing_labs_1 = None
    existing_labs_2 = None

    if cookies1 is not None:
        ### Get folder list of EVE1 ###

        get_folder_url = f"http://{EVE_1}/api/folders/"
        get_folder_api = requests.get(url=get_folder_url,cookies=cookies1,headers=headers)

        get_folder_response = get_folder_api.json()

        get_folder_response_dict = get_folder_response['data']
        #pprint (get_folder_response_dict)

        existing_labs_1 = [lab['path'] for lab in get_folder_response_dict['labs']]

    if cookies2 is not None:
        if num_group_eve_2 > 0:
        ### Get folder list of EVE2 ###

            get_folder_url = f"http://{EVE_1}/api/folders/"
            get_folder_api = requests.get(url=get_folder_url,cookies=cookies1,headers=headers)

            get_folder_response = get_folder_api.json()

            get_folder_response_dict = get_folder_response['data']
            #pprint (get_folder_response_dict)

            existing_labs_2 = [lab['path'] for lab in get_folder_response_dict['labs']]
    
    return existing_labs_1, existing_labs_2

def create_lab(cookies1, cookies2, existing_labs_1, existing_labs_2):

    # if cookies1 and existing_labs_1 is not None:
    #     ### Create New Lab in EVE1 ###
    #     ### This verson can't check labs under folders ###

    if lab_name_check not in existing_labs_1:
        lab_data = {"author":"","description":"","scripttimeout":300,"version":1,"name":f"{lab_name}","body":"","path":"/"}
        lab_data = json.dumps(lab_data)
        
        create_lab_url = f"http://{EVE_1}/api/labs"
        create_lab_api = requests.post(url=create_lab_url,data=lab_data,cookies=cookies1,headers=headers)

        #create_lab_response = create_lab_api.json()
        #print (create_lab_response)

        print (f"{lab_name} is created in EVE-NG-1.")
        print ("")
        PASS1 = True
    else:
        print (f"{lab_name}: lab name conflicts in EVE-NG-1. Delete that lab and try again.")
        print ("")
        PASS1 = False

    # if cookies2 and existing_labs_2 is not None:
    #     ### Create New Lab in EVE2 ###
    #     ### This verson can't check labs under folders ###
    if num_group_eve_2 > 0:
        if lab_name_check not in existing_labs_2:
            lab_data = {"author":"","description":"","scripttimeout":300,"version":1,"name":f"{lab_name}","body":"","path":"/"}
            lab_data = json.dumps(lab_data)
            
            create_lab_url = f"http://{EVE_2}/api/labs"
            create_lab_api = requests.post(url=create_lab_url,data=lab_data,cookies=cookies2,headers=headers)
                        
            print (f"{lab_name} is created in EVE-NG-2.")
            print ("")   
            PASS2 = True

        else:
            print (f"{lab_name}: lab name conflicts in EVE-NG-2. Delete that lab and try again.")
            print ("")
            PASS2 = False
    
    if num_group_eve_2 == 0:
            PASS2 = True

    return PASS1, PASS2

def create_node(cookies1, cookies2):
    ### Create Nodes in EVE1 ###
    left_position = 100
    for i in range(1, num_ios_eve_1 + 1):
        ios_data = {"template":"c7200","type":"dynamips","count":"1","image":"c7200-adventerprisek9-mz.152-4.S6.image","name":f"Group{i}-Router1","icon":"Router.png","idlepc":f"{EVE_1_IDLE_PC}","nvram":"128","ram":"256","slot1":"PA-FE-TX","slot2":"PA-FE-TX","slot3":"PA-FE-TX","slot4":"PA-FE-TX","slot5":"PA-FE-TX","slot6":"PA-FE-TX","config":"0","delay":"0","left":f"{left_position}","top":"150","postfix":0}

        left_position = left_position + 120
        ios_data = json.dumps(ios_data)

        create_node_url = f"http://{EVE_1}/api/labs/{lab_name_check}/nodes"
        create_node_api = requests.post(url=create_node_url,data=ios_data,cookies=cookies1,headers=headers)


    left_position = 100
    for j in range(1, num_slax_eve_1 + 1):
        slax_data = {"template":"linux","type":"qemu","count":"1","image":"linux-slax-9.11.1","name":f"Group{j}-Host1","icon":"Server.png","uuid":"","cpulimit":"undefined","cpu":"1","ram":"512","ethernet":"1","firstmac":"","qemu_version":"","qemu_arch":"","qemu_nic":"","qemu_options":"-machine type: pc,accel=kvm -vga std -usbdevice tablet -boot order=cd -cpu host","qemu_options":"-machine type=pc,accel=kvm -vga std -usbdevice tablet -boot order=cd -cpu host","config":"0","delay":"0","console":"vnc","left":f"{left_position}","top":"350","postfix":0}

        left_position = left_position + 120
        slax_data = json.dumps(slax_data)

        create_node_url = f"http://{EVE_1}/api/labs/{lab_name_check}/nodes"
        create_node_api = requests.post(url=create_node_url,data=slax_data,cookies=cookies1,headers=headers)

    ### Create Nodes in EVE2 ###
    left_position = 100
    for i in range(num_ios_eve_1 + 1, num_ios + 1):
        ios_data = {"template":"c7200","type":"dynamips","count":"1","image":"c7200-adventerprisek9-mz.152-4.S6.image","name":f"Group{i}-Router1","icon":"Router.png","idlepc":f"{EVE_2_IDLE_PC}","nvram":"128","ram":"256","slot1":"PA-FE-TX","slot2":"PA-FE-TX","slot3":"PA-FE-TX","slot4":"PA-FE-TX","slot5":"PA-FE-TX","slot6":"PA-FE-TX","config":"0","delay":"0","left":f"{left_position}","top":"150","postfix":0}

        left_position = left_position + 120
        ios_data = json.dumps(ios_data)

        create_node_url = f"http://{EVE_2}/api/labs/{lab_name_check}/nodes"
        create_node_api = requests.post(url=create_node_url,data=ios_data,cookies=cookies2,headers=headers)

    left_position = 100
    for j in range(num_slax_eve_1 + 1, num_slax + 1):
        slax_data = {"template":"linux","type":"qemu","count":"1","image":"linux-slax-9.11.1","name":f"Group{j}-Host1","icon":"Server.png","uuid":"","cpulimit":"undefined","cpu":"1","ram":"512","ethernet":"1","firstmac":"","qemu_version":"","qemu_arch":"","qemu_nic":"","qemu_options":"-machine type: pc,accel=kvm -vga std -usbdevice tablet -boot order=cd -cpu host","qemu_options":"-machine type=pc,accel=kvm -vga std -usbdevice tablet -boot order=cd -cpu host","config":"0","delay":"0","console":"vnc","left":f"{left_position}","top":"350","postfix":0}

        left_position = left_position + 120
        slax_data = json.dumps(slax_data)

        create_node_url = f"http://{EVE_2}/api/labs/{lab_name_check}/nodes"
        create_node_api = requests.post(url=create_node_url,data=slax_data,cookies=cookies2,headers=headers)

def create_bridge_network(cookies1, cookies2):

    ### Create BRIDGE Network in EVE1 ###
    left_position = 100
    for i in range(1, num_ios_eve_1 + 1):
        bridge_data = {"type":"bridge","visibility":1,"left":f"{left_position}","top":"250","postfix":0}
        bridge_data = json.dumps(bridge_data)
        left_position = left_position + 120

        create_bridge_url = f"http://{EVE_1}/api/labs/{lab_name_check}/networks"
        create_bridge_api = requests.post(url=create_bridge_url,data=bridge_data,cookies=cookies1)

    ### Create BRIDGE Network in EVE2 ###
    left_position = 100
    for i in range(num_ios_eve_1 + 1, num_ios + 1):
        bridge_data = {"type":"bridge","visibility":1,"left":f"{left_position}","top":"250","postfix":0}
        bridge_data = json.dumps(bridge_data)
        left_position = left_position + 120

        create_bridge_url = f"http://{EVE_2}/api/labs/{lab_name_check}/networks"
        create_bridge_api = requests.post(url=create_bridge_url,data=bridge_data,cookies=cookies2)     

def connect_ios_to_bridge(cookies1, cookies2):
   
    ### Connect IOS Interfaces to Bridges in EVE1 ###
    for i in range (1, num_ios_eve_1 + 1):
        add_intf_url = f"http://{EVE_1}/api/labs/{lab_name_check}/nodes/{i}/interfaces"
        int_map = {"0":f"{i}"} # "intf_id_of_node":"net_id"
        int_map = json.dumps(int_map)
        
        add_intf_api = requests.put(url=add_intf_url,data=int_map,cookies=cookies1,headers=headers)

    ### Connect IOS Interfaces to Bridges in EVE2 ###
    for i in range (1, num_ios_eve_2 + 1):
        add_intf_url = f"http://{EVE_2}/api/labs/{lab_name_check}/nodes/{i}/interfaces"
        int_map = {"0":f"{i}"} # "intf_id_of_node":"net_id"
        int_map = json.dumps(int_map)
        
        add_intf_api = requests.put(url=add_intf_url,data=int_map,cookies=cookies2,headers=headers)
        
def connect_slax_to_bridge(cookies1, cookies2):
    ### Connect SLAX Interfaces to Bridges in EVE1 ###
    j = 1    
    for i in range (num_ios_eve_1 + 1, num_ios_eve_1 + num_slax_eve_1 + 1):
        add_intf_url = f"http://{EVE_1}/api/labs/{lab_name_check}/nodes/{i}/interfaces"
        int_map = {"0":f"{j}"} # "intf_id_of_node":"net_id"
        int_map = json.dumps(int_map)
        j = j + 1
        
        add_intf_api = requests.put(url=add_intf_url,data=int_map,cookies=cookies1,headers=headers)

    ### Connect SLAX Interfaces to Bridges in EVE2 ###
    j = 1    
    for i in range (num_ios_eve_2 + 1, num_ios_eve_2 + num_slax_eve_2 + 1):
        add_intf_url = f"http://{EVE_2}/api/labs/{lab_name_check}/nodes/{i}/interfaces"
        int_map = {"0":f"{j}"} # "intf_id_of_node":"net_id"
        int_map = json.dumps(int_map)
        j = j + 1
        
        add_intf_api = requests.put(url=add_intf_url,data=int_map,cookies=cookies2,headers=headers)

def bridge_invisible(cookies1, cookies2):
    ### Make Bridge Network Invisible in EVE1 ###               
    for i in range(1, num_ios_eve_1 + 1):
        bridge_visibility_data = {"visibility":0}
        bridge_visibility_data = json.dumps(bridge_visibility_data)

        bridge_visibility_url = f"http://{EVE_1}/api/labs/{lab_name_check}/networks/{i}"
        bridge_visibility_api = requests.put(url=bridge_visibility_url,data=bridge_visibility_data,cookies=cookies1) 

    ### Make Bridge Network Invisible in EVE2 ###               
    for i in range(1, num_ios_eve_2 + 1):
        bridge_visibility_data = {"visibility":0}
        bridge_visibility_data = json.dumps(bridge_visibility_data)

        bridge_visibility_url = f"http://{EVE_2}/api/labs/{lab_name_check}/networks/{i}"
        bridge_visibility_api = requests.put(url=bridge_visibility_url,data=bridge_visibility_data,cookies=cookies2)

def create_mgmt_network(cookies1, cookies2):
    ### Create PNET1 Network in EVE1 ###

    pnet_data = {"count":"1","visibility":"1","name":"Net","type":"pnet1","left":"600","top":"50","postfix":0}
    pnet_data = json.dumps(pnet_data)

    create_pnet_url = f"http://{EVE_1}/api/labs/{lab_name_check}/networks"
    create_pnet_api = requests.post(url=create_pnet_url,data=pnet_data,cookies=cookies1)

    ### Create PNET1 Network in EVE2 ###

    pnet_data = {"count":"1","visibility":"1","name":"Net","type":"pnet1","left":"600","top":"50","postfix":0}
    pnet_data = json.dumps(pnet_data)

    create_pnet_url = f"http://{EVE_2}/api/labs/{lab_name_check}/networks"
    create_pnet_api = requests.post(url=create_pnet_url,data=pnet_data,cookies=cookies2)

def connect_ios_to_mgmt(cookies1, cookies2):
    ### Connect IOS to MGMT network in EVE1 ###
    for i in range (1, num_ios_eve_1 + 1):
        add_mgmt_url = f"http://{EVE_1}/api/labs/{lab_name_check}/nodes/{i}/interfaces"
        mgmt_map = {"96":f"{num_group_eve_1+1}"} # "intf_id_of_node":"net_id"
        mgmt_map = json.dumps(mgmt_map)
        add_mgmt_api = requests.put(url=add_mgmt_url,data=mgmt_map,cookies=cookies1,headers=headers)

    ### Connect IOS to MGMT network in EVE2 ###
    for i in range (1, num_ios_eve_2 + 1):
        add_mgmt_url = f"http://{EVE_2}/api/labs/{lab_name_check}/nodes/{i}/interfaces"
        mgmt_map = {"96":f"{num_group_eve_2+1}"} # "intf_id_of_node":"net_id"
        mgmt_map = json.dumps(mgmt_map)
        add_mgmt_api = requests.put(url=add_mgmt_url,data=mgmt_map,cookies=cookies2,headers=headers)


def push_startup_config(cookies1, cookies2):
    ### Push startup-configs in EVE1 ###
    j = 1
    for i in range (1, num_ios_eve_1 + 1):    
        # Read the contents of the text file
        json_data = {"id": "1", "data": ""}

        with open(f"ipv6_basic_config_files/Group{i}-Router1-startup-config.txt", "r") as file:
            #print (f"Reading {HOST}-startup-config.txt")
            json_data["data"] = file.read()

            # Convert the Python dictionary to a JSON string
            json_string = json.dumps(json_data, indent=2)

            # Save the JSON string to a new file
            #with open('output.json', 'w') as json_file:
            #    json_file.write(json_string)

            ### Push Config ###
            push_config_data = json_string

            #print ("Lab data: " + lab_data)
            #lab_data = json.dumps(lab_data)
                    
            push_config_url = f"http://{EVE_1}/api/labs/{lab_name_check}/configs/{j}"
            push_config_api = requests.put(url=push_config_url,data=push_config_data,cookies=cookies1,headers=headers)
            
            ### Set Config Bit in EVE1 ###
            config_bit_data = {"id":1,"count":1,"postfix":0,"config":1}
            config_bit_data = json.dumps(config_bit_data)
                    
            config_bit_url = f"http://{EVE_1}/api/labs/{lab_name_check}/nodes/{j}"
            config_bit_api = requests.put(url=config_bit_url,data=config_bit_data,cookies=cookies1,headers=headers)
    
            j = j + 1

    print("Lab provision is successfull in EVE-NG-1.")

    if num_group_eve_2 > 0:
        ### Push startup-configs in EVE2 ###
        j = 1
        for i in range (num_ios_eve_1 + 1, num_ios + 1):    
            # Read the contents of the text file
            json_data = {"id": "1", "data": ""}

            with open(f"ipv6_basic_config_files/Group{i}-Router1-startup-config.txt", "r") as file:
                #print (f"Reading {HOST}-startup-config.txt")
                json_data["data"] = file.read()

                # Convert the Python dictionary to a JSON string
                json_string = json.dumps(json_data, indent=2)

                # Save the JSON string to a new file
                #with open('output.json', 'w') as json_file:
                #    json_file.write(json_string)

                ### Push Config ###
                push_config_data = json_string

                #print ("Lab data: " + lab_data)
                #lab_data = json.dumps(lab_data)
                        
                push_config_url = f"http://{EVE_2}/api/labs/{lab_name_check}/configs/{j}"
                push_config_api = requests.put(url=push_config_url,data=push_config_data,cookies=cookies2,headers=headers)
                ### Set Config Bit in EVE2 ###
                config_bit_data = {"id":1,"count":1,"postfix":0,"config":1}
                config_bit_data = json.dumps(config_bit_data)
                        
                config_bit_url = f"http://{EVE_2}/api/labs/{lab_name_check}/nodes/{j}"
                config_bit_api = requests.put(url=config_bit_url,data=config_bit_data,cookies=cookies2,headers=headers)
                j = j + 1
        
        print("")
        print("Lab provision is successfull in EVE-NG-2.")

# Create ipv6-basic.html file
def create_index_html(create_index):
    new_index = ""
    lines = create_index.split('\n')
    replace_flag = False
    vnc_port = 32769 + int(num_group_eve_1)
    for line in lines:
        if line.strip().startswith("Router_Login"):
            replace_flag = True
            for i in range(1, num_group + 1):
                new_index += f"      <tr valign='top'>\n"
                new_index += f"        <td align='middle'>Group{i}-Router1</td>\n"
                new_index += f"        <td align='middle'>Jump Host</td>\n"
                new_index += f"        <td align='middle'>SSH</td>\n"
                new_index += f"        <td align='middle'>2406:6400:99::<b>{i}</b>:1</td>\n"
                new_index += f"        <td align='middle'>10.99.<b>{i}</b>.1</td>\n"
                new_index += f"      </tr>\n"
            new_index += f"    </table>\n"
        if line.strip().startswith("Host_Login"):
            replace_flag = True
            # For Slax Host in EVE-NG-1 #
            j = 0
            for i in range(1, num_group_eve_1 + 1):
                new_index += f"      <tr valign='top'>\n"
                new_index += f"        <td align='middle'>Group{i}-Host1</td>\n"
                new_index += f"        <td align='middle'>PC</td>\n"
                new_index += f"        <td align='middle'>VNC</td>\n"
                new_index += f"        <td align='middle'>2406:6400:99::99:<b>12</b>:<mark>{vnc_port}</mark></td>\n"
                new_index += f"        <td align='middle'>10.99.99.<b>12</b>:<mark>{vnc_port}</mark></td>\n"
                new_index += f"      </tr>\n"
                vnc_port = vnc_port + 1
                j = j + 1

            # For Slax Host in EVE-NG-2 #
            if num_group_eve_2 > 0:
                vnc_port = 32769 + int(num_group_eve_2)
                for i in range(j + 1, num_group_eve_1 + num_group_eve_2 + 1):
                    new_index += f"      <tr valign='top'>\n"
                    new_index += f"        <td align='middle'>Group{i}-Host1</td>\n"
                    new_index += f"        <td align='middle'>PC</td>\n"
                    new_index += f"        <td align='middle'>VNC</td>\n"
                    new_index += f"        <td align='middle'>2406:6400:99::99:<b>22</b>:<mark>{vnc_port}</mark></td>\n"
                    new_index += f"        <td align='middle'>10.99.99.<b>22</b>:<mark>{vnc_port}</mark></td>\n"
                    new_index += f"      </tr>\n"
                    vnc_port = vnc_port + 1
            new_index += f"    </table>\n"
        elif replace_flag and line.strip().startswith("</table>"):
            replace_flag = False
        elif not replace_flag:
            new_index += line + "\n"
    
    return new_index

def write_index_html():
    # # Interate and create config from default config and common config file
    # for i in range(1, num_group + 1):
    #     # Read ipv6-basic template file
    #     with open("templates/ipv6-basic.template", 'r') as read_index:
    #         create_index = read_index.read()
    #         # Update the router configuration
    #         for j in range (1, num_group + 1):
    #             updated_index = create_index_html(create_index)

    # # Write to main ipv6-basic.html file 
    # try:
    #     with open(f"/var/www/html/ipv6-basic.html", 'w') as write_index:
    #         write_index.seek(0)
    #         write_index.write(updated_index)
    # except:
    #     pass
    # read_index.close()

    # Create index.html file
    create_index = ""
    with open("templates/ipv6-basic.template", 'r') as read_index:
        create_index = read_index.read()

    updated_index = create_index_html(create_index)

    try:
        with open(f"/var/www/html/ipv6-basic.html", 'w') as write_index:
            write_index.seek(0)
            write_index.write(updated_index)
    except:
        pass

    read_index.close()


# Main Function #
def main():
    cookies1, cookies2 = eve_ng_login()
    existing_labs_1, existing_labs_2 = check_lab(cookies1, cookies2)
    PASS1, PASS2 = create_lab(cookies1, cookies2, existing_labs_1, existing_labs_2)
    if PASS1 == True and PASS2 == True:
        create_node(cookies1, cookies2)
        create_bridge_network(cookies1, cookies2)
        connect_ios_to_bridge(cookies1, cookies2)
        connect_slax_to_bridge(cookies1, cookies2)
        bridge_invisible(cookies1, cookies2)
        create_mgmt_network(cookies1, cookies2)
        connect_ios_to_mgmt(cookies1, cookies2)
        push_startup_config(cookies1, cookies2)
    elif PASS1 == False and PASS2 == True:
        print("Lab provision is not successfull in EVE-NG-1...(!)")
    elif PASS1 == True and PASS2 == False:
        print("Lab provision is not successfull in EVE-NG-2...(!)")
    else:
        print("Lab provision is not successfull in EVE-NG-1...(!)")
        print("")
        print("Lab provision is not successfull in EVE-NG-2...(!)")
    
    # create_index = create_index_html()
    # write_index_html(create_index)
    write_index_html()


# Call main() to execute the code
if __name__ == "__main__":
    main()

 
 


