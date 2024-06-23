from configparser import ConfigParser
import mysql.connector as mysql
import json


config = ConfigParser()
config.read('config.ini')

with open('output/fire_to_flights_out.json', 'r') as f:
    fire_to_flights = json.load(f)

with open('output/plane_drops_results.csv', 'w') as f:
    db = mysql.connect(
        user=config['db']['user'],
        password=config['db']['password'],
        database=config['db']['database'],
        host=config['db']['host']
    )
    cursor = db.cursor()

    cursor.execute(f'''
            SELECT fire_id, ROUND(latitude, 2) as latitude, ROUND(longitude, 2) as longitude
            FROM FirePoint
        ''')
    all_fires = cursor.fetchall()
    fire_coords = {}
    
    for fire_id, latitude, longitude in all_fires:
        if fire_id in fire_to_flights:
            fire_coords[fire_id] = (latitude, longitude)
    
    cursor.execute(f'''
        SELECT tail_no, flight_id, flight_timestamp, ROUND(latitude, 2) as latitude, round(longitude, 2) as longitude
        FROM Flight
    ''')
    flights = cursor.fetchall()
    flight_pts = {}
    db.close()

    for fire_id in fire_to_flights:
        for flight_id in fire_to_flights[fire_id]:
            flight_pts[flight_id] = []
    
    for tail_no, flight_id, flight_timestamp, latitude, longitude in flights:
        if flight_id in flight_pts:
            flight_pts[flight_id].append((tail_no, flight_timestamp, latitude, longitude))
    
    f.write('fire_id,tail_no,flight_id,flight_timestamp\n')

    for fire_id in fire_to_flights:
        fire_lat, fire_long = fire_coords[fire_id]

        for flight_id in fire_to_flights[fire_id]:
            for tail_no, timestamp, flight_lat, flight_long in flight_pts[flight_id]:
                if flight_lat == fire_lat and flight_long == fire_long:
                    f.write(f'{fire_id},{tail_no},{flight_id},{timestamp}\n')
                    break
