-- Cleanup
DROP TABLE IF EXISTS FirePoint;

-- Create Tables
CREATE TABLE FirePoint (
    create_date DATETIME,
    latitude DECIMAL(16, 13),
    longitude DECIMAL(16, 13),
    -- Non-Key Fire Data
    containment_date DATETIME,
    fireout_date DATETIME,
    discovery_acres FLOAT(9,3),
    incident_size_acres FLOAT(9, 3),
    PRIMARY KEY (create_date, latitude, longitude)
);
