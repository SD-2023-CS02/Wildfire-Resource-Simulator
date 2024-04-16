from configparser import ConfigParser
import mysql.connector as mysql
from datetime import timedelta
import json


config = ConfigParser()
config.read('config.ini')


with open('output/tankerbase_visits.csv', 'w') as f:
    db = mysql.connect(
        user=config['db']['user'],
        password=config['db']['password'],
        database=config['db']['database'],
        host=config['db']['host']
    )
    cursor = db.cursor()
