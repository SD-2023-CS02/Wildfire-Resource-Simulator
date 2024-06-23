CREATE TABLE Flight (
    tail_no CHAR(6),
    flight_id VARCHAR(30) NOT NULL,
    flight_timestamp DATETIME,
    latitude DECIMAL(16, 13) NOT NULL,
    longitude DECIMAL(16, 13) NOT NULL,
    altitude DECIMAL(16, 4) NOT NULL,
    altitude_change ENUM('C', 'D', '-'),
    ground_speed INT UNSIGNED NOT NULL,
    heading INT UNSIGNED NOT NULL,
    PRIMARY KEY (tail_no, flight_timestamp),
    FOREIGN KEY (flight_id) REFERENCES FlightInfo (flight_id),
    FOREIGN KEY (tail_no) REFERENCES FirePlane (tail_no)
);
