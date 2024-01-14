Startup Config Maker
====================
Prepare customized startup-config files for lab routers

Introduction
------------
The "Startup Config Maker" is a Python script designed to automate the generation of router configurations for multiple devices based on input data from an Excel spreadsheet. It reads information such as hostname, IPv4 and IPv6 addresses from the "Device-Info.xlsx" spreadsheet and applies these details to template configurations stored in "default_config.txt" and "common_config.txt" files. The updated configurations are then written to individual files for each router.

Prerequisites
-------------
Ensure the following dependencies are installed:
● openpyxl
● ipaddress

Install dependencies using the following command:
> pip install openpyxl ipaddress

Usage
-----
1. Excel Spreadsheet Format:
The script expects an Excel spreadsheet named "Device-Info.xlsx" with the following structure in the "Sheet1" worksheet:

Hostname	...	IPv6_FA60		IPv4_FA60	...
-------------------------------------------------------------------
G1-R1		...	2406:6400:99::1:1/64	10.99.1.1/16	...
G2-R1		...	2406:6400:99::2:1/64	10.99.2.1/16	...
G3-R1		...	2406:6400:99::3:1/64	10.99.3.1/16	...
...		...	...			...		...
...		...	...			...		...
...		...	...			...		...

2. Router Configuration Templates:

The script utilizes two template files:

● default_config.txt: Contains the default router configuration.
● common_config.txt: Contains common configuration elements shared by all routers.

3. Run the Script:

Execute the script using the following command:
> python3 script.py

The script iterates through each row in the spreadsheet, updates the router configuration based on the provided information, and generates individual configuration files for each router.

4. Output Files:

Individual configuration files for each router will be created in the same directory as the script. The filenames will follow the format "{hostname}.txt".

Functionality
-------------
1. update_router_config(config_text)

This function takes the default router configuration as input and updates specific sections based on the information from the Excel spreadsheet. The updated configuration is then returned.

2. Iterating through Excel Spreadsheet

The script iterates through each row of the "Sheet1" worksheet in the "Device-Info.xlsx" Excel file. For each router, it reads the hostname, IPv6 address (IPv6_FA60), and IPv4 address (IPv4_FA60) from the spreadsheet.

3. Reading Template Configurations

The default router configuration is read from "default_config.txt," and the common configuration is read from "common_config.txt."

4. Writing Updated Configurations

The script writes the updated router configuration and the common configuration to individual files for each router. The filenames are generated based on the hostname.

Error Handling
--------------
In case of a ValueError, the script prints an error message indicating an invalid input detected in the Excel file and closes the workbook.

Closing Resources
-----------------
The script ensures proper closure of opened resources, including the workbook and file handles.


Feel free to customize this documentation based on additional details or specifics relevant to your project.