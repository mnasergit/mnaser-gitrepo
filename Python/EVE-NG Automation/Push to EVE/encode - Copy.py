'''
import re
import hashlib

def hash_config(config):
    # Use MD5 hash to encrypt the password
    #hash_object = hashlib.md5(config.encode())
    #return hash_object.hexdigest()
    hashed_object = hash(config)
    return str(hashed_object)
'''
def process_config(config):
    # Find lines containing "secret" and encrypt the password
    encrypted_config = ""
    for line in config.split('\n'):
        match = re.search(r'\s+secret (\d+) (.+)', line)
        if match:
            encrypted_password = encrypt_password(match.group(2))
            line = f' secret {match.group(1)} {encrypted_password}'

        encrypted_config += line + '\n'

    return encrypted_config
'''

with open("Group1-Router1-startup-config.txt", 'r') as plain_cfg:
    plain_config = plain_cfg.read()

# Process the configuration and print the result
    #encrypted_config = process_config(example_config)
hashed_config = hash_config(plain_config)
print(hashed_config)

with open("Hashed_File.txt", 'w') as hashed_cfg:
    hashed_cfg.seek(0)
    hashed_cfg.write(hashed_config)


plain_cfg.close()
hashed_cfg.close()
'''



import base64

# Read the contents of the text file
with open('Group1-Router1-startup-config.txt', 'rb') as file:
    text_contents = file.read()

# Encode the contents using base64
encoded_contents = base64.b64encode(text_contents)

# Write the encoded contents to a new file
with open('Hashed_File.txt', 'wb') as encoded_file:
    encoded_file.write(encoded_contents)
