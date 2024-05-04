CREATE TABLE SuppressionStats (
    fire_id VARCHAR(50),
    hours_burned FLOAT(12, 3) NOT NULL,
    normalized_time FLOAT(12, 3) NOT NULL,
    normalized_acres FLOAT(12, 3) NOT NULL,
    suppression_result FLOAT(12, 3) NOT NULL,
    has_plane_drop BOOLEAN NOT NULL,
    PRIMARY KEY (fire_id),
    FOREIGN KEY (fire_id) REFERENCES FirePoint (fire_id)
);
