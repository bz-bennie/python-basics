#example of bad function from flow control and bad var

def bad_function():
    global bad_var
    bad_var = 'bob'
    print(message)

message = "words are cool"

bad_function()

print(bad_var)

