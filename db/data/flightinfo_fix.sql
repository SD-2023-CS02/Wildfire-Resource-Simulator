# updates the flightinfo take off time with the earliest flight timestamp
# of that flight id. only replaces if the takeoff time in flight info was later
# than the earliest flight timestamp.
UPDATE FlightInfo fi JOIN (
                SELECT MIN(flight_timestamp) AS first, flight_id
				FROM Flight
				GROUP BY flight_id
			) f ON fi.flight_id=f.flight_id
SET fi.takeoff=f.first
WHERE fi.takeoff > f.first;


## updates the flight info landing times with the max flight timestamp
# for that flight_id in the flight table. but only updates if the current landing
# is earlier than the actual landing according to flight
UPDATE FlightInfo fi JOIN (
                SELECT MAX(flight_timestamp) AS last, flight_id
				FROM Flight
				GROUP BY flight_id
			) f ON fi.flight_id=f.flight_id
SET fi.landing=f.last
WHERE fi.landing < f.last;