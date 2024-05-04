CREATE TABLE FirePlane (
    tail_no CHAR(6),
    tanker_type VARCHAR(20) NOT NULL,
    contractor VARCHAR(50),
    PRIMARY KEY (tail_no),
    FOREIGN KEY (tanker_type) REFERENCES AirTanker (tanker_type)
);
