'''Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right. 

Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.'''

import random

number = random.randint(1, 9)
tries = 1
while True:
    guess = int(input('Guess the number (1-9): '))

    if number == guess:
        print('Yes, it\'s {}. It took you {} tries.'.format(number, tries))
        break
    if number > guess:
        print('Too low...')
    else:
        print('Too high...')
    
    game = input('Do you want to try again? (y/exit) ')
    if game == 'exit':
        break
    tries += 1

