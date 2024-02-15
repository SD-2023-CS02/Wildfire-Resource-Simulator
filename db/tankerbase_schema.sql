DROP TABLE IF EXISTS TankerBase;

CREATE TABLE TankerBase (
    base_code CHAR(3),
    base_name VARCHAR(50) NOT NULL,
    airport VARCHAR(50) NOT NULL,
    region VARCHAR(50) NOT NULL,
    elevation INT UNSIGNED NOT NULL, -- ft
    latitude DECIMAL(16, 13) NOT NULL,
    longitude DECIMAL(16, 13) NOT NULL,
    -- Runway Weight Limits (tons)
    single_rwl FLOAT NOT NULL,
    double_rwl FLOAT NOT NULL,
    2s_rwl FLOAT NOT NULL,
    2d_rwl FLOAT NOT NULL,
    -- Allowed Plane Types
    vlat ENUM('YES', 'NO') NOT NULL,
    lat ENUM('YES', 'NO') NOT NULL,
    seat ENUM('YES', 'NO') NOT NULL,
    -- Misc
    maffs ENUM('YES', 'NO', 'R', 'H', 'F', 'R/H/F', 'R/H', 'H/F', 'R/F') NOT NULL,
    hot_load ENUM('YES', 'NO') NOT NULL,
    fuel_load ENUM('YES', 'NO') NOT NULL,
    hot_refuel ENUM('YES', 'NO') NOT NULL,
    retardant_type ENUM('NONE', 'LC 95A', 'MVP FX', 'P-100') NOT NULL,
    pit_total INT UNSIGNED NOT NULL,
    parking_total INT UNSIGNED NOT NULL,
    load_simul INT UNSIGNED NOT NULL,
    offload_capacity INT UNSIGNED NOT NULL, -- gallons
    -- Keys
    PRIMARY KEY (base_code)
);
