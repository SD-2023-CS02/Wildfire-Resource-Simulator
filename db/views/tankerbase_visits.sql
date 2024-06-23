CREATE VIEW TankerBaseVisits AS
SELECT DISTINCT f.flight_id, f.tail_no, t.base_code
FROM Flight f CROSS JOIN TankerBase t
WHERE ROUND(f.latitude, 1) = ROUND(t.latitude, 1) AND ROUND(f.longitude, 1) = ROUND(t.longitude, 1);
