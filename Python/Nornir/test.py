# pip install nornir
# pip install nornir-utils
# pip install nornir-napalm
# pip install nornir-netmiko
# pip install --upgrade nornir nornir_utils napalm

from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_command
import json
import pprint

nr = InitNornir(
    config_file="hosts.yaml", dry_run=True
)

print(nr.inventory.hosts)

results = nr.run(
    task=napalm_get, getters=["facts", "interfaces", "interfaces_ip"]
    #task=napalm_get, getters=["config"]
)

# Define the command to execute
commands = ["show ip interface brief", "show users"]
results_mul = {}
# Run the task to send the command
# Run the task to send the command for each host
for command in commands:
    for host, host_data in nr.inventory.hosts.items():
        platform = host_data.get("platform")  # Get the platform information
        if platform and platform.lower() == "ios":  # Check if platform is iOS
            result = nr.run(
                task=netmiko_send_command,
                command_string=command,
                on_failed=True
            )
            if host not in results_mul:
                results_mul[host] = {}
            results_mul[host][command] = result



# Convert each individual result to a dictionary
#results_dict = {host: result[0].result for host, result in results.items()}

### If it is required to see the file ###
# Convert OrderedDict to JSON string
#result_json = json.dumps(results_dict)

# # Convert JSON string to pprint format
# result_json = json.loads(result_json)
# result_json = pprint.pformat(result_json)

# with open(f"results_dict.json", "w") as result_file:
#     result_file.write(result_json)


# a = results_dict["rtr1"]["interfaces_ip"]
# b = results_dict["rtr2"]["interfaces_ip"]
# pprint.pprint(a)
# pprint.pprint(b)
    
# for router_name, router_data in results_dict.items():
#     print(router_name)
#     print("#" * len(router_name))
#     for interface_name, interface_data in router_data['interfaces'].items():
#         print(f"Interface: {interface_name}")
#         print(f"Details: {interface_data}")
#         print("\n")

# for router_name, router_data in results_dict.items():
#     print(router_name)
#     print("=" * len(router_name))
#     hostname = router_data['facts']['hostname']
#     mgmt_ip_data = router_data['interfaces_ip']['FastEthernet6/0']['ipv4']
#     mgmt_ip = list(mgmt_ip_data.keys())[0]
#     mgmt_mask_data = list(mgmt_ip_data.values())[0]
#     mgmt_mask = list(mgmt_mask_data.values())[0]
#     # facts = router_data.get('facts', {})  # Access the 'facts' dictionary, or an empty dictionary if it doesn't exist
#     # hostname = facts.get('hostname', '')  # Access the 'hostname' key from the 'facts' dictionary, or an empty string if it doesn't exist
#     # mgmt_ip_dict = router_data['interfaces_ip'].get('FastEthernet6/0', {}).get('ipv4', {})  # Access the IPv4 dictionary, or an empty dictionary if it doesn't exist
#     # mgmt_ip = next(iter(mgmt_ip_dict), '')  # Get the first key in the IPv4 dictionary, or an empty string if the dictionary is empty
#     print(f"Router Name: {router_name}")
#     print(f"Hostname: {hostname}")
#     print(f"MGMT IP: {mgmt_ip}")
#     print(f"Mask: {mgmt_mask}")
#     ip_mask = mgmt_ip + "/" + str(mgmt_mask)
#     print(f"IP and Mask: {ip_mask}")
#     print("")


''''
from datetime import timedelta

def format_uptime(seconds):
    uptime_timedelta = timedelta(seconds=seconds)
    return str(uptime_timedelta)

uptime_seconds = 3180.0
uptime_formatted = format_uptime(uptime_seconds)
print(uptime_formatted)
'''

# # Print the running configuration for each device
# for host, result in results.items():
#     running_config = result.result.get("config", {}).get("running", "")
#     print(f"Running configuration for {host}:")
#     print(running_config)
#     print("-" * 50)



# Iterate over the results dictionary and print the output for each command
for host, command_data in results_mul.items():
    print(f"\nHost: {host}")
    for command, result in command_data.items():
        print(f"\nOutput of command '{command}':")
        print(result[host].result)


