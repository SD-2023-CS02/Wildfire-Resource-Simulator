from firms import *
from breeze import *
from directory_parser import *


# firms = FIRMS()
# firms.write_data_to_csv("firms_columns")
# firms.write_footprint_data_to_kml("firms_footprint")

# breezometer = BREEZE()
# breezometer.write_wildfire_api("breezometer_areas")

parser = DirectoryParser("data/air_tanker_base_directory.pdf")
parser.parse_directory()
