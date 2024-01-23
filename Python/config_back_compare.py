from netmiko import Netmiko

import datetime
import difflib
import webbrowser

from netmiko.exceptions import NetmikoAuthenticationException
from netmiko.exceptions import NetmikoTimeoutException
from netmiko.exceptions import SSHException



lab_csr1 = {host = "192.168.1.1",
			username = "user",
			password = "password",
			device_type = "cisco_ios"}


lab_csr2 = {host = "192.168.1.2",
			username = "user",
			password = "password",
			device_type = "cisco_ios"}
			
my_router = Netmiko(**lab_csr)
						
print (my_router.find_promt())
print ("Successful")

show_run = my_router.send_command("show run")

now = datetime.datetime.now().replace(microseconds=0)
currunt_conf_file = f"{now}_{lab_csr[host]}.txt"

with open(currunt_conf_file, "w") as my_data:
	my_data.write(show_run)

ref = open("backup.txt)"
ref_content = ref.readlines()
rf.colse()

new = open("backup.txt)"
new = ref.readlines()
new.colse()


conf_compare = difflib.HtmlDiff().make_file(fromlines=ref_content,
                                            tolines = new_content,
                                            fromdesc="Backup Ref", todesc=fCurrent {currunt_conf_file}
                                            
with open ("diff.html", "w") as new_diff:
    new_diff.write(conf_compare)
    
webbrowser.open_new_tab("diff.html")


except NetmikoAuthenticationException:
    print (" ")




