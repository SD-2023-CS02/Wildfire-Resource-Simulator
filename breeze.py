from configparser import ConfigParser
import requests


FOLDER = "test_output"


class BREEZE:
    def __init__(self, config_file: str = "config.ini") -> None:
        config = ConfigParser()
        config.read(config_file)
        self.__key = config["API"]["GoogleKey"]


    # radius is in km, min 5, max 100
    # the latitude and longitude values I arbitrarily chose are for Boulder, CO
    def write_wildfire_api(self, file_name: str, lat = 40, lon = 105, radius = 100):
        area_url = f"https://api.breezometer.com/fires/v1/burnt-area?key={self.__key}&lat={lat}&lon={lon}&radius={radius}&daysFromExtinguish={360}"

        result = requests.get(area_url)

        with open(f"{FOLDER}/{file_name}.json", "w", errors="ignore") as f:
            f.write(result.text)
