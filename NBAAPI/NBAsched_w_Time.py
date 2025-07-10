import requests
from pprint import pprint
import json
import datetime
from tkinter import *

date = input("Enter Game Date (ex. xx/xx/xxxx): " )
zeroes = "00:00:00"
url = "https://cdn.nba.com/static/json/staticData/scheduleLeagueV2.json"
response = requests.get(url)
bucks = response.json()
gddict = bucks['leagueSchedule']['gameDates']

indexday = []

awayteam = []
hometeam = []
gametime = []
scoreaway = []
scorehome = []

for l in range(0, len(gddict), 1):
    if gddict[l]['gameDate'] == date + " " + zeroes:
        indexday.append(l)

try:
    games = gddict[indexday[0]]['games']
    for x in games:
        awayteam.append(x['awayTeam']['teamName'])
        hometeam.append(x['homeTeam']['teamName'])
        gametime.append(x['gameStatusText'])
        scoreaway.append(x['awayTeam']['score'])
        scorehome.append(x['homeTeam']['score'])

except IndexError:
    print("Wrong Date Format!")

def matchups(awayteam, hometeam, gametime, scoreaway, scorehome):
    return [sub[item] for item in range(len(hometeam))
                    for sub in [awayteam, hometeam, gametime, scoreaway, scorehome]]

gamestoday = matchups(awayteam, hometeam, gametime, scoreaway, scorehome)

for i in range(0, len(gamestoday), 5):
    # print(gamestoday[i], "At", gamestoday[i + 1], " -- ", gamestoday[i + 2], "-- ", gamestoday[i + 3], "To", gamestoday[i + 4])
    # print("-" * 70)
    endresult = gamestoday[i], "At", gamestoday[i + 1], " -- ", gamestoday[i + 2], "-- ", gamestoday[i + 3], "To", gamestoday[i + 4]
    pprint(endresult)
    root = Tk()
    w = Label(root, text=endresult)
    w.pack
    root.mainloop()

#print(gamestoday)

