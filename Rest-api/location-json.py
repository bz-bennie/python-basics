'''geo location with ip-api'''

import requests

ip_address = requests.get('https://api.ipify.org').text

location = requests.get(f'http://ip-api.com/json/{ip_address}').json()

print(ip_address)

print(location)

print(f'City: {location["city"]} -- State: {location["regionName"]}')