name = input('Your Name: ')

try:
    print(f' Hello {name}')
except:
    print("There seems to be an error")
else:
    print("Im happy to meet you")
finally:
    print("The script has finished")