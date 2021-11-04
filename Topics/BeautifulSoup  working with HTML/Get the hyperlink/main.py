import requests

from bs4 import BeautifulSoup

line, url = (int(input()), input())
r = requests.get(url)
bs = BeautifulSoup(r.content, 'html.parser')
links = bs.find_all('a')
print(links[line - 1].get('href'))
