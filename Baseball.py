import requests
from pprint import pprint
import json


blanklist = []
url = "http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1"
response = requests.get(url)
MLB = response.json()
date = MLB['dates'][0]['date']
print("Today's MLB Schedule!")
print(date)
games = MLB['dates'][0]['games'][0:]
for x in games:
    blanklist.append(x['teams'])

away = []
home = []
for ateam in blanklist:
    away.append(ateam['away']['team']['name'])

for hteam in blanklist:
    home.append(hteam['home']['team']['name'])

for a, h in zip(away, home):
    print("-----")
    print(a + " At " + h)

