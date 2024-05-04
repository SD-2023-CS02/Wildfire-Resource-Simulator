CREATE TABLE FlightInfo (
    flight_id VARCHAR(30),
    source VARCHAR(3),
    destination VARCHAR(3),
    takeoff DATETIME NOT NULL,
    landing DATETIME NOT NULL,
    PRIMARY KEY (flight_id)
);
