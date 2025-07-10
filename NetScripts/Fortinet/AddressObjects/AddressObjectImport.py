import requests
import getpass
import json
from fortigate_api import FortiGate
from pprint import pprint

username = input("Username:")
password = getpass.getpass()
host = input("Host IP:")

devlist = FortiGate(host=host, username=username, password=password)

with open("/home/python/pyscripts/AddressObjects/fortifqdn.txt", "r") as f:
    devlist = FortiGate(host=host, username=username, password=password)
    for object in f.read().splitlines():
        newobject = {
            "name": object,
            "type": "fqdn",
            "fqdn": object
        } 
        response = devlist.post(url="api/v2/cmdb/firewall/address/", data=newobject)
        result = response.json()['status']
        print(result)
        