import jinja2
import jinja2
from jinja2 import Environment, FileSystemLoader
import os
import json


template_dir = "C:\\mnasergit-repo\\mnasergit-repo\\Python\\Random Practices\\New folder"
template_file = "ios-xe_template.j2"

output_directory = "C:\\mnasergit-repo\\mnasergit-repo\\Python\\Random Practices\\New folder\\configs"
# create the central Jinja2 environment and load template
# env = jinja2.Environment(
#     loader=jinja2.FileSystemLoader(searchpath="."), trim_blocks=True, lstrip_blocks=True
# )
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template(template_file)

# check for configs directory if not present create
# if not os.path.exists(output_directory):
#     os.mkdir(output_directory)

# create the config templates
with open("config.json", "r") as parameters:
    data = json.load(parameters)
    for p in data:
        result = template.render(p)
        f = open(os.path.join(output_directory, p["hostname"] + ".txt"), "w")
        f.write(result)
        f.close()
        parameters.close()

#print ("Current Working Directory:", os.getcwd())