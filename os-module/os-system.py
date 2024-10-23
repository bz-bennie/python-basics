'''create file with os module'''

import os 

command = 'type nul > os-test.txt'

os.system(command)

result = os.system(command)

print(result)

# 0 is a pass, 32512 example of fail resault 