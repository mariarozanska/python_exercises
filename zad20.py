'''Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list 
and returns (then prints) an appropriate boolean.

Extras:
Use binary search.'''

# Zał. Lista bez powtórzeń

import random

def getMidIndex(start_index, end_index):
    return start_index + (end_index - start_index)//2

# def hasNumber(ordered_number_list, number):
#     start_index = 0
#     end_index = len(ordered_number_list)

#     while start_index < end_index - 1:
#         mid_index = getMidIndex(start_index, end_index)
#         if ordered_number_list[mid_index] == number:
#             return True
#         elif ordered_number_list[mid_index] > number:
#             end_index = mid_index
#         else:
#             start_index = mid_index

#     if start_index == 0 and ordered_number_list[start_index] == number:
#         return True
 
#     return False

def hasNumber(ordered_number_list, number):
    start_index = 0
    end_index = len(ordered_number_list)
    
    mid_index = getMidIndex(start_index, end_index)
    if ordered_number_list[mid_index] == number:
        return True
    if end_index == 1:
        return False
    
    if ordered_number_list[mid_index] > number:
        end_index = mid_index
    else:
        start_index = mid_index
          
    return hasNumber(ordered_number_list[start_index : end_index], number)

if __name__ == '__main__':
    orderedIntList = random.sample(range(21), random.randint(1, 10))
    orderedIntList.sort()
    print(orderedIntList)
    numberInt = random.randint(0, 20)
    print(numberInt)
    hasNumberBool = hasNumber(orderedIntList, numberInt)
    print(hasNumberBool)