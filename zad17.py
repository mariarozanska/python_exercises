'''Use the BeautifulSoup and requests Python packages 
to print out a list of all the article titles on the New York Times homepage.'''

import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.nytimes.com/')
html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')

# titles = soup.find_all(attrs={'class' : 'story-heading'})
titles = soup.find_all(class_='story-heading')
# list_of_titles = [title.a.string.strip() if title.a else title.string.strip() for title in titles]
# for title in list_of_titles:
#     print(title)

for title in titles:
    if title.a:
        print(str(title.a.text).strip())
    else: 
        print(str(title.string).strip())

# for title in titles: 
#     if title.a:
#         print(title.a.text.replace("\n", " ").strip())
#     else: 
#         print(title.contents[0].strip())


