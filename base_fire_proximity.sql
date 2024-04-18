SELECT fire_id, base_code
FROM (
    SELECT f.fire_id, t.base_code, ST_Distance_Sphere(
        POINT(f.longitude, f.latitude), POINT(t.longitude, t.latitude)
    ) as distance
    FROM TankerBase t CROSS JOIN FirePoint f
) d
