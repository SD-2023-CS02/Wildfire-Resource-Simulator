# from firms import *
from breeze import *
from directory_parser import *


# firms = FIRMS()
# firms.write_data_to_csv("firms_columns")
# firms.write_footprint_data_to_kml("firms_footprint")

# breezometer = BREEZE()
# breezometer.write_wildfire_api("breezometer_areas")

parser = DirectoryParser()
parser.parse_directory("output", "elements.txt")
parser.write_csv("tanker_bases.csv")
