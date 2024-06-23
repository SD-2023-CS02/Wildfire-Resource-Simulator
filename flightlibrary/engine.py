# Author: DBog
# Date: 2/13/2024
# Purpose: Central running for the gathering, heart of the program
# Output: Success or Failure
import csv

import config
import identGet
import routeGet
from datetime import datetime, timedelta

def run():
    #get_idents()
    get_routes()

def get_idents():
    file = open(config.PLANE_ID_CSV, "r")
    registrations = []
    for row in file:
        registrations.append(row[:-1])
    for registration in registrations:
        identGet.create_requests(registration, datetime(year=config.START_YEAR, day=config.START_DAY, month=config.START_MONTH))

def get_routes():
    file = open(config.FLIGHT_ID_CSV, "r")
    reader = csv.reader(file)
    fa_flight_ids = []
    for row in reader:
        if row != []:
            fa_flight_ids.append([row[0],row[1]])
    routeGet.create_request(fa_flight_ids)


run()