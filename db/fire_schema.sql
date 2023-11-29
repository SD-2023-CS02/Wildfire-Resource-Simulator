-- Cleanup
DROP TABLE IF EXISTS FirePoint;

-- Create Tables
CREATE TABLE FirePoint (
    create_date DATETIME,
    latitude DECIMAL(16, 13),
    longitude DECIMAL(16, 13),
    PRIMARY KEY (create_date, latitude, longitude)
);
