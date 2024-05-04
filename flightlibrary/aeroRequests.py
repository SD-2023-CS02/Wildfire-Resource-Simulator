# Author: DBog
# Date: 2/13/2024
# Purpose: Runs a given request link. Put aside for less repeating code segments
# Output: JSON response from given link

import requests
from requests.auth import HTTPBasicAuth

import config
import costScripting


def request(link, type):
    print("Request Sent:", link, " Type:", type)
    if type == 1:
        payload = {'max_pages': 10}
        auth_header = {'x-apikey': config.APIKEY,
                       'Accept': 'application/json; charset=utf-8'}

        response = requests.get(link, params=payload, headers=auth_header)
        costScripting.ident_grab()
    elif type == 2:
        costScripting.ident_grab()
        response = requests.get(link)
    else:
        url = link
        auth_header = {'x-apikey': config.APIKEY,
                       'Accept': 'application/json; charset=utf-8'}

        costScripting.route_grab()
        response = requests.get(url, headers=auth_header)

    if response.status_code == 400:
        print("ERROR: Response Code 400")
        print(response.json())
        exit(1)
    elif response.status_code == 401:
        print("Bad Key :(")
    else:
        print("Success")

    return response.json()