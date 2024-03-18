import requests
import json

# Define EVE-NG server information
eve_ng_host = '192.168.30.12'
eve_ng_username = 'admin'
eve_ng_password = 'AD@eve24'
lab_id = "1794e4bf-1613-42e4-ba37-c45a3678992e"

# Authenticate with EVE-NG API
auth_response = requests.post(f'http://{eve_ng_host}/api/auth/login', json={"username": eve_ng_username, "password": eve_ng_password})
auth_token = auth_response.json()['data']['token']

# Get information about devices in EVE-NG
devices_response = requests.get(f'http://{eve_ng_host}/api/labs/{lab_id}/nodes', headers={'Authorization': f'Bearer {auth_token}'})
devices = devices_response.json()['data']

# Identify the Cisco router node
cisco_router = next(device for device in devices if device['name'] == 'R1')

# Access router console/CLI
console_response = requests.post(f'http://{eve_ng_host}/api/labs/{lab_id}/nodes/{cisco_router["id"]}/console', headers={'Authorization': f'Bearer {auth_token}'})

# Send command to retrieve idle PC value
command = 'show processes cpu | include Idle'
command_response = requests.post(f'http://{eve_ng_host}/api/labs/{lab_id}/nodes/{cisco_router["id"]}/console', headers={'Authorization': f'Bearer {auth_token}'}, json={"input": command})

# Parse output to extract idle PC value
output = command_response.json()['output']
idle_pc_value = output.split()[5]

print(f"Idle PC value: {idle_pc_value}")
