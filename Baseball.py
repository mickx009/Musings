import requests
from pprint import pprint
import json


datalist = []
url = "http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1"
response = requests.get(url)
MLB = response.json()
date = MLB['dates'][0]['date']
print("Today's MLB Schedule!")
print(date)
games = MLB['dates'][0]['games'][0:]
for x in games:
    datalist.append(x['teams'])

away = []
home = []
ascore = []
hscore = []

for ateam in datalist:
    away.append(ateam['away']['team']['name'])
    ascore.append(ateam['away']['score'])

for hteam in datalist:
    home.append(hteam['home']['team']['name'])
    hscore.append(hteam['home']['score'])

for a, h, aws, hos in zip(away, home, ascore, hscore):
    print("-----")
    print(a + " " + str(aws) + " At " + h + " " + str(hos))

