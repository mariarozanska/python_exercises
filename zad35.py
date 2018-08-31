'''This exercise is Part 3 of 4 of the birthday data exercise series.
In the previous exercise we saved information about famous scientists’ names and birthdays to disk. 
In this exercise, load that JSON file from disk, extract the months of all the birthdays, 
and count how many scientists have a birthday in each month.
Your program should output something like:
{
	"May": 3,
	"November": 2,
	"December": 1
}'''

import zad34
import calendar
from collections import Counter

def getMonthDict(birthday_dict):
    birthday_data_list = [calendar.month_name[int(data.split('/')[1])] for data in birthday_dict.values()]
    return dict(Counter(birthday_data_list))
    # birthday_data_list = [int(data.split('/')[1]) for data in birthday_dict.values()]
    # return {calendar.month_name[i]: birthday_data_list.count(i) for i in range(1, 13)}

def printMonthDict(month_dict):
    for i in range(1, 13):
        month = calendar.month_name[i]
        if month in month_dict:
        # if month_dict[month] != 0:
            print('{:10s} {}'.format(month, month_dict[month]))
    
if __name__ == '__main__':  
    birthdayDict = zad34.loadBirthdayDict()
    monthDict = getMonthDict(birthdayDict)
    printMonthDict(monthDict)
    