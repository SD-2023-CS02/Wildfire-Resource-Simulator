from firms import *
from breezometer_test import *


firms = FIRMS()
firms.write_data_to_csv("firms_columns")
firms.write_footprint_data_to_csv("firms_footprint")

breezometer = BREEZE()
breezometer.write_wildfire_api("breezometer_areas")
