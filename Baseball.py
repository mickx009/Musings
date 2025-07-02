import requests
from pprint import pprint
import json

#date = input("Today's Date: ")
url = "http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1"
response = requests.get(url)
MLB = response.json()
date = MLB['dates'][0]['date']
print(date)

awaylist = []
homelist = []

dataaway = MLB['dates'][0]['games'][0]['teams']['away']['team']['name']
datahome = MLB['dates'][0]['games'][0]['teams']['home']['team']['name']

for team1 in dataaway:
    awaylist.append(team1)

for team2 in datahome:
    homelist.append(team2)

awayteams = ' '.join(awaylist)
hometeams = ' '.join(homelist)

finalaway = awayteams.strip("")
finalhome = hometeams.strip("")

print(finalaway +  " AT "  + finalhome)
#print(homelist)



# print(dataaway)
# print("vs.")
# print(datahome)


