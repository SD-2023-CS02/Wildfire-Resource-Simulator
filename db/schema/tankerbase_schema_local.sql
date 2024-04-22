CREATE TABLE TankerBase (
    base_code CHAR(3), -- FAA ID
    base_name VARCHAR(50) NOT NULL,
    airport VARCHAR(50) NOT NULL,
    region VARCHAR(50) NOT NULL,
    elevation INT UNSIGNED NOT NULL, -- ft
    latitude DECIMAL(16, 13) NOT NULL,
    longitude DECIMAL(16, 13) NOT NULL,
    -- Runway Weight Limits (tons)
    single_rwl FLOAT NOT NULL,
    double_rwl FLOAT NOT NULL,
    s_rwl FLOAT NOT NULL,
    d_rwl FLOAT NOT NULL,
    -- Allowed Airtanker Types
    vlat TEXT CHECK(vlat IN ('YES', 'NO')) NOT NULL, -- very large
    lat TEXT CHECK(lat IN ('YES', 'NO')) NOT NULL, -- large
    seat TEXT CHECK(seat IN ('YES', 'NO')) NOT NULL, -- single engine
    -- Misc
    maffs TEXT CHECK(maffs IN ('YES', 'NO', 'R', 'H', 'F', 'R/H/F', 'R/H', 'H/F', 'R/F')) NOT NULL,
    hot_load TEXT CHECK(hot_load IN ('YES', 'NO')) NOT NULL,
    fuel_load TEXT CHECK(fuel_load IN ('YES', 'NO')) NOT NULL,
    hot_refuel TEXT CHECK(hot_refuel IN ('YES', 'NO')) NOT NULL,
    retardant_type TEXT CHECK(retardant_type IN ('NONE', 'LC 95A', 'MVP FX', 'P-100')) NOT NULL,
    pit_total INT UNSIGNED NOT NULL,
    parking_total INT UNSIGNED NOT NULL,
    load_simul INT UNSIGNED NOT NULL,
    offload_capacity INT UNSIGNED NOT NULL, -- gallons
    -- Keys
    PRIMARY KEY (base_code)
);
