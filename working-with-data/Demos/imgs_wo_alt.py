import requests
from bs4 import BeautifulSoup


def get_content():
    url = input('Enter a URL: ')
    r = requests.get(url)
    return r.text

def main():
    content = get_content()
    soup = BeautifulSoup(content, 'lxml')

    images = soup.find_all('img', alt=False)

    found = False
    for i, img in enumerate(images, 1):
        found = True
        print(f'{i}. {img}')

    if not found:
        print('None found.')

main()