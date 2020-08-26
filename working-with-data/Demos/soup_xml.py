import requests
from bs4 import BeautifulSoup

url = 'https://www.webucator.com/course-demos/python/hrleadersxml.cfm'
r = requests.get(url)
content = r.text

soup = BeautifulSoup(content, 'lxml')

players = soup.find_all('player')
for i, player in enumerate(players, 1):
    print(f'{i}. {player.text}')