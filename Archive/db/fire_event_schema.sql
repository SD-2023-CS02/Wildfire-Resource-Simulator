DROP TABLE IF EXISTS FireEvent;

CREATE TABLE FireEvent (
    id INT UNSIGNED AUTO_INCREMENT, -- surrogate key
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY (start_time, end_time)
);
