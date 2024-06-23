# Author: DBog
# Date: 2/6/2024
# Purpose: Creates route Get Requests and Runs them to gather JSON responses.
# Output: JSON response from Route Get Requests

# Vocab: Route - a list of plane locations for a given fa_flight_id from link: https://aeroapi.flightaware.com/aeroapi/history/flights/{id}/route

import json
import routeParse
import aeroRequests

# converts file to json right now. eventually this will be used in the curl request function to convert response to json
def convert_json(respJson, fa_flight_id, registration):
    routeParse.run(respJson, fa_flight_id, registration)
    #with open('test2.json') as json_file:
     #   data = json.load(json_file)
      #  routeParse.run(data)

# gets a list of fa_flight_ids from a given filename into a list to use for creating the links
def get_fa_flight_id(filename):
    file = open(filename)
    fa_flight_ids = []
    for fa_flight_id in file:
        fa_flight_ids.append(fa_flight_id)
    return fa_flight_ids

# creates the request link for a given fa_flight_id
def create_link(fa_flight_id):
    apilink = "https://aeroapi.flightaware.com/aeroapi/history/flights/"

    getstring = fa_flight_id[0] + "/track"

    curlstring = apilink + getstring
    return curlstring

# creates the list of request links for all fa_flight_ids
def create_request(fa_flight_ids):
    links = []
    for fa_flight_id in fa_flight_ids:
        links.append((create_link(fa_flight_id), fa_flight_id[0], fa_flight_id[1]))

    for link in links:
        curl_request(link[0], link[1], link[2])

# curls a single link and calls convert_json() that will run the routeParse.py file.
def curl_request(request_link, fa_flight_id, registration):
    # will curl the link
    respJson = aeroRequests.request(request_link, 0)
    convert_json(respJson, fa_flight_id, registration)
