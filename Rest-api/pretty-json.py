'''Api call and pritify json'''
#.dumps turns json into string 

import requests
import json

ip_address = requests.get('https://api.ipify.org').text
location = requests.get(f'http://ip-api.com/json/{ip_address}').json()

#print(ip_address)
print(location)

location_pretty = json.dumps(location, indent=5)

print(location_pretty)


