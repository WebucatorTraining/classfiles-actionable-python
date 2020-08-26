import requests
from bs4 import BeautifulSoup


def get_content():
    url = input('Enter a URL: ')
    r = requests.get(url)
    return r.text

def main():
    content = get_content()
    soup = BeautifulSoup(content, 'lxml')

    external_links = soup.find_all('a', target='_blank')

    found = False
    for i, link in enumerate(external_links, 1):
        found = True
        print(f'{i}. {link}')

    if not found:
        print('None found.')

main()