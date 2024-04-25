from configparser import ConfigParser
import mysql.connector as mysql
import pandas as pd

def connect_to_db():
    config = ConfigParser()
    config.read('../config.ini')

    db = mysql.connect(
        user=config['db']['user'],
        password=config['db']['password'],
        database=config['db']['database'],
        host=config['db']['host']
    )
    cursor = db.cursor()

    cursor.execute('SELECT base_name, latitude, longitude FROM TankerBase')
    bases = cursor.fetchall()

    base_arr = []

    for name, lat, long in bases:
        base_arr.append([name, lat, long])

    base_df = pd.DataFrame(base_arr, columns=['base_name', 'latitude', 'longitude'])

    cursor.execute('SELECT latitude, longitude FROM FirePoint')
    fires = cursor.fetchall()
    db.close()

    fire_arr = []

    for lat, long in fires:
        fire_arr.append([lat, long])

    fire_df = pd.DataFrame(fire_arr, columns=['latitude', 'longitude'])
    return base_df, fire_df
