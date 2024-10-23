import os 
import time

sites = input(f'Host / IP address for network test: ')

sites = sites.split(' ')

print(sites)

while True:
    #os.system('cls')
    for address in sites:
        try:
            command = (f'ping {address}')
            response = os.popen(command).read()

            if 'Received = 4' in response:
                print(f'{address} is up')
            else:
                 print(f'{address} is down')
        except:
            print(f'{address} COMMAND FAIL')
            