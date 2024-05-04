# Author: DBog
# Date: 2/5/2024
# Purpose: Parses the json to get all the fa_flight_id's from the given 7 day period
#           and writes to a file
# Output: fa_flight_ids.csv list of all fa_flight_ids

# Vocab:
# fa_flight_id - FlightAwares Single Flight ID. Needed for flights.

# runs the program.
import csv
import config


def run(jsonDict, tail_num):
    fa_flight_id_list = []
    flights_list = jsonDict["flights"]
    flight_excess = []
    for flight in flights_list:
        add(flight["fa_flight_id"], tail_num, fa_flight_id_list)
        add_excess(flight, flight_excess)
        # currently only adds fa_flight_id's. considering more attributes to add
    write(fa_flight_id_list)
    write_excess(flight_excess)

# seperate function created to add the fa_flight_id to the list in the event
# that we take more information instead of just the fa_flight_id in the future
# and need multiple lists. Contains it all in one place
def add(fa_flight_id, tail_num, fa_flight_id_list):
    fa_flight_id_list.append([fa_flight_id, tail_num])

def add_excess(flight, flight_excess):
    if flight["origin"] is not None:
        origin = flight["origin"]["code_iata"]
    else:
        origin = ""
    if flight["destination"] is not None:
        dest = flight["destination"]["code_iata"]
    else:
        dest = ""
    flight_excess.append([flight["fa_flight_id"], origin, dest, flight["actual_off"], flight["actual_on"]])

# run after all the fa_flight_ids are found.
def write(fa_flight_id_list):
    file = open(config.FLIGHT_ID_CSV, "a")

    csvwriter = csv.writer(file)
    for fa_flight_id in fa_flight_id_list:
        csvwriter.writerow(fa_flight_id)

    file.close()

def write_excess(flight_excess):
    file = open(config.FLIGHT_EXCESS_CSV, "a")

    csvwriter = csv.writer(file)
    for excess_data in flight_excess:
        csvwriter.writerow(excess_data)

    file.close()