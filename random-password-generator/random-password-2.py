'''Genarate a random password, 
2nd attempt'''

import random

# character sets
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

Number = ['1','2','3','4','5','6','7','8','9','0',]

special_character = ['!','@','#','$','%','^','&','(',')',':',';','?','/',]

letter_count = 4
number_count = 3
special_count = 2
random_password =""


while letter_count >= 0:
        password = random.choice(letter)
        print(password)
    
        password = random.choice(Number)
        print(password)
       
        password = random.choice(special_character)
        print(password)
        letter_count += -1
