import requests
from pprint import pprint
from datetime import datetime
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
if num_group > num_group_eve_1:
    num_group_eve_2 = num_group - num_group_eve_1
else:
    num_group_eve_1 = num_group
    num_group_eve_2 = 0
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
    
    except:
        print("Login into EVE-NG-1 is not successful.")


    ### Login into EVE2 ###
    if num_group_eve_2 > 0:
        try:
            login_url = f"http://{EVE_2}/api/auth/login"
            cred = '{{"username":"{}","password":"{}","html5":"-1"}}'.format(EVE_USER, EVE_PASSWORD)

            login_api = requests.post(url=login_url, data=cred, headers=headers)
            cookies2 = login_api.cookies
        
        except:
            print("Login into EVE-NG-2 is not successful.")

    return cookies1, cookies2

def check_node_status(cookies1, cookies2):

    # Check Status of Node in EVE1 #
    if cookies1 is not None:
        node_status_url_1 = f"http://{EVE_1}/api/labs/IPv6-Basic-Connectivity-Lab.unl/nodes"
        node_status_api_1 = requests.get(url=node_status_url_1,cookies=cookies1,headers=headers)
        node_status_api_response_1 = node_status_api_1.json()
        node_status_dict_1 = node_status_api_response_1['data']
        ### num_nodes = len(node_status_dict)

    # Check Status of Node in EVE2 #
    if cookies2 is not None:
        node_status_url_2 = f"http://{EVE_2}/api/labs/IPv6-Basic-Connectivity-Lab.unl/nodes"
        node_status_api_2 = requests.get(url=node_status_url_2,cookies=cookies2,headers=headers)
        node_status_api_response_2 = node_status_api_2.json()
        node_status_dict_2 = node_status_api_response_2['data']

    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    print()
    print(f"Node status: (last updated on {formatted_time})")
    print()

    try:
        if node_status_api_1:
            for i in range (1, num_ios_eve_1 + 1):
                device_status = node_status_dict_1[f"{i}"]["status"]
                if device_status == 2:
                    print (f"Group{i}-Router1 is is running....")
                elif device_status == 0:
                    print (f"Group{i}-Router1 is stopped.")
                else:
                    pass
    except:
        pass

    try:
        if node_status_api_2:
            j = 1
            for i in range (num_ios_eve_1 + 1, num_ios + 1):
                device_status = node_status_dict_2[f"{j}"]["status"]
                if device_status == 2:
                    print (f"Group{i}-Router1 is is running....")
                elif device_status == 0:
                    print (f"Group{i}-Router1 is stopped.")
                else:
                    pass
                j = j + 1
            print(" ")
    except:
        pass

    try:
        if node_status_api_1:
            j = 1
            for i in range (num_ios_eve_1 + 1, num_ios_eve_1 + num_slax_eve_1 + 1 ):
                device_status = node_status_dict_1[f"{i}"]["status"]

                if device_status == 2:
                    print (f"Group{j}-Host1 is is running....")
                elif device_status == 0:
                    print (f"Group{j}-Host1 is stopped.")
                else:
                    pass
                j = j + 1
    except:
        pass

    try:
        if node_status_api_2:
            for i in range (num_ios_eve_2 + 1, num_ios_eve_2 + num_slax_eve_2 + 1 ):
                device_status = node_status_dict_2[f"{i}"]["status"]

                if device_status == 2:
                    print (f"Group{j}-Host1 is is running....")
                elif device_status == 0:
                    print (f"Group{j}-Host1 is stopped.")
                else:
                    pass
                j = j + 1
    except:
        pass

# Main Function #
def main():
    cookies1, cookies2 = eve_ng_login()
    check_node_status(cookies1, cookies2)

# Call main() to execute the code
if __name__ == "__main__":
    main()