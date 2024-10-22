import requests

ip_address = requests.get('https://api.ipify.org').text

print(ip_address)

#geo_lo = requests.get(f'https://ip-api.com/{ip_address}').text

#print(geo_lo)