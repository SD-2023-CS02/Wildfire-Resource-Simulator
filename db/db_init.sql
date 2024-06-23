-- Master file for populating a remote database (MySQL)
-- Tables:
SOURCE schema/fire_schema.sql
SOURCE schema/tankerbase_schema.sql

SOURCE schema/airtanker_schema.sql
SOURCE schema/fireplane_schema.sql
SOURCE schema/flightinfo_schema.sql
SOURCE schema/flight_schema.sql

SOURCE schema/basefireproximity_schema.sql
SOURCE schema/planedrops_schema.sql
SOURCE schema/suppressionstats_schema.sql

-- Views:
SOURCE views/plane_grounded.sql
SOURCE views/plane_hours.sql
SOURCE views/response_time.sql
SOURCE views/tankerbase_visits.sql

-- Inserts:
SOURCE data/fire_data.sql
SOURCE data/tankerbase_data.sql

SOURCE data/airtanker_data.sql
SOURCE data/fireplane_data.sql
SOURCE data/flightinfo_data.sql

SOURCE data/flight_data1.sql
SOURCE data/flight_data2.sql
SOURCE data/flight_data3.sql
SOURCE data/flight_data4.sql
SOURCE data/flight_data5.sql
SOURCE data/flight_data6.sql

SOURCE scripts/flightinfo_update.sql
