'''list of some basic commands that work on most OS's'''

import os 

#os.mkdir('test-dir')

#os.rename('test-dir', 'production-dir')

#os.rmdir('production-dir')

result = os.scandir()

for x in result:
    print(x)


