'''Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below.'''

import math

def is_prime(n):
    # if n == 1:
    #     return False

    # for i in range(2, round(num/2)):
    #     if num % i == 0:
    #         return False
    
    
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    for i in range(3, round(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False

    return True


num = int(input('Number: '))
res = is_prime(num)
print(res)