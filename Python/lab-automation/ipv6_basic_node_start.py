import requests
from pprint import pprint
import time
import sqlite3
from lab_variable import EVE_1, EVE_2, EVE_USER, EVE_PASSWORD, num_group_eve_1

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

# Start Lab Node ##
def start_node(cookies1, cookies2):
    # 1. Check node status and start node in EVE1 #
    node_status_url_1 = f"http://{EVE_1}/api/labs/IPv6-Basic-Connectivity-Lab.unl/nodes"
    node_status_api_1 = requests.get(url=node_status_url_1,cookies=cookies1,headers=headers)

    node_status_api_response_1 = node_status_api_1.json()
    #pprint (node_status_api_response)

    node_status_dict_1 = node_status_api_response_1['data']
    #num_nodes = len(node_status_dict_1)

    print("")
    
    # Start nodes that are not running in EVE1 #
    if node_status_api_1:
        try:
            j = 0
            for i in range (1, num_group_eve_1 * 2 + 1):
                device_status = node_status_dict_1[f"{i}"]["status"]
                if device_status == 2:
                    j = j + 1
                elif device_status != 2 and device_status != 0:
                    j = j + 1
                elif device_status == 0:
                    node_start_url_1 = f"http://{EVE_1}/api/labs/IPv6-Basic-Connectivity-Lab.unl/nodes/{i}/start"
                    node_start_api_1 = requests.get(url=node_start_url_1,cookies=cookies1,headers=headers)
                    j = j + 1
                    time.sleep(3)
                    
                else:
                    pass

            if j == int(num_group_eve_1 * 2):
                print (f"Nodes started in EVE-NG-1.")
            elif j == 0:
                print (f"No node found to be started in EVE-NG-1.")
            else:
                pass

            print ("")

        except:
            print("No node couldn't be started in EVE-NG-1.")
    
    # 2. Check node status and start node in EVE2 #
    node_status_url_2 = f"http://{EVE_2}/api/labs/IPv6-Basic-Connectivity-Lab.unl/nodes"
    node_status_api_2 = requests.get(url=node_status_url_2,cookies=cookies2,headers=headers)

    node_status_api_response_2 = node_status_api_2.json()
    #pprint (node_status_api_response)

    node_status_dict_2 = node_status_api_response_2['data']
    #num_nodes = len(node_status_dict_2)

    # Start nodes that are not running in EVE2 #
    if node_status_api_2:
        try:
            j = 0
            for i in range (1, num_group_eve_2 * 2 + 1):
                device_status = node_status_dict_2[f"{i}"]["status"]
                if device_status == 2:
                    j = j + 1
                elif device_status != 2 and device_status != 0:
                    j = j + 1
                elif device_status == 0:
                    node_start_url_2 = f"http://{EVE_2}/api/labs/IPv6-Basic-Connectivity-Lab.unl/nodes/{i}/start"
                    node_start_api_2 = requests.get(url=node_start_url_2,cookies=cookies2,headers=headers)
                    j = j + 1
                    time.sleep(3)
                    
                else:
                    pass

            if j == int(num_group_eve_2 * 2):
                print(f"Nodes started in EVE-NG-2.")
            elif j == 0:
                print(f"No node found to be started in EVE-NG-2.")
            else:
                pass

        except:
            print("No node couldn't be started in EVE-NG-2.")

# Main Function #
def main():
    cookies1, cookies2 = eve_ng_login()
    start_node(cookies1, cookies2)


# Call main() to execute the code
if __name__ == "__main__":
    main()