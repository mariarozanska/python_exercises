'''Implement a function that takes as input three variables, 
and returns the largest of the three. Do this without using the Python max() function!
The goal of this exercise is to think about some internals that Python normally takes care of for us. 
All you need is some variables and if statements!'''

import random

def findMaxNumber(int1, int2, int3):
    if int1 >= int2 and int1 >= int3:
        return int1
    elif int2 >= int1 and int2 >= int3:
        return int2
    else:
        return int3

if __name__ == '__main__':
    int1, int2, int3 = [random.randint(1, 10) for i in range(3)]
    print(int1, int2, int3)
    maxInt = findMaxNumber(int1, int2, int3)
    print(maxInt)