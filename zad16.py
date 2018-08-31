'''Write a password generator in Python. 
Be creative with how you generate passwords - 
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.

Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.'''

import string
import random
import time

def get_password(m='s'):
    if m == 'w':
        words = 'Ask the user how strong they want their password to be'.split()
        password = ''.join([random.choice(words) for i in range(random.randint(1, 2))])
        print(password)
    elif m == 's':
        signs = [random.choice(string.ascii_lowercase) for i in range(random.randint(5, 10))]
        signs += [random.choice(string.ascii_uppercase) for i in range(random.randint(5, 10))]
        signs += [random.choice(string.digits) for i in range(random.randint(3, 7))]
        signs += [random.choice(string.punctuation) for i in range(random.randint(3, 7))]
        random.shuffle(signs)
        password = ''.join(signs)
        print(password)

def main():
    strong = input('Do you want to get a weak or strong password? (w/s): ')
    start_time = time.clock()
    get_password(strong)
    end_time = time.clock()
    print('--- %.8f seconds ---' % (end_time - start_time))

main()