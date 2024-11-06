'''this is a random password gen, copied from github.'''


numbers = '0123456789'
chars = 'abcdefghijklmnopqrstuvwxyz'
up = chars.upper()
special = '_!#$%()'

all = numbers+chars+up+special

from random import choice

password = ''.join(choice(all) for i in range(8))

print(password)