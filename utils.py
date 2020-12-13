import requests


def download(url, path):
    f = open(path, 'wb')
    content = requests.get(url).content
    f.write(content)
    f.close()
