'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.'''

import random 

def first_last_element(l):
    return [l[0], l[-1]]

# my_list = [5, 10, 15, 20, 25]
my_list = random.sample(range(100), k=random.randint(5, 15))
print(my_list)
res = first_last_element(my_list)
print(res)