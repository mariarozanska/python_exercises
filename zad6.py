'''Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)'''

word = input('Word: ')

if word == word[::-1]:
    print('%s is a palindrome' % word)
else:
    print('%s is not a palindrome' % word)