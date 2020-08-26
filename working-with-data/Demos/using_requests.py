import requests

url = 'https://www.webucator.com/course-demos/python/hrleaders.cfm'
r = requests.get(url)
content = r.text
print(content[:125]) # print first 125 characters