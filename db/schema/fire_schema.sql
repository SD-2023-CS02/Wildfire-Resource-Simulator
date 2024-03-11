CREATE TABLE FirePoint (
    fire_id VARCHAR(50),
    incident_name VARCHAR(50) NOT NULL,
    create_date DATETIME NOT NULL,
    discovery_date DATETIME NOT NULL,
    latitude DECIMAL(16, 13) NOT NULL,
    longitude DECIMAL(16, 13) NOT NULL,
    -- Optional Location Data
    initial_lat DECIMAL(16, 13),
    initial_long DECIMAL(16, 13),
    gacc VARCHAR(10),
    -- Optional Time Data
    containment_date DATETIME,
    fireout_date DATETIME,
    control_date DATETIME,
    -- Optional Acre Data
    discovery_acres FLOAT(12,3),
    incident_size_acres FLOAT(12, 3),
    final_acres FLOAT(12, 3),
    initial_acres FLOAT(12, 3),
    -- Table Keys
    PRIMARY KEY (fire_id)
);
