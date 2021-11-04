import string

import requests
from bs4 import BeautifulSoup
import os, os.path

pages_number = int(input())
article_type = input()
# url_base = 'https://www.nature.com/nature/articlesscsd'  # bad url internal test
url_base = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=##PAGE_NUM##'  # input()
base_path = os.getcwd()
for i in range(1, pages_number + 1):
    url = url_base.replace('##PAGE_NUM##', str(i))
    r = requests.get(url)
    os.mkdir(os.path.join(base_path, 'Page_' + str(i)))
    os.chdir(os.path.join(base_path, 'Page_' + str(i)))
    if r:
        #base_path = print(os.getcwd())
        #print(os.getcwd())
        bs = BeautifulSoup(r.content, 'html.parser')
        for article in bs.find_all('article'):
            if article.find('span', {"class": "c-meta__type"}).text == article_type:  # ex: 'News'
                article_a = article.find('a', {"data-track-action": "view article"})
                article_name = article_a.text
                article_url = 'https://www.nature.com' + article_a.get('href')
                # print(article_url)
                with requests.get(article_url) as r2:
                    article_bs = BeautifulSoup(r2.content, 'html.parser')
                    article_body = article_bs.find('div', {'class': 'c-article-body'}).text.strip()
                    tbl = str.maketrans(' ', '_', string.punctuation)
                    file_name = article_name.strip().translate(tbl) + '.txt'
                    #print(file_name)
                    # print(article_bs.find('div', {'class': 'c-article-body'}).text)
                    # print(os.getcwd())
                    with open(os.path.join(base_path, 'Page_' + str(i),file_name) , 'w', encoding="utf-8") as f_1:
                        f_1.write(article_body)
            # os.chdir("..")
    else:
        print(f"URL {url} returned status code: {r.status_code}")
