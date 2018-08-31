'''This exercise is Part 1 of 4 of the birthday data exercise series.
For this exercise, we will keep track of when our friend’s birthdays are, 
and be able to find that information based on their name. 
Create a dictionary (in your file) of names and birthdays. 
When you run your program it should ask the user to enter a name, 
and return the birthday of that person back to them. 
The interaction should look something like this:
>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.'''

def printBirthdayDict(birthday_dict):
    print('We know the birthdays of:')
    for name in birthday_dict:
        print(name)

def printBirthdayData(person_name, birthday_dict):
    print('%s\'s birthday is %s.' % (person_name, birthday_dict[person_name]))

def askPersonName(birthday_dict):
    person_name = input('Who\'s birthday do you want to look up? ').title().strip()
    while person_name not in birthday_dict.keys():
        print('We don\'t know the birthdays of %s.' % person_name)
        person_name = input('Who\'s birthday do you want to look up? ').title().strip()
    return person_name

if __name__ == '__main__':
    birthdayDict = {
        'Albert Einstein': '14/03/1879',
        'Benjamin Franklin': '17/01/1706',
        'Ada Lovelace': '10/12/1815',
        'Rowan Atkinson': '06/01/1955',
    }

    print('Welcome to the birthday dictionary.')
    printBirthdayDict(birthdayDict)
    personName = askPersonName(birthdayDict)
    printBirthdayData(personName, birthdayDict)
