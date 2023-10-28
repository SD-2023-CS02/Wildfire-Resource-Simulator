from configparser import ConfigParser
import requests
import re


SOURCES = set(["LANDSAT_NRT", "MODIS_NRT", "MODIS_SP", "VIIRS_NOAA20_NRT", "VIIRS_SNPP_NRT", "VIIRS_SNPP_SP"])
DATE = re.compile("(19\d\d|20\d\d)[-](0[1-9]|1[0-2])[-](0[1-9]|[12]\d|3[01])")


class FIRMS:
    def __init__(self, config_file: str = "config.ini") -> None:
        config = ConfigParser()
        config.read(config_file)
        self.__key = config["API"]["MapKey"]
    
    
    def write_data_to_csv(self, file_name: str, date: str = "", day_range: int = 1, source: str = "LANDSAT_NRT") -> None:
        if date and not DATE.match(date):
            raise ValueError("date not in YYYY-MM-DD format")
        if not (1 <= day_range <= 10):
            raise ValueError("day_range must be between 1 and 10")
        if source not in SOURCES:
            raise ValueError("Invalid satellite source")
        
        url = f"https://firms.modaps.eosdis.nasa.gov/api/country/csv/{self.__key}/{source}/USA/{day_range}"

        # if date: gets data from [date, date + day_range)
        # no date: gets data from [today - (day_range - 1), today]
        if date:
            url += f"/{date}"
        
        res = requests.get(url)
        
        with open(f"{file_name}.csv", "w") as f:
            f.write(res.text)
    
    def write_footprint_data_to_csv(self, file_name: str):
        #potential area api
        area_url = "/api/kml_fire_footprints/?region=usa_contiguous_and_hawaii&date_span=7d&sensor=noaa-20-viirs-c2"

        result = requests.get(area_url)
        with open(f"{file_name}.csv", "w") as f:
            f.write(result.text)