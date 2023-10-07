from configparser import ConfigParser
import requests


config = ConfigParser()
config.read("config.ini")

key = config["API"]["MapKey"]
area = "world"
source = "LANDSAT_NRT"
day_range = 2

url = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{key}/{source}/{area}/{day_range}"
res = requests.get(url)

res_list = res.text.split("\n")

for row in res_list[:3]:
    print(row)
