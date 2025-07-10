import requests
import getpass
import json
from fortigate_api import FortiGate
from pprint import pprint

username = input("Username:")
password = getpass.getpass()
host = input("Firewall MGMT IP:")
fqdn = input("DDNS: ")

devlist = FortiGate(host=host, username=username, password=password)

newobject = {
            "name": fqdn,
            "type": "fqdn",
            "fqdn": fqdn
}

#Create new Address Object
newadobject = devlist.post(url="api/v2/cmdb/firewall/address/", data=newobject)
newaddobresp = newadobject.json()['status']
print("New Address Object:",newaddobresp)

#Append Group with New Object

createdobject = {
    "name": fqdn
}
groupappend = devlist.post(url="api/v2/cmdb/firewall/addrgrp/<GROUPNAME>/member/", data=createdobject)
print("Merge",groupappend)