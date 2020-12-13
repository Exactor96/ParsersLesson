import ctypes
import os
import time

from download_wallheaven_random import check_wallheaven_url
from get_random_image_from_wallheaven import get_one_wallheaven_img
from utils import download

CHANGE_WALLPAPER_AFTER = 900  # in seconds


def set_windows_wallpaper(path):
    if os.path.isfile(path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
    else:
        print(f'{path} - not found. Enter absolute path')


def main():
    if not os.path.isdir('imgs'):
        os.mkdir('imgs')

    image_folder = os.path.join(os.path.abspath('.'), 'imgs')

    url = get_one_wallheaven_img()
    img_url, img_name = check_wallheaven_url(url)

    img_abs_path = os.path.join(image_folder, img_name)

    download(img_url, img_abs_path)

    set_windows_wallpaper(img_abs_path)

    time.sleep(CHANGE_WALLPAPER_AFTER)


if __name__ == '__main__':
    main()
