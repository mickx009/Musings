import requests
import getpass
import json
from fortigate_api import FortiGate
from pprint import pprint

username = input("Username:")
password = getpass.getpass()
host = input("FIREWALL MGMT IP:")

devlist = FortiGate(host=host, username=username, password=password)

response = devlist.get(url="api/v2/cmdb/vpn.ipsec/phase1-interface/")
phase1vpns = response.json()['results']
pprint(phase1vpns)
ddnslist = []
for ddns in phase1vpns:
   ddnslist.append(ddns['remotegw-ddns'])  
pprint(ddnslist)    

with open('VPN_INT_NAME.txt', 'w') as fqdn:
   for x in ddnslist:
       fqdn.write(f"{x}\n")

