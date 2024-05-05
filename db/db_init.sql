-- Master file for populating the database
-- Tables:
SOURCE fire_schema.sql;
SOURCE tankerbase_schema.sql; -- tankerbase_schema_local.sql

SOURCE airtanker_schema.sql;
SOURCE fireplane_schema.sql;
SOURCE flightinfo_schema.sql;
SOURCE flight_schema.sql;

SOURCE basefireproximity_schema.sql;
SOURCE planedrops_schema.sql;
SOURCE suppressionstats_schema.sql;

-- Views:
SOURCE plane_grounded.sql;
SOURCE plane_hours.sql;
SOURCE response_time.sql;
SOURCE tankerbase_visits.sql;

-- Inserts:
SOURCE fire_data.sql;
SOURCE tankerbase_data.sql; -- tankerbase_data_local.sql

SOURCE airtanker_data.sql;
SOURCE fireplane_data.sql;
SOURCE flightinfo_data.sql;

SOURCE flight_data1.sql;
SOURCE flight_data2.sql;
SOURCE flight_data3.sql;
SOURCE flight_data4.sql;
SOURCE flight_data5.sql;
SOURCE flight_data6.sql;

SOURCE flightinfo_fix.sql;

SOURCE basefireproximity_data.sql;
SOURCE planedrops_data.sql;
SOURCE suppressionstats_data.sql;
