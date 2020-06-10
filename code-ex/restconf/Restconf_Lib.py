def get_specific_interface():
    url = "http://{h]/restconf/api/running/interfaces/interface/GigabitEthernet1".format(HOST)
    headers = {'Content-Type': 'application/vnd.yang.data+json',
               'Accept': 'application/vnd.yang.data+json'}
    response = requests.get(url, auth=(USER, PASS),
                            headers=headers, verify=False)

    return.response.text


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

