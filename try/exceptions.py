name = input("Your name: ")

try:
    print(f'Hello {name}')
except Exception as error:
    print(error)
else:
    print('Im happy to meet you')
finally:
    print("The script is finished")