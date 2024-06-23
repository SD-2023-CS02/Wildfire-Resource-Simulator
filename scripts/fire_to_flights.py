from configparser import ConfigParser
import mysql.connector as mysql
from datetime import timedelta
import json


config = ConfigParser()
config.read('config.ini')

with open('output/fire_to_flights_out.json', 'w') as f:
    out = {}
    db = mysql.connect(
        user=config['db']['user'],
        password=config['db']['password'],
        database=config['db']['database'],
        host=config['db']['host']
    )
    cursor = db.cursor()

    cursor.execute('''
        SELECT fire_id, discovery_date, containment_date, fireout_date, control_date
        FROM FirePoint
    ''')
    fires = cursor.fetchall()

    cursor.execute('''
        SELECT flight_id, takeoff
        FROM FlightInfo
    ''')
    flights = cursor.fetchall()

    for fire_id, discovery, containment, fireout, control in fires:
        bound = None

        if fireout:
            bound = fireout
        elif control:
            bound = control
        elif containment:
            bound = containment
        else:
            bound = discovery + timedelta(30)
        
        for flight_id, takeoff in flights:
            if discovery <= takeoff <= bound:
                if fire_id not in out:
                    out[fire_id] = []
                
                out[fire_id].append(flight_id)

    db.close()
    json.dump(out, f, indent=2)
