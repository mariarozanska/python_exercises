'''In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
This time, we’re going to do exactly the opposite. 
You, the user, will have in your head a number between 0 and 100. 
The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
At the end of this exchange, your program should print out how many guesses it took to get your number.
As the writer of this program, you will have to choose how your program will strategically guess. 
A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. 
But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 
(right in the middle of the range), and then increase / decrease by 1 as needed.'''

def getMidInt(start_int, end_int):
    return start_int + (end_int - start_int)//2

startInt = 0
endInt = 100
print('You will have in your head a number between %i and %i.' % (startInt, endInt))
print('The program will guess a number.')
tryCount = 1
while True:
    guessInt = getMidInt(startInt, endInt)
    print('My guess is %i!' % guessInt)
    userMsg = input('Is it too high (h), too low (l), or your number (x)? ').lower()
    if userMsg == 'x':
        break
    elif userMsg == 'h':
        endInt = guessInt
    elif userMsg == 'l':
        startInt = guessInt 
    tryCount += 1

print('It took %i tries.' % tryCount)