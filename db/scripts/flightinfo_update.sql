-- updating the takeoff for flights in the flightinfo table
UPDATE fi 
SET fi.takeoff=f.first 
FROM FlightInfo fi JOIN (
                SELECT MIN(flight_timestamp) AS first, flight_id
                FROM Flight
                GROUP BY flight_id
            ) f ON fi.flight_id=f.flight_id
WHERE fi.takeoff > f.first;

-- updating the landing for flights in the flightinfo table
UPDATE fi
SET
    fi.landing=f.last
FROM FlightInfo fi JOIN (
                SELECT MAX(flight_timestamp) AS last, flight_id 
                FROM Flight
                GROUP BY flight_id
            ) f
WHERE fi.landing > f.last;
