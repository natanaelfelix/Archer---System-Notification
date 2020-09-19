import requests
import json
from switch_data import SwitchData

base_uri = 'https://148.148.205.115/webacs/api/v4'
user = 'mspdaemon'
password = 'eHr1h]fc'
rest_path = '/data/InventoryDetails/.json?.full=true&summary.reachability=REACHABLE'
device_list = []


url = base_uri + rest_path
response = requests.request('GET', url, auth=(user, password), verify=False)
jsonResponse = json.loads(response.text)

visu = []
sh = input('Digite o host:')
inter = input('Digite a interface:')
for entity in jsonResponse['queryResponse']['entity']:

    summary = entity['inventoryDetailsDTO']['summary']
    device_id = summary['deviceId']
    device_name = summary['deviceName']
    device_typ = summary['deviceType']
    ip_add = summary['ipAddress']
    reach = summary['reachability']
    uptime = summary['upTime']
    host = summary['deviceName']
    if sh == host:
        print (host)
        for interface in entity['inventoryDetailsDTO']['ethernetInterfaces']['ethernetInterface']:
                port = interface['name']
                status = interface['operationalStatus']
                adm = interface['adminStatus']
                if inter == port:
                    print( port, status, adm)





