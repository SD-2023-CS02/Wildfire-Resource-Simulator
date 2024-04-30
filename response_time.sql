CREATE VIEW ResponseTime AS
SELECT flight_id, fire_id, discovery_date, takeoff, TIMEDIFF(takeoff, discovery_date) AS response_time
FROM (SELECT DISTINCT fire_id, flight_id FROM PlaneDrops) s
    JOIN FirePoint USING (fire_id)
    JOIN FlightInfo USING (flight_id)
ORDER BY discovery_date;
