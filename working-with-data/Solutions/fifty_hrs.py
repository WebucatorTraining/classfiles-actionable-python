import requests
from bs4 import BeautifulSoup

# Constants to express which content is in which cells
NUM = 0
PLAYER = 1
HRS = 2
YEAR = 3
BIRTH_DAY = 4

def get_content():
    url = 'https://www.webucator.com/course-demos/python/hrleaders.cfm'
    r = requests.get(url)
    return r.text

def get_soup(content):
    return BeautifulSoup(content, 'lxml')

def get_players(soup):
    data_container = soup.find('tbody')

    # Get all table rows in the tbody
    rows = data_container.find_all('tr')

    players = []
    # Loop through the rows
    for row in rows:
        # Get int value of HRS text
        hrs = int(row.find_all('td')[HRS].text)
        if hrs >= 50:
            player = row.find_all('td')[PLAYER].text
            # Add the name of the player to players
            #  but only if they're not already in there
            if player not in players:
                players.append(player)
        if hrs < 50:
            return players # No need to keep looking
    
    return players # Just in case all have 50 or more hrs

def main():
    content = get_content()
    soup = get_soup(content)
    players = get_players(soup)

    for i, player in enumerate(players, 1):
        print(f'{i}. {player}')

main()