#! usr/bin/python3
"""This scripts contains functions that
      can be used to generate passawards
      and OPTs forverification"""

import string
import random
def password_generator():
    uppercase = ''.join(random.choice(string.ascii_uppercase) for letter in range(2)) 
    lowercase = ''.join(random.choice(string.ascii_lowercase) for letter in range(2))
    number = ''.join(random.choice(string.digits) for letter in range(2))
    character = ''.join(random.choice(string.punctuation) for letter in range(2))
    password = uppercase + lowercase + str(number) + character
    print(password)

password_generator()




def verification_code(length):
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for  char in range(length))
    print(code)

try:
    length = int(input())
    verification_code(length)
except TypeError:
    print('sorry try again')
