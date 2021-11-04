import requests

from bs4 import BeautifulSoup

line, url = (int(input()), input())
r = requests.get(url)
bs = BeautifulSoup(r.content, 'html.parser')
print(bs.find_all('h2')[line].text)
