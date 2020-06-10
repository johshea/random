import requests
import sys

#IP of end host
HOST = '192.168.57.101'
#Username and Password
USER = 'api'
PASS = 'api'

def get_configured_interfaces():
    """
    Retrieving config data (interface) from RESTCONF.
    """
    url = "http://{h}/restconf/api/running/interfaces".format(h=HOST)
    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/vnd.yang.data+json',
               'Accept': 'application/vnd.yang.data+json'}
    # this statement performs a GET on the specified url
    response = requests.get(url, auth=(USER, PASS),
                            headers=headers, verify=False)

    # return the json as text
    return response.text


def main():
    """
    Simple main method calling our function.
    """
    interfaces = get_configured_interfaces()

    # print the json that is returned
    print(interfaces)

if __name__ == '__main__':
    sys.exit(main())