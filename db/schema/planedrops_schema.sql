CREATE TABLE PlaneDrops (
    fire_id VARCHAR(50),
    tail_no CHAR(6) NOT NULL,
    flight_id VARCHAR(30),
    flight_timestamp DATETIME,
    PRIMARY KEY (fire_id, flight_id, flight_timestamp),
    FOREIGN KEY (tail_no, flight_timestamp) REFERENCES Flight (tail_no, flight_timestamp),
    FOREIGN KEY (flight_id) REFERENCES FlightInfo (flight_id)
);
