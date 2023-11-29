# Test methods must begin with test_
import pytest
from firms import *


FOLDER = "test_output"


def test_valid_columns():
    cols = "country_id,latitude,longitude,path,row,scan,track,acq_date,acq_time,satellite,confidence,daynight"
    file_name = "firms_test"

    firms = FIRMS()
    firms.write_data_to_csv(file_name)

    with open(f"{FOLDER}/{file_name}.csv", "r") as f:
        output = f.read()
    
    assert output == cols
