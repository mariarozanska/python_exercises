'''This exercise is Part 3 of 3 of the Hangman exercise series.
In this exercise, we will finish building Hangman. In the game of Hangman, 
the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.
Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:
Only let the user guess 6 times, and tell the user how many guesses they have left.
Keep track of the letters the user guessed. If the user guesses a letter they already guessed, 
don’t penalize them - let them guess again.
Optional additions:
When the player wins or loses, let them start a new game.
Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman.
Your solution will be a lot cleaner if you make use of functions to help you!'''

import zad30
import zad31

if __name__ == '__main__':
    # hangmanList = makeHangmanList()
    while True:
        print('Welcome to Hangman!')
        clueWord = zad30.pickRandomWord()
        clueWordList = zad31.makeClueWordList(clueWord)
        guessWordList = zad31.makeGuessWordList(clueWordList)
        guessLetterSet = zad31.makeGuessLetterSet()
        mistakeCount = 0
        while mistakeCount <= 6:
            print()
            print('You have %i incorrect guesses left.' % (6 - mistakeCount))            
            zad31.printGuessLetterSet(guessLetterSet)
            zad31.printGuessWord(guessWordList)
            guessLetter = zad31.getLetter(guessLetterSet)
            if zad31.hasGuessLetter(clueWordList, guessWordList, guessLetter):
                if zad31.isWin(clueWordList, guessWordList):
                    print('You won!')
                    break
            else:
                mistakeCount += 1
        else:
            print('You lost!')
        print('The word is %s.' % clueWord)
        
        game = input('Do you want to play again (y/n)? ').lower()
        if game == 'n':
            break