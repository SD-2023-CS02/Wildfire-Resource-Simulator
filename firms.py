from configparser import ConfigParser
import requests
import re


URL = "https://firms.modaps.eosdis.nasa.gov/api"

SOURCES = set(["LANDSAT_NRT", "MODIS_NRT", "MODIS_SP", "VIIRS_NOAA20_NRT", "VIIRS_SNPP_NRT", "VIIRS_SNPP_SP"])
DATE = re.compile("(19\d\d|20\d\d)[-](0[1-9]|1[0-2])[-](0[1-9]|[12]\d|3[01])")

DATE_SPANS = set(["24h", "48h", "72h", "7d"])
SENSORS = set(["c6.1", "landsat", "suomi-npp-viirs-c2", "noaa-20-viirs-c2"])
REGIONS = set(["usa_contiguous_and_hawaii", "alaska"])


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
        
        url = f"{URL}/country/csv/{self.__key}/{source}/USA/{day_range}"

        # if date: gets data from [date, date + day_range)
        # no date: gets data from [today - (day_range - 1), today]
        if date:
            url += f"/{date}"
        
        res = requests.get(url)
        
        with open(f"{file_name}.csv", "w") as f:
            f.write(res.text)
    

    def write_footprint_data_to_csv(self, file_name: str, date_span: str = "7d", sensor: str = "noaa-20-viirs-c2", region: str = "usa_contiguous_and_hawaii") -> None:
        if date_span not in DATE_SPANS:
            raise ValueError("Invalid date_span")
        if sensor not in SENSORS:
            raise ValueError("Invalid sensor")
        if region not in REGIONS:
            raise ValueError("Invalid region")
        
        # potential area api
        area_url = f"{URL}/kml_fire_footprints/{region}/{date_span}/{sensor}"

        result = requests.get(area_url)

        with open(f"{file_name}.csv", "w") as f:
            f.write(result.text)
