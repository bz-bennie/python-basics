'''create file in working dir, write and read with os.path'''

import os 

directory = os.path.dirname(os.path.abspath(__file__))

print(directory)

file_name = 'os-test.txt'

file_path = os.path.join(directory, file_name)

with open(file_path, 'w') as file:
    file.write("The OS Module is so cool")

with open(file_path, 'r') as file:
    message =file.read()

print(message)
