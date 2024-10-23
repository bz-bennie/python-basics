'''popen ping with os'''

import os

host = input("Host / IP address to ping: ")
command = (f' ping  {host}')
response = os.popen(command).read()

print(response)