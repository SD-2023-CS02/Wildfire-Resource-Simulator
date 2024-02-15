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
    discovery_acres FLOAT(12,3),
    incident_size_acres FLOAT(12, 3),
    PRIMARY KEY (create_date, latitude, longitude)
);

CREATE TABLE FirePoint (
    fire_id VARCHAR(50),
    incident_name VARCHAR(50) NOT NULL,
    gacc VARCHAR(10) NOT NULL,
    create_date DATETIME NOT NULL,
    latitude DECIMAL(16, 13) NOT NULL,
    longitude DECIMAL(16, 13) NOT NULL,
    -- Optional Location Data
    initial_lat DECIMAL(16, 13),
    initial_long DECIMAL(16, 13),
    -- Optional Time Data
    containment_date DATETIME,
    fireout_date DATETIME,
    control_date DATETIME,
    discovery_date DATETIME,
    response_date DATETIME,
    -- Optional Acre Data
    discovery_acres FLOAT(12,3),
    incident_size_acres FLOAT(12, 3),
    final_acres FLOAT(12, 3),
    initial_acres FLOAT(12, 3),
    -- Table Keys
    PRIMARY KEY (fire_id)
);
