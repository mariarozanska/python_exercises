'''Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. 
Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place, they have a “cow”. 
For every digit the user guessed correctly in the wrong place is a “bull.” 
Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
Once the user guesses the correct number, the game is over. 
Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:
  Welcome to the Cows and Bulls Game! 
  Enter a number: 
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...
Until the user guesses the number.'''

import random

def cows_bulls(guess, number):
    cows = 0
    bulls = 0
    guess_copy = list(guess)
    number_copy = list(number)
    for i in range(len(number)):
        if number[i] == guess[i]:
            # del number_copy[i - cows]
            # del guess_copy[i - cows]
            cows += 1
            number_copy.remove(number[i])
            guess_copy.remove(number[i])
    for d in guess_copy:
        if d in number_copy:
            bulls += 1
            number_copy.remove(d)
    return cows, bulls
    
if __name__ == '__main__':
    print('Welcome to the Cows and Bulls Game!')
    number = '%04d' % random.randint(0, 9999)
    tries = 0
    while True:
        guess = input('Enter a number (%i digits) or "exit": ' % (len(number)))
        if guess == 'exit':
            break
        tries += 1

        cows, bulls = cows_bulls(guess, number)

        if cows == len(number):
            print('You win. It is %s. It took you %i tries.' % (number, tries))
            break

        print('%i cows, %i bulls' % (cows, bulls))

    
