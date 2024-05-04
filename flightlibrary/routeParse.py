# Author: DBog
# Date: 2/8/2024
# Purpose: Parse the JSON given from routeGet and then gets parsed into single lines for file
# Output: flight_route_locations.txt a list of all flight locations ith a given flightid and such

import csv

# runs the routeParse program, will be run for each json file
import config


def run(jsonDict, fa_flight_id, registration):
    flight_route_points = []
    print(jsonDict)
    flight_positions = jsonDict["positions"]
    for flight_point in flight_positions:
        add(flight_point, flight_route_points, fa_flight_id, registration)
        # currently only adds fa_flight_id's. considering more attributes to add
    write(flight_route_points)

# Adds flight point to flight_route_point list. this parses the given dictionary to have the information needed
def add(flight_position, flight_route_points, fa_flight_id, registration):
    flight_point = [fa_flight_id, flight_position["altitude"], flight_position["altitude_change"],
                    flight_position["groundspeed"], flight_position["heading"], flight_position["latitude"],
                    flight_position["longitude"], flight_position["timestamp"], registration]
    flight_route_points.append(flight_point)

# Writes the list to a file in csv format using csv writer
def write(flight_route_points):
    file = open(config.FLIGHT_ROUTE_CSV, "a")
    csvwriter = csv.writer(file)

    for flight_point in flight_route_points:
        csvwriter.writerow(flight_point)

    file.close()


