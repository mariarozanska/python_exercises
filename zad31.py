'''This exercise is Part 2 of 3 of the Hangman exercise series.
Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program 
that the player has to guess, letter by letter. The player guesses one letter at a time 
until the entire word has been guessed. 
(In the actual game, the player can only guess 6 letters incorrectly before losing).
Let’s say the word the player has to guess is “EVAPORATE”. 
For this exercise, write the logic that asks a player to guess a letter 
and displays letters in the clue word that were guessed correctly. 
For now, let the player guess an infinite number of times until they get the entire word. 
As a bonus, keep track of the letters the player guessed 
and display a different message if the player tries to guess that letter again. 
Remember to stop the game when all the letters have been guessed correctly! 
Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining.
An example interaction can look like this:
>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on, until the player gets the word.'''

def makeClueWordList(clue_word):
    return list(clue_word)

def makeGuessWordList(clue_word_list):
    return ['_'] * len(clue_word_list)

def makeGuessLetterSet():
    return set()

def hasGuessLetter(clue_word_list, guess_word_list, guess_letter):
    if guess_letter not in clue_word_list:
        print('Incorrect!')
        return False
    else:
        print('Correct!')
        setGuessWordList(clue_word_list, guess_word_list, guess_letter)
        return True

def setGuessWordList(clue_word_list, guess_word_list, guess_letter):
    for i in range(len(clue_word_list)):
        if guess_letter == clue_word_list[i]:
            guess_word_list[i] = guess_letter

def setGuessLetterSet(guess_letter_set, guess_letter):
    guess_letter_set.add(guess_letter)

def isUsedGuessLetter(guess_letter_set, guess_letter):
    return guess_letter in guess_letter_set

def printGuessWord(guess_word_list):
    print(' '.join(guess_word_list))

def printGuessLetterSet(guess_letter_set):
    print('Used letters: %s' % guess_letter_set)

def getLetter(guess_letter_set):
    guess_letter = input('Guess your letter: ').upper()
    while isUsedGuessLetter(guess_letter_set, guess_letter):
        print('You try to guess that letter again.')
        guess_letter = input('Guess your letter: ').upper()
    setGuessLetterSet(guess_letter_set, guess_letter)
    return guess_letter

def isWin(clue_word_list, guess_word_list):
    return clue_word_list == guess_word_list

if __name__ == '__main__':
    clueWord = 'PYTHON'
    clueWordList = makeClueWordList(clueWord)
    guessWordList = makeGuessWordList(clueWordList)
    guessLetterSet = makeGuessLetterSet()
    mistakeCount = 0
    while mistakeCount < 6:
        print()
        printGuessWord(guessWordList)
        printGuessLetterSet(guessLetterSet)
        guessLetter = getLetter(guessLetterSet)
        if hasGuessLetter(clueWordList, guessWordList, guessLetter):
            if isWin(clueWordList, guessWordList):
                print('You won! The word is %s.' % clueWord)
                break
        else:
            mistakeCount += 1
    else:
        print('You lost!')