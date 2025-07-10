import requests
import getpass
import json
from fortigate_api import FortiGate
from pprint import pprint

#devices = ["10

username = input("Username:")
password = getpass.getpass()

Unregister = {
    "unregister": True
}

NewFMG = {
    "fortimanager_ip": "<FortiManager_IP>",
    "serial": "<FortigateSerial>"
}

#Unregister Fortigate from old FortiManager

with open("hostfile.txt", "r") as f:
    for host in f.read().splitlines():
        devlist = FortiGate(host=host, username=username, password=password)    
        response = devlist.post(url="api/v2/monitor/system/fortimanager/config", data=Unregister)
        result = response.json()['status']
        print(host,"Unregister:")
        pprint(result)

#Register Fortigate with new FortiManager

with open("hostfile.txt", "r") as f:
    for host in f.read().splitlines():
        devlist = FortiGate(host=host, username=username, password=password)    
        response = devlist.post(url="api/v2/monitor/system/fortimanager/config", data=NewFMG)
        result = response.json()['status']
        print(host, "FMG_Change:")
        pprint(result)

