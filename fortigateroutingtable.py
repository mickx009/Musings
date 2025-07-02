import requests
import getpass
import json
from fortigate_api import FortiGate
from pprint import pprint

username = input("Username:")
password = getpass.getpass()
host = "10.10.30.1"

devlist = FortiGate(host=host, username=username, password=password)

routingtable = devlist.get(url="/api/v2/monitor/router/ipv4")
results = routingtable.json()
resultsdefined = results['results']

with open('routetable.txt', 'w') as f:
    for x in resultsdefined:
        f.write(x['ip_mask'] + "\n")
        f.write(x['interface'] + "\n")


