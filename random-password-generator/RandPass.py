#! python
# Random password genirator save to file 
import random
import string
import os
# change location of platform input.
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for i in range(length))

def save_password(platform, user, password, filename="passwords.txt"):
    with open(filename, "a") as file:
        file.write(f"{platform}: {user}: {password}\n")
    print(f"Password saved for {user}.")

def main():
    platform = input("Platform Name: ")
    user = input("User Name: ")
    password = generate_password()
    print(f"Generated Password: {password}")
    save_password(platform, user, password)

if __name__ == "__main__":
    main()


