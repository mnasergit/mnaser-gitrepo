"""
Description:    Simple IOS-XE configuration Generator. Run program and browse to 127.0.0.1:5000
"""

import jinja2
from jinja2 import Environment, FileSystemLoader
import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
app = Flask(__name__)

@app.route("/")
def webroot():
    return render_template("index.html")


@app.route("/success", methods = ["GET"])
#@app.route("/", methods = ["GET"])
def success():
    return render_template("success.html")

#@app.route("/config", methods = ["POST"])
@app.route("/config", methods = ["POST"])
def config():
    hostname = request.form["hostname"]
 
    data = [{
            "hostname": hostname
            }]
            
            
    template_dir = "C:\\mnasergit-repo\\mnasergit-repo\\Python\\Random Practices\\New folder"
    template_file = "ios-xe_template.j2"
    output_directory = "configs"
    output_directory = "C:\\mnasergit-repo\\mnasergit-repo\\Python\\Random Practices\\New folder\\configs"
    # create the central Jinja2 environment and load template
    #env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."),
    #                         trim_blocks=True,
    #                         lstrip_blocks=True)
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_file)

    

    # check for configs directory if not present create
    # if not os.path.exists(output_directory):
    #     os.mkdir(output_directory)

    # create the config templates
    for p in data:
        result = template.render(p)
        f = open(os.path.join(output_directory, p['hostname'] + ".txt"), "w")
        f.write(result)
        f.close()
    return redirect(url_for("success"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)


