import requests
import json 

ip_address = requests.get('https://api.ipify.org').text

location =requests.get(f'http://ip-api.com/json/{ip_address}').json()

#print(ip_address)
#print(location)

lattitude = location['lat']
longitude = location['lon']

#print(lattitude)
#print(longitude)

'''used for percise location'''
#weather = requests.get(f'https://api.weather.gov/points/{lattitude},{longitude}').json()

state = location['region']

#print(city)
'''used for state'''
weather = requests.get(f'https://api.weather.gov/alerts/active?area=FL').json()

#print(weather)

weather_pretty = json.dumps(weather, indent = 3)

#print(weather_pretty)

#print(weather['features'][0]['properties']['headline'])
#print(weather['features'][0]['properties']['description'])

try:
    print("WEATHER")

    for x in weather["features"]:
        print('\n ---- >>>WARNING<<< ----')
        print(x['properties']['headline'])
        print(x['properties']['description'])

except:
    print("No Alerts")