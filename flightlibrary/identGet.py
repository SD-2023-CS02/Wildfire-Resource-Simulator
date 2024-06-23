# Author: DBog
# Date: 2/5/2024
# Purpose: Creates Ident Get Requests and Runs them to gather JSON responses.
# Output: JSON response from Ident Get Requests

# Vocab: Ident - Means identification. Every reference to it is to run the https://aeroapi.flightaware.com/aeroapi/history/flights/ run

import json

import config
import identParse
import aeroRequests
from datetime import datetime, timedelta

# converts file to json right now. eventually this will be used in the curl request function to convert response to json
def convert_json(respJson, registration):
    for resp in respJson:
        identParse.run(resp, registration)

# gets the date ranges of 7 days for the ranges in the link requests
def date_range_calculator(prev_end):
    new_end = prev_end + timedelta(days=7)
    return (prev_end,new_end)

# converts the timerange to the string format required for AeroAPI
def time_convert(timerange):
    start = timerange[0]
    end = timerange[1]

    newstart = str(start.year) + "-" + str(start.month).zfill(2) + "-" + str(start.day).zfill(2) + "T" + str(start.hour).zfill(2) + \
               "%3A" + str(start.minute).zfill(2) + "%3A" + str(start.second).zfill(2) + "Z"

    newend = str(end.year) + "-" + str(end.month).zfill(2) + "-" + str(end.day).zfill(2) + "T" + str(end.hour).zfill(2) + \
               "%3A" + str(end.minute).zfill(2) + "%3A" + str(end.second).zfill(2) + "Z"

    return (newstart, newend)

# puts together the link to run in the curl request
def create_link(timerange, registration):
    apilink = "https://aeroapi.flightaware.com/aeroapi/history/flights/"

    getstring = registration + "?start=" + timerange[0] + "&end=" + timerange[1] + "&max_pages=10"

    curlstring = apilink + getstring
    return curlstring

# curls the request link and sends the response to the convert_json() function
def curl_request(link, registration):
    # will curl the link
    respJson = aeroRequests.request(link, 1)
    responseList = []
    responseList.append(respJson)
    if respJson['num_pages'] > 1:
        print("Pagination Run")
        print(respJson)
        cur = respJson
        while cur['links'] is not None:
            resp = aeroRequests.request(cur['links']['next'], 1)
            cur = resp
            responseList.append(resp)
        print(responseList)
    convert_json(responseList, registration)

# creates the requests for one plane registration, and sends them to the curl request function
def create_requests(registration, startdate):
    today = False
    requests = []
    current_start = startdate
    count = 0
    while not today:
        count += 1
        daterange = date_range_calculator(current_start)
        if daterange[1] > datetime(year=config.END_YEAR, day=config.END_YEAR, month=config.END_MONTH):
            today = True
            break
        requests.append(create_link(time_convert(daterange), registration))
        current_start = daterange[1]

    for request in requests:
        curl_request(request, registration)
