-- Master file for populating a local database (SQLite)
-- Tables:
.read schema/fire_schema.sql
.read schema/tankerbase_schema_local.sql

.read schema/airtanker_schema.sql
.read schema/fireplane_schema.sql
.read schema/flightinfo_schema.sql
.read schema/flight_schema_local.sql

.read schema/basefireproximity_schema.sql
.read schema/planedrops_schema.sql
.read schema/suppressionstats_schema.sql

-- Views:
.read views/plane_grounded.sql
.read views/plane_hours.sql
.read views/response_time.sql
.read views/tankerbase_visits.sql

-- Inserts:
.read data/fire_data.sql
.read data/tankerbase_data_local.sql

.read data/airtanker_data.sql
.read data/fireplane_data.sql
.read data/flightinfo_data.sql

.read data/flight_data1.sql
.read data/flight_data2.sql
.read data/flight_data3.sql
.read data/flight_data4.sql
.read data/flight_data5.sql
.read data/flight_data6.sql

-- WARNING: May take serveral hours to run this
.read scripts/flightinfo_update_local.sql
