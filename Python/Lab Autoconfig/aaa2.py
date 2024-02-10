data = {'lab': {'@id': 'f24908d6-75bc-4aaa-9d9c-6f7b3d494620',
         '@lock': '0',
         '@name': 'Test',
         '@scripttimeout': '300',
         '@version': '1',
         'topology': {'networks': {'network': [{'@id': '1',
                                                '@left': '357',
                                                '@name': 'Net-R1-IOSiface_0',
                                                '@top': '269',
                                                '@type': 'bridge',
                                                '@visibility': '0'},
                                               {'@id': '2',
                                                '@left': '357',
                                                '@name': 'Net-R1-IOSiface_16',
                                                '@top': '269',
                                                '@type': 'bridge',
                                                '@visibility': '0'},
                                               {'@id': '3',
                                                '@left': '477',
                                                '@name': 'Net-R3-IOSiface_16',
                                                '@top': '442',
                                                '@type': 'bridge',
                                                '@visibility': '0'},
                                               {'@id': '4',
                                                '@left': '63',
                                                '@name': 'Net',
                                                '@top': '369',
                                                '@type': 'pnet1',
                                                '@visibility': '1'},
                                               {'@id': '5',
                                                '@left': '813',
                                                '@name': 'Net-R4-IOSiface_0',
                                                '@top': '433',
                                                '@type': 'bridge',
                                                '@visibility': '0'},
                                               {'@id': '6',
                                                '@left': '813',
                                                '@name': 'Net-R4-IOSiface_16',
                                                '@top': '433',
                                                '@type': 'bridge',
                                                '@visibility': '0'}]},
                      'nodes': {'node': [{'@config': '0',
                                          '@console': '',
                                          '@delay': '0',
                                          '@icon': 'Router.png',
                                          '@id': '1',
                                          '@idlepc': '0x62f21b30',
                                          '@image': 'c7200-adventerprisek9-mz.152-4.S7.image',
                                          '@left': '360',
                                          '@name': 'R1-IOS',
                                          '@nvram': '128',
                                          '@ram': '256',
                                          '@template': 'c7200',
                                          '@top': '195',
                                          '@type': 'dynamips',
                                          'interface': [{'@id': '0',
                                                         '@name': 'fa0/0',
                                                         '@network_id': '1',
                                                         '@type': 'ethernet'},
                                                        {'@id': '16',
                                                         '@name': 'fa1/0',
                                                         '@network_id': '2',
                                                         '@type': 'ethernet'},
                                                        {'@id': '96',
                                                         '@name': 'fa6/0',
                                                         '@network_id': '4',
                                                         '@type': 'ethernet'}],
                                          'slot': [{'@id': '1',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '2',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '3',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '4',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '5',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '6',
                                                    '@module': 'PA-FE-TX'}]},
                                         {'@config': '0',
                                          '@console': '',
                                          '@delay': '0',
                                          '@icon': 'Router.png',
                                          '@id': '2',
                                          '@idlepc': '0x62f21b30',
                                          '@image': 'c7200-adventerprisek9-mz.152-4.S7.image',
                                          '@left': '726',
                                          '@name': 'R2-IOS',
                                          '@nvram': '128',
                                          '@ram': '256',
                                          '@template': 'c7200',
                                          '@top': '204',
                                          '@type': 'dynamips',
                                          'interface': [{'@id': '0',
                                                         '@name': 'fa0/0',
                                                         '@network_id': '1',
                                                         '@type': 'ethernet'},
                                                        {'@id': '16',
                                                         '@name': 'fa1/0',
                                                         '@network_id': '3',
                                                         '@type': 'ethernet'},
                                                        {'@id': '32',
                                                         '@name': 'fa2/0',
                                                         '@network_id': '5',
                                                         '@type': 'ethernet'},
                                                        {'@id': '96',
                                                         '@name': 'fa6/0',
                                                         '@network_id': '4',
                                                         '@type': 'ethernet'}],
                                          'slot': [{'@id': '1',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '2',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '3',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '4',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '5',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '6',
                                                    '@module': 'PA-FE-TX'}]},
                                         {'@config': '0',
                                          '@console': '',
                                          '@delay': '0',
                                          '@icon': 'Router.png',
                                          '@id': '3',
                                          '@idlepc': '0x62f21b30',
                                          '@image': 'c7200-adventerprisek9-mz.152-4.S7.image',
                                          '@left': '531',
                                          '@name': 'R3-IOS',
                                          '@nvram': '128',
                                          '@ram': '256',
                                          '@template': 'c7200',
                                          '@top': '522',
                                          '@type': 'dynamips',
                                          'interface': [{'@id': '0',
                                                         '@name': 'fa0/0',
                                                         '@network_id': '2',
                                                         '@type': 'ethernet'},
                                                        {'@id': '16',
                                                         '@name': 'fa1/0',
                                                         '@network_id': '3',
                                                         '@type': 'ethernet'},
                                                        {'@id': '32',
                                                         '@name': 'fa2/0',
                                                         '@network_id': '6',
                                                         '@type': 'ethernet'},
                                                        {'@id': '96',
                                                         '@name': 'fa6/0',
                                                         '@network_id': '4',
                                                         '@type': 'ethernet'}],
                                          'slot': [{'@id': '1',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '2',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '3',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '4',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '5',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '6',
                                                    '@module': 'PA-FE-TX'}]},
                                         {'@config': '0',
                                          '@console': '',
                                          '@delay': '0',
                                          '@icon': 'Router.png',
                                          '@id': '4',
                                          '@idlepc': '0x62f21b30',
                                          '@image': 'c7200-adventerprisek9-mz.152-4.S7.image',
                                          '@left': '846',
                                          '@name': 'R4-IOS',
                                          '@nvram': '128',
                                          '@ram': '256',
                                          '@template': 'c7200',
                                          '@top': '375',
                                          '@type': 'dynamips',
                                          'interface': [{'@id': '0',
                                                         '@name': 'fa0/0',
                                                         '@network_id': '5',
                                                         '@type': 'ethernet'},
                                                        {'@id': '16',
                                                         '@name': 'fa1/0',
                                                         '@network_id': '6',
                                                         '@type': 'ethernet'},
                                                        {'@id': '96',
                                                         '@name': 'fa6/0',
                                                         '@network_id': '4',
                                                         '@type': 'ethernet'}],
                                          'slot': [{'@id': '1',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '2',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '3',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '4',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '5',
                                                    '@module': 'PA-FE-TX'},
                                                   {'@id': '6',
                                                    '@module': 'PA-FE-TX'}]}]}}}}



# Open a file to store output #
node_ip_config = open(f"node-ip-config.txt", "w")

# Define pair of nodes connected to same P2P link #
node_pair = []

# Find dict for nodes #
nodes = data["lab"]["topology"]["nodes"]["node"]

# Start to iterate nodes #
for item in range(0, len(nodes)):
    node = nodes[item]
    node_id = node["@id"]
    node_name = node["@name"]
    node_type = node["@type"]
    interfaces = node["interface"]

    # node_commands = ""
    # node_commands += "!\n"
    # node_commands += "conf t\n"

    if node_type == "dynamips":
        node_commands = "\n"
        node_commands += "!\n"
        node_commands += "conf t\n"

        # Start to iterate node > interface #
        for i in range (0, len(interfaces)):
            interface = interfaces[i]
            interface_name = interface["@name"]
            interface_net_id = interface["@network_id"]

            # Find dict for networks #
            networks = data["lab"]["topology"]["networks"]["network"]
            
            # Start to iterate networks #
            for item in range(0, len(networks)):
                network = networks[item]
                main_net_id = network["@id"]
                main_net_type = network["@type"]

                if main_net_id is interface_net_id and "pnet" not in main_net_type:
                    node_commands += f" interface {interface_name}\n"

                    next_nodes = data["lab"]["topology"]["nodes"]["node"]
                    # Start to iterate next nodes #
                    for item in range(0, len(next_nodes)):
                        next_node = next_nodes[item]
                        next_node_id = next_node["@id"]
                        next_node_name = next_node["@name"]
                        next_node_interfaces = next_node["interface"]
                        
                        # Self node id not eq to next node id #
                        if next_node_id is not node_id:                                    
                            for i in range (0, len(next_node_interfaces)):
                                next_node_interface = next_node_interfaces[i]        
                                next_node_net_id = next_node_interface["@network_id"]
                                if next_node_net_id is interface_net_id:
                                    node_pair1 = node_id + next_node_id ### 12
                                    node_pair2 = next_node_id + node_id  ### 21       
                                    if node_pair1 not in node_pair and node_pair2 not in node_pair:
                                        if int(node_pair1) < int(node_pair2):
                                            node_pair.append(node_pair1)
                                            node_commands += f"  ip address 10.0.{node_pair1}.1 255.255.255.252\n"
                                            node_commands += f"  description ** Connected to {next_node_name} **\n"           
                                        elif int(node_pair2) < int(node_pair1):
                                            node_pair.append(node_pair2)
                                            node_commands += f"  ip address 10.0.{node_pair2}.2 255.255.255.252\n"
                                            node_commands += f"  description ** Connected to {next_node_name} **\n"
                                    elif node_pair1 in node_pair or node_pair2 in node_pair:
                                        if int(node_pair1) < int(node_pair2):
                                            node_commands += f"  ip address 10.0.{node_pair1}.1 255.255.255.252\n"
                                            node_commands += f"  description ** Connected to {next_node_name} **\n"    
                                        elif node_pair2 < node_pair1:
                                            node_commands += f"  ip address 10.0.{node_pair2}.2 255.255.255.252\n"
                                            node_commands += f"  description ** Connected to {next_node_name} **\n"
                                            
                    node_commands += f"  no shutdown\n"
                    node_commands += f"!\n"

                elif main_net_id is interface_net_id and "pnet" in main_net_type:
                    node_commands += f" interface {interface_name}\n"
                    node_commands += f"  ip address 10.99.99.{node_id} 255.255.0.0\n"
                    node_commands += f"  description ** Connected to MGMT **\n"
                    node_commands += f"  no shutdown\n"
                    node_commands += f"!\n"

    else:
        node_commands = f"\n"
        node_commands += f"Node type for {node_name} is not supported by this script\n"
        node_commands += f"\n"

    node_ip_config.write(f"\n")
    node_ip_config.write(f"{node_name}\n")
    node_ip_config.write(f"======\n")
    node_ip_config.write(f"{node_commands}")

node_ip_config.close()




# # Find dict for nodes #
# nodes = data["lab"]["topology"]["nodes"]["node"]

# # Start to iterate nodes #
# for item in range(0, len(nodes)):
#     node = nodes[item]
#     node_id = node["@id"]
#     node_name = node["@name"]
#     node_type = node["@type"]

#     print(f"{node_name} is a {node_type} node")