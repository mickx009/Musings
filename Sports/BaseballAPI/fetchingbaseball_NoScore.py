import requests
from pprint import pprint
import json
from tkinter import *


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

status = []
away = []
home = []
ascore = []
hscore = []

for ateam in datalist:
    away.append(ateam['away']['team']['name'])
#    ascore.append(ateam['away']['score'])

for hteam in datalist:
    home.append(hteam['home']['team']['name'])
#    hscore.append(hteam['home']['score'])

for final in games:
    status.append(final['status']['detailedState'])

for a, h, f in zip(away, home, status):
    print("-----")
    print(a + " " + " At " + h + " " + " " + "----" + " " + f)

for a, h, f in zip(away, home, status):
    with open("todaysgames.txt", "w") as file:
        file.write(a + " " + " At " + h + " " + " " + "----" + " " + f + "\n")

#Create Tkinter Window and print from TXT file
root = Tk()
root.title("Today's MLB Games")
root.geometry("800x650")
#root.configure(bg="green")

schedule = open("todaysgames.txt", "r")
content = schedule.read()       

my_text = Text(root, width=100, height=100, font=("Helvetica", 20))
my_text.pack(expand=True, fill="both",pady=60)
my_text.tag_configure("center", justify='center')
my_text.insert(END, content)
my_text.tag_add("center", "1.0", "end")

root.mainloop()
