from netmiko import Netmiko, redispatch ssh_exception
import time


linux_jump_host_ip = "192.168.1.2"
linux_jump_host_user = "user"
linux_jump_host_password = "password"

router_ip = "10.99.1.1"
router_user = "admin"
router_password = "admin"

try:
    net_connect = Netmiko(device_type="linux_ssh",
                           host=linux_jump_host_ip,
                           username=linux_jump_host_user,
                           password=linux_jump_host_password
                           )
                           
    print("Connecting to the jump host...")
    print(net_connect.find_promt()
    print("Connected to the jump host.")


    print("\n")
    print("Connecting to the destination device...")

    net_connect.write_channel(f"ssh {router_user}@{router_ip}")
    time.sleep(2)

    #output = net_connect.find_promt()
    output = net_connect.read_channel()

    print ("output")

    if "Password" in output:
        print("Received password promt")
        net_connect.write_channel(f"{router_password}\n"
        time.sleep(2)
        print ("\nDestination Device Prompt")
        print(net_connect.find_promt())
        

    cmds = ["show ip int brief", "show ip route", "show users"]

    redispatch(net_connect,device_type="cisco_ios")
    for cmd in cmds:
        print(f"\nExecuting the command: {cmd}")
        router_output = net_connect.send_command(cmd)
        print(router_output)
        
    else:
        print ("Unable to connect to destination router")
    
    
except ssh_exception.NetmikoTimeoutException:
    print ("Jump host not reachable")
except ssh_exception.NetmikoAuthenticationException:
    print ("Jump authenticatio failed.")
    
    
    
    





