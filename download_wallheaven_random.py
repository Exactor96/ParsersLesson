import os

import requests
from bs4 import BeautifulSoup

from get_random_image_from_wallheaven import get_wallheavens_imgs
from utils import download


def check_wallheaven_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f'{url} - return not 200 status code. {response.status_code}')

    soup = BeautifulSoup(response.text, "html.parser")
    img = soup.find('img', {'id': 'wallpaper'})
    url = img.get('src')
    name = os.path.split(url)[-1]

    return url, name


def main():
    if not os.path.isdir('imgs'):
        os.mkdir('imgs')

    image_folder = os.path.join(os.path.abspath('.'), 'imgs')

    urls_list = get_wallheavens_imgs()
    iterator = 0
    for url in urls_list:
        img_url, img_name = check_wallheaven_url(url)
        download(img_url, os.path.join(image_folder, img_name))
        iterator += 1
        print(f'{iterator}/{len(urls_list)}\t{img_name} - is Downloaded')


if __name__ == '__main__':
    main()
