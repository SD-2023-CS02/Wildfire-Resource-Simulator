CREATE VIEW plane_grounded AS
SELECT 8760 - SUM(t.total_hours) AS year_spent_grounded, ((8760 - SUM(t.total_hours))/8760)*100 AS percentage_spent_grounded, SUM(t.total_hours)- 285.409356409615 AS diff_over_avg, t.tail_no, YEAR(takeoff) AS year
FROM (
    SELECT *, TIME_TO_SEC(TIMEDIFF(f.landing,f.takeoff))/3600 AS total_hours
    FROM (
        SELECT MAX(flight_timestamp) AS landing, MIN(flight_timestamp) AS takeoff, flight_id, tail_no
        FROM Flight
        GROUP BY flight_id, tail_no
    ) f
      ) t
GROUP BY YEAR(takeoff), t.tail_no
ORDER BY t.tail_no, YEAR(takeoff);
