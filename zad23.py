'''Given two .txt files that have lists of numbers in them, 
find the numbers that are overlapping. 
One .txt file has a list of all prime numbers under 1000, 
and the other .txt file has a list of happy numbers up to 1000.'''

def getListInt(file_obj):
    return [int(line) for line in file_obj]

with open('prime_numbers.txt', 'r') as primeFileObj, \
     open('happy_numbers.txt', 'r') as happyFileObj:
    # primeNumberSet = set(primeFileObj.read().split())
    # happyNumberSet = set(happyFileObj.read().split())
    # primeAndHappySet = primeNumberSet & happyNumberSet
    # print(primeAndHappySet)

    primeNumberList = getListInt(primeFileObj)
    happyNumberList = getListInt(happyFileObj)
    primeAndHappyList = [num for num in primeNumberList if num in happyNumberList]
    print(primeAndHappyList)
