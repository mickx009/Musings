import requests
import getpass
import json
from fortigate_api import FortiGate
from pprint import pprint

username = input("Username:")
password = getpass.getpass()
host = input("Fortigate/Controller IP:")

devlist = FortiGate(host=host, username=username, password=password)

clientlist = devlist.get(url="/api/v2/monitor/wifi/client")
clients = clientlist.json()
clientdata = clients['results'[0:]]
with open('wificlients.txt', 'w') as f:
    for x in clientdata:
        f.write(x['host'] + " ")
        f.write(x['ip'] + " ")
        f.write(str(x['snr']))
        f.write("\n")
