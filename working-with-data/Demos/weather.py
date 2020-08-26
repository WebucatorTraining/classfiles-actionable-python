import requests
from datetime import datetime

API_KEY = 'abca198b092b0295697beb48914a442c'
FEED = 'https://api.openweathermap.org/data/2.5/forecast/'


def main():
    city = 'Syracuse'
    state = 'New York'
    country_code = 'us'

    params = {
        'q': city + ',' + state + ',' + country_code,
        'units': 'imperial',
        'APPID': API_KEY
    }

    r = requests.get(FEED, params)
    print(r.url) # prints the URL created using the params

    weather = r.json()

    fmt_in = '%Y-%m-%d %H:%M:%S'
    fmt_out = '%A, %B %d, %Y at %I %p'
    for item in weather['list']:
        max_temp = item['main']['temp_max']
        dt = item['dt_txt']
        day_time = datetime.strptime(dt, fmt_in).strftime(fmt_out)
        print(f'High on {day_time} in {city}: {max_temp} fahrenheit.')

main()