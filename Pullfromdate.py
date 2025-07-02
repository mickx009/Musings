import requests
from pprint import pprint
import json

date = "03/13/2025 00:00:00" 
#date = input("Today's Date: ")
url = "https://cdn.nba.com/static/json/staticData/scheduleLeagueV2.json"
response = requests.get(url)
bucks = response.json()
gddict = bucks['leagueSchedule']['gameDates']
# print(len(gddict))

for i in range(0, len(gddict), 1):
    if gddict[i]['gameDate'] == date:
        pprint(i)