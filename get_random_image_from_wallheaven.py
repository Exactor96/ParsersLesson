import sys

import requests
from bs4 import BeautifulSoup

MAIN_URL = 'https://wallhaven.cc/random'


def get_one_wallheaven_img():
    response = requests.get(MAIN_URL)

    if response.status_code != 200:
        print(f'Status code is not 200. {response.status_code}')
        sys.exit()

    soup = BeautifulSoup(response.text, "html.parser")

    image = soup.find('div', {'id': 'thumbs'}).find('ul').find('li')

    return image.find('figure').find('a', {'class': 'preview'}).get('href')


def get_wallheavens_imgs():
    response = requests.get(MAIN_URL)

    if response.status_code != 200:
        print(f'Status code is not 200. {response.status_code}')
        sys.exit()

    soup = BeautifulSoup(response.text, "html.parser")

    images_html_list = soup.find('div', {'id': 'thumbs'}).find('ul').find_all('li')

    urls_list = []

    for item in images_html_list:
        if item.find('figure'):
            urls_list.append(item.find('figure').find('a', {'class': 'preview'}).get('href'))

    return urls_list


if __name__ == '__main__':
    print('\n'.join(get_wallheavens_imgs()))
