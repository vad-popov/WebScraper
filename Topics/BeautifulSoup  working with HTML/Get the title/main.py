import requests

from bs4 import BeautifulSoup

url = input()
r = requests.get(url)
if r:
    bs = BeautifulSoup(r.content, 'html.parser')
    t = bs.find('h1')
    print(t.text)
