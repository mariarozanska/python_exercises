'''Write a program (function!) that takes a list and returns a new list that contains 
all the elements of the first list minus all the duplicates.

Extras:
Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.'''

import random

# def remove_duplicates(l):
#     return list(set(l))

def remove_duplicates(l):
    l_unique = []
    for x in l:
        if x not in l_unique:
            l_unique.append(x)
    return l_unique

my_list = [random.randint(1, 10) for i in range(random.randint(5, 10))]
my_list_unique = remove_duplicates(my_list)
print(my_list)
print(my_list_unique)