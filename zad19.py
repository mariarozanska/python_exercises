'''Using the requests and BeautifulSoup Python libraries, 
print to the screen the full text of the article on this website: 
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
The article is long, so it is split up between 4 pages. 
Your task is to print out the text to the screen so that you can read 
the full article without having to click any buttons.'''

import requests
from bs4 import BeautifulSoup

def get_page(url):
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    return soup

def get_article(soup):
    sections = soup.article.find_all('p')
    for sec in sections[:-1]:
        print(sec.text)

if __name__ == '__main__':
    url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
    soup = get_page(url)
    get_article(soup)
    

