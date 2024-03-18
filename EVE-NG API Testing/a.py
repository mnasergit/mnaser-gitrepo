import json

# Define the path to your plain text file
text_file_path = 'a.txt'
json_data = {"id": "1", "data": ""}

# Read the plain text file and convert it to JSON
with open(text_file_path, 'r') as file:
    json_data["data"] = file.read()

# Convert the Python dictionary to a JSON string
json_string = json.dumps(json_data, indent=2)

# Save the JSON string to a new file
with open('output.json', 'w') as json_file:
    json_file.write(json_string)

print("Conversion complete. JSON file saved as 'output.json'.")






# file = open("a.txt", "r")
# text = file.readlines()
# lines = text.strip().split("\n")

# json_data = {}

# for line in lines:
#     key, value = line.strip().split(' ', 1)
#     json_data[key.strip()] = value.strip()

# json_string = json.dumps(json_data, indent=2)

# # Save the JSON string to a new file
# with open('output.json', 'w') as json_file:
#     json_file.write(json_string)

# file.close()
# json_file.close()

# print("Conversion complete. JSON file saved as 'output.json'.")    


# '''

# # with open("a.txt", 'r') as file:
# #     for line in file:
# #         key, value = line.strip().split(':', 1)
# #         json_data[key.strip()] = value.strip()

# # json_string = json.dumps(json_data, indent=2)

# # with open('output.json', 'w') as json_file:
# #     json_file.write(json_string)

# # print("Conversion complete. JSON file saved as 'output.json'.")


# # Split the text into lines
# lines = text.strip().split('\n')

# # Create a dictionary from the lines
# json_data = {}
# for line in lines:
#     key, value = line.strip().split(' ', 1)
#     json_data[key.strip()] = value.strip()

# # Convert the Python dictionary to a JSON string
# json_string = json.dumps(json_data, indent=2)

# # Save the JSON string to a new file
# with open('output.json', 'w') as json_file:
#     json_file.write(json_string)

# print("Conversion complete. JSON file saved as 'output.json'.")

# '''