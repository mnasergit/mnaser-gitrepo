from jinja2 import Environment, FileSystemLoader
import os
import sqlite3

downoad_link = "<a href='static/Config_Output.txt' download>Download Configuration File</a>"

data = []

# Connect to the same SQLite database
conn = sqlite3.connect('config_data.db')
cursor = conn.cursor()

# Retrieve the value from the table
cursor.execute("SELECT * FROM table_config_data")

# Fetch all rows returned by the query
rows = cursor.fetchall()

# Iterate over the rows and print each row
for row in rows:
    value = row[1]
    data.append(value)

template_dir = "C:\\mnasergit-repo\\mnasergit-repo\\Python\\ixp-peering"
template_file = "template_cisco_ios.j2"

output_directory = "C:\\mnasergit-repo\\mnasergit-repo\\Python\\ixp-peering\\static"
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template(template_file)

# create the config templates
try:
    result = template.render(own_asn=data[0], 
                             neighbor_asn=data[1],
                             bgp_neighbor=data[2]
                             )
    f = open(os.path.join(output_directory, "Config_Output.txt"), "w")
    f.write(result)
    f.close()
    print("The configuration has been generated successfully.")
    print (f"Click to download {downoad_link}")
except Exception as e:
    print("Error rendering template:", e)


