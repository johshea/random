import requests
import sys

#IP of end host
HOST = '192.168.57.101'
#Username and Password
USER = 'api'
PASS = 'api'

def get_specific_interface():
    url = "http://{h]/restconf/api/running/interfaces/interface/GigabitEthernet1".format(HOST)
    headers = {'Content-Type': 'application/vnd.yang.data+json',
               'Accept': 'application/vnd.yang.data+json'}
    response = requests.get(url, auth=(USER, PASS),
                            headers=headers, verify=False)

    return.response.text

def get_interface():
    interface = get_specific_interface()

    print(interface)

    if __name__ == 'get_interface';
        sys.exit(main())
