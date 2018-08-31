'''Given a .txt file that has a list of a bunch of names, 
count how many of each name there are in the file, and print out the results to the screen. 

Extra:
Instead of using the .txt file from above, take this .txt file, 
and count how many of each “category” of each image there are. 
This text file is actually a list of files corresponding to the SUN database scene recognition database, 
and lists the file directory hierarchy for the images. 
Once you take a look at the first line or two of the file, 
it will be clear which part represents the scene category.'''

import re

def getNameCountDict(name_list):
    name_set = set(name_list)
    name_count_dict = {name: name_list.count(name) for name in name_set}
    return name_count_dict

def getCategoryCountDict(file_text):
    category_regex = r'/./(\w+?)/'
    category_list = re.findall(category_regex, file_text)
    category_set = set(category_list)    
    category_count_dict = {category: category_list.count(category) for category in category_set}
    return category_count_dict

if __name__ == '__main__':
    with open('names.txt', 'r') as file_obj:
        nameList = file_obj.read().split()
    nameCountDict = getNameCountDict(nameList)
    print(nameCountDict)

    with open('images.txt', 'r') as file_obj:
        fileText = file_obj.read()
    categoryCountDict = getCategoryCountDict(fileText)
    print(categoryCountDict)