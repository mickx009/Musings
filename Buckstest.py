import requests
from pprint import pprint
import json

#date = input("Today's Date: ")
url = "https://cdn.nba.com/static/json/staticData/scheduleLeagueV2.json"
response = requests.get(url)
bucks = response.json()
gddict = bucks['leagueSchedule']['gameDates']

games = gddict[150]['games']

awayteam = []
hometeam = []

for x in games:
    awayteam.append(x['awayTeam']['teamName'])
    hometeam.append(x['homeTeam']['teamName'])

def matchups(awayteam, hometeam):
    return [sub[item] for item in range(len(hometeam))
                      for sub in [awayteam, hometeam]]

gamestoday = matchups(awayteam, hometeam)
#pprint(gamestoday)

for i in range(0, len(gamestoday), 2):
    print(gamestoday[i], "At", gamestoday[i + 1])


































#################   Test Code ####################

    #print(str(gamestoday[i]), '+', str(gamestoday[i + 1]), '=', str(gamestoday[i] + gamestoday[i + 1]))

# for i in range(len(gamestoday) - 1):
#     print(gamestoday[i], gamestoday[i + 1])

# for teams in gamestoday:
#     print("The", teams, "at The", teams)

#pprint(awayteam[0])
# pprint(gddict[148]['games'][2]['awayTeam'])
# pprint(gddict[148]['games'][2]['homeTeam'])


        