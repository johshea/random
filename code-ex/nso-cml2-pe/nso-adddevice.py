import requests
import yaml

# load values from Yaml into a dictionary
with open(r'./nso_env.yml') as file:
    #handlers = yaml.load(file, Loader=yaml.SafeLoader)
    handlers = yaml.safe_load(file)





### NSO Provisioning Functions
def adddev(devdata):
  headers = {
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+xml',
        'Authorization': 'Basic YWRtaW46YWRtaW4=',
        # 'Content-Type': 'text/plain'
   }

  url = f"http://{handlers['nsoip']}:{handlers['nsoport']}/restconf/data/tailf-ncs:devices"
  print(url)


  response = requests.request("POST", url, headers=headers, data = devdata)
  print(response.text.encode('utf8'))
  return

def fetchkeys(keydata, payload):
    headers = {
        'Accept': 'application/yang-data+json',
        'Authorization': 'Basic YWRtaW46YWRtaW4='
    }

    url = f"http://{handlers['nsoip']}:{handlers['nsoport']}/restconf/data/tailf-ncs:devices/device={keydata}/ssh/fetch-host-keys"
    print(url)

    response = requests.request("POST", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))

    return
def add_devgroup(devgroup):
   headers = headers = {
        'Content-Type': 'application/yang-data+xml',
        'Authorization': 'Basic YWRtaW46YWRtaW4=',
        'Accept': 'application/yang-data+json'
     }

   url = f"http://{handlers['nsoip']}:{handlers['nsoport']}/restconf/data/tailf-ncs:devices"

   response = requests.request("PATCH", url, headers=headers, data=devgroup)
   print(response.text.encode('utf8'))

#build the device XML and send it to NSO
for device in handlers['devices'].keys():

   devdata = "\n<device>\n <name>" + handlers['devices'][device]['name'] + "</name>\n <address>" + handlers['devices'][device]['ip'] + "</address>\n <port>" + handlers['devices'][device]['port']  \
       + "</port>\n <authgroup>" + handlers['devices'][device]['authgroup'] + "</authgroup>\n <device-type>\n   <cli>\n     <ned-id xmlns:" + handlers['devices'][device]['cli']  \
       + "=\"http://tail-f.com/ns/ned-id/" + handlers['devices'][device]['cli'] + "\">" + handlers['devices'][device]['cli'] + ":" + handlers['devices'][device]['cli'] \
       + "</ned-id>\n   </cli>\n </device-type>\n <state>\n <admin-state>" + handlers['devices'][device]['state'] + "</admin-state>\n </state>\n</device>\n        "
   #Formatting validation

   #call the add Device function to create the devices
   adddev(devdata)

#Fetch Host Keys from defined devices
for device in handlers['devices'].keys():
    keydata = handlers['devices'][device]['name']
    #print(keydata)
    payload = {}
    fetchkeys(keydata, payload)

#Create Device Groups and add devices to those groups
for device in handlers['devices'].keys():
    devgroup = "\n<devices xmlns=\"http://tail-f.com/ns/ncs\">\n<device-group>\n<name>"+handlers['devices'][device]['devicegroup']+"</name>\n<device-name>"+handlers['devices'][device]['name'] \
    +"</device-name>\n</device-group>\n<device-group>\n<name>parent-group-all-devices+</name>\n<device-group>"+handlers['devices'][device]['devicegroup']+"</device-group>\n</device-group>\n</devices>\n"

    print(devgroup)
    add_devgroup(devgroup)

