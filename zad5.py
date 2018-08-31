'''Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements 
that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:
Randomly generate two lists to test this
Write this in one line of Python'''

import random

# zwraca listę elementów bez powtórzeń
# a = random.sample(range(100), random.randint(5,15))
# b = random.sample(range(100), random.randint(5,15))
# z powtórzeniami
a = [random.randint(1,100) for i in range(random.randint(5,15))]
b = [random.randint(1,100) for i in range(random.randint(5,15))]
print(a)
print(b)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

intersec = list(set([x for x in a if x in b]))
print(intersec)

# intersec = list(set(a) & set(b))
# print(intersec)