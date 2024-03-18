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



# print(type(data))
# print(len(data))

'''

nodes = data["lab"]["topology"]["nodes"]["node"]
# print(f"Type of nodes: {type(nodes)}")
# print(f"Length of nodes: {len(nodes)}")
# print(f"Nodes: {nodes}")
# print("#"*100)
# print("")

for item in range(0, len(nodes)):
    node = nodes[item]
    # print(f"Type of node: {type(node)}")
    # print(f"Length of node: {len(node)}")
    # print(f"node: {node}")
    # print("#"*100)
    # print("")
    value = node["@name"]
    #print(len(value))
    print(f"Router Name: {value}")

networks = data["lab"]["topology"]["networks"]["network"]
# print(f"Type of networks: {type(networks)}")
# print(f"Length of networks: {len(networks)}")
# print(f"Nodes: {networks}")
# print("#"*100)
# print("")
    
for item in range(0, len(networks)):
    network = networks[item]
    # print(f"Type of network: {type(network)}")
    # print(f"Length of network: {len(network)}")
    # print(f"network: {network}")
    # print("#"*100)
    # print("")
    type = network["@type"]
    value1 = network["@name"]
    value2 = network["@id"]
    #print(len(value))
    if "pnet" not in type:
        print(f"Network Name: {value1} and Network Id: {value2}")


nodes = data["lab"]["topology"]["nodes"]["node"]
for item in range(0, len(nodes)):
    node = nodes[item]
    node_name = node["@name"]
    # print(f"Type of node: {type(node)}")
    # print(f"Length of node: {len(node)}")
    # print(f"node: {node}")
    # print("#"*100)
    # print("")
    print(f"Node Name: {node_name}")
    interfaces = node["interface"]
    for i in range (0, len(interfaces)):
        interface = interfaces[i]
        value1 = interface["@name"]
        value2 = interface["@network_id"]
        print(f"Interface {value1} belongs to Network Id {value2}")

'''

networks = data["lab"]["topology"]["networks"]["network"]

for item in range(0, len(networks)):
    network = networks[item]
    net_id_main = network["@id"]
    net_type = network["@type"]
    nodes = data["lab"]["topology"]["nodes"]["node"]
    net_id_list = []
    pnet_id_list = []
    if "pnet" not in net_type:
        for item in range(0, len(nodes)):
            node = nodes[item]
            node_id = node["@id"]
            node_name = node["@name"]
            interfaces = node["interface"]
            for i in range (0, len(interfaces)):
                interface = interfaces[i]        
                net_id = interface["@network_id"]
                if net_id is net_id_main:
                    net_id_list.append(node_id)
        
        print(f"Network Id {net_id_main} is connecting {net_id_list[0]} and {net_id_list[1]}")

    elif "pnet" in net_type:
        for item in range(0, len(nodes)):
            node = nodes[item]
            node_name = node["@name"]
            interfaces = node["interface"]
            for i in range (0, len(interfaces)):
                interface = interfaces[i]        
                net_id = interface["@network_id"]
                if net_id is net_id_main:
                    pnet_id_list.append(node_name)
        
        print(f"Network Id {net_id_main} is connecting", end=' ')
        for item in pnet_id_list:
            if pnet_id_list.index(item) == (len(pnet_id_list)) - 1:
                print(f"and {item}")
            elif pnet_id_list.index(item) == (len(pnet_id_list)) - 2:
                print(f"{item}", end=' ')
            else:
                print(f"{item},", end=' ')

    else:
        print("No match found for this code!")


list1 = ["12", "21"]
a = "12"
b = "21"

if a in list1 or b in list1:
    print ("matches")
else:
    print ("Doesn't match")


# a = [1, 2, 3, 4, 5]

# # Iterate over the list and print each value on the same line
# for item in a:
#     print(item, end=' ')

# a = [1, 2, 3, 4, 5]

# # Iterate over the list and print each value on the same line
# for i, item in enumerate(a):
#     if i == len(a) - 1:
#         print(item)  # Print the last item with a newline
#     else:
#         print(item, end=' ')  # Print other items with a space as separator

# a = [1, 2, 3, 4, 5]

# # Find the position of item 3 in the list
# position = a.index(3)
# print("Position of item 3:", position)






# for i in range (1, n):
#     a = data[f"{i}"]["@id"]
#     print(a)
