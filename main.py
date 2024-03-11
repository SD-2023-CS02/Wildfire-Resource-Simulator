# from firms import *
from breeze import *


# firms = FIRMS()
# firms.write_data_to_csv("firms_columns")
# firms.write_footprint_data_to_kml("firms_footprint")

breezometer = BREEZE()
breezometer.write_wildfire_api("breezometer_areas")
