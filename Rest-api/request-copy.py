import requests

page = requests.get('https://krebsonsecurity.com/').text

print(page)

with open("krbs-copy.html", 'w') as file:
    file.write(page)