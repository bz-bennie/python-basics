file_name = "file.txt"

try:
    file = open(file_name, 'r')
    data = file.read()
    file.close()
except NameError as name_error:
    print(name_error)
except FileNotFoundError as file_error:
    print(file_error)
except Exception as error:
    print(error)
else:
    print(data)
finally:
    print("The script is finished")