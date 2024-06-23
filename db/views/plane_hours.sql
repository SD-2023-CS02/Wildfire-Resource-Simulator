CREATE VIEW PlaneHours AS
SELECT SUM(t.total_hours)/COUNT(DISTINCT YEAR(takeoff)) AS monthly_avg, t.tail_no, MONTH(takeoff) AS month, SUM(t.total_hours) AS total_hours
FROM (
    SELECT *, TIME_TO_SEC(TIMEDIFF(f.landing,f.takeoff))/3600 AS total_hours
    FROM (
        SELECT MAX(flight_timestamp) AS landing, MIN(flight_timestamp) AS takeoff, flight_id, tail_no
        FROM Flight
        GROUP BY flight_id, tail_no
    ) f
      ) t
GROUP BY MONTH(takeoff), t.tail_no
ORDER BY t.tail_no, MONTH(takeoff);
