'''Take the code from the How To Decode A Website exercise 
and instead of printing the results to a screen, write the results to a txt file. 
In your code, just make up a name for the file you are saving to.

Extras:
Ask the user to specify the name of the output file that will be saved.'''

import requests
from bs4 import BeautifulSoup

def fetchSoup(url):
    req = requests.get(url)
    page_html = req.text
    soup = BeautifulSoup(page_html, 'html.parser')
    return soup

def getTitleList(soup):
    story_heading_list = soup.find_all(class_='story-heading')
    title_list = [str(story_heading.a.text).strip() if story_heading.a else str(story_heading.string).strip()
                 for story_heading in story_heading_list]
    return title_list

def saveList(item_list, file_name):
    with open(file_name + '.txt', 'w') as file_obj:
        for item in item_list:
            file_obj.write(str(item) + '\n')

    
if __name__ == '__main__':
    myUrl = 'https://www.nytimes.com/'
    fileName = input('Give the name of the file: ')
    mySoup = fetchSoup(myUrl)
    titleList = getTitleList(mySoup)
    saveList(titleList, fileName)
