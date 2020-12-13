import sys

import requests
from bs4 import BeautifulSoup

MAIN_URL = 'https://habr.com/ru/top/'

response = requests.get(MAIN_URL)

if response.status_code != 200:
    print(f'Status code is not 200. {response.status_code}')
    sys.exit()

soup = BeautifulSoup(response.text, "html.parser")

most_read_html_list = soup.find('ul', {
    'class': 'content-list content-list_most-read'})  # Получаем ul (список самых чистаемых статей)

most_read_articles = {}

for item in most_read_html_list.find_all('li'):
    article_name = item.find('a').text
    article_url = item.find('a').get('href')
    most_read_articles[article_url] = article_name

for key, value in most_read_articles.items():
    print(f'{value}\n{key}')
    print('-' * 30)
