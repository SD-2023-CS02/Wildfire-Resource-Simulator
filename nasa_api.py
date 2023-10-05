import requests


key = ""
area = "world"
source = "LANDSAT_NRT"
day_range = 1

url = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{key}/{source}/{area}/{day_range}"
res = requests.get(url)

print(res.text)
