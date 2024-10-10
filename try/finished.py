name = input('Your Name: ')

try:
    print(f' Hello {name}')
except:
    print("There seems to be an error")
finally:
    print("The script has finished")