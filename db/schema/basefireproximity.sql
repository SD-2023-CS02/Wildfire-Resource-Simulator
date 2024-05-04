CREATE TABLE BaseFireProximity (
    base_code CHAR(3),
    avg_proximity FLOAT(12,3) NOT NULL,
    PRIMARY KEY (base_code),
    FOREIGN KEY (base_code) REFERENCES TankerBase (base_code)
);
