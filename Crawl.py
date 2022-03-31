from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
import requests
import re

url = 'https://www.dienmayxanh.com/kinh-nghiem-hay/honor-ra-mat-san-pham-moi-vao-ngay-29-3-du-kien-t-1422619'

def crawNewsdata(url):
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.text, 'html.parser')
    # craw title
    title = soup.find('div',class_='bcenter').find('h1').text
    # craw header
    header = []
    for item in soup.find('div',class_='bxcontentnews').findAll('h3'):
        header.append(item.text)

    description = []
    for item in soup.findAll('figcaption'):
        description.append(item.text)

    # craw content except description's images
    content = ''
    for item in soup.find('div',class_='bxcontentnews').findAll('p'):
        if item.text not in description:
            content += item.text

    print('Title: "{}"'.format(title))
    print('Header: "{}"'.format(';'.join(header)))
    print('Content: "{}"'.format(content))

crawNewsdata(url)

