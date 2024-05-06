# Python Dependences
* pandas
* numpy
* mysql.connector
* haversine

# Configuration Files
The following instructions are to be done **in order**.
## FlightLibrary
* Place FlightAware AeroAPI key in `/flightlibrary/config.py`
* Set dates and cost thresholds in `config.py` as well
## Database Querying
* Create a file called `config.ini` in the root folder
* Template off of `example_config.ini`
* No surrounding quotes required for files in `config.ini`

# Fire Data
1. Ensure downloaded NIFC Wildland Fire Incident Locations dataset is located at `/data/Wildland_Fire_Incident_Locations.csv`
1. Open `/notebooks/Fire_Data_Cleaning.ipynb` and run all cells to generate cleaned fire data in output

# Flight Data
1. After configuring the FlightLibrary `config.py`, run `/flightlibrary/engine.py`
1. The library modules should create `fa_flight_ids.csv`, `flight_excess.csv`, and `flight_route_locations.csv` in output
1. Run `/scripts/flight_results.py` to create `flight_results.csv` in output
* NOTE: `flight_results.csv` contains dummy date-timestamps that will be replaced during table population in the datbase

# Database Creation
1. Run `fire_inserts.py`, `fireplane_inserts.py`, `flight_inserts.py`, `flightinfo_inserts.py`, and `tankerbase_inserts.py` (or `tankerbase_inserts_local.py`) in `/db/scripts`
1. If the database is hosted remotely, transfer the `/db` folder onto the server; if hosted locally, open the database instance in the `/db` folder
1. Execute `db_init.sql` (for remote) or `db_init_local.sql` (for local) using the `SOURCE <file>` or `.read <file>` commands respectively
## Generating Statistics
1. After configuring the database `config.ini`, run `/scripts/main.py`, `/scripts/fire_to_flights.py`, and `/scripts/plane_drops` in sequence (the latter 2 take long to complete based on the size of the data)
1. Run all cells in `/notebooks/Drops_vs_Suppression.ipynb` and `/notebooks/Fire_Suppression_Results.ipynb` in sequence
1. Run `basefireproximity_inserts.py`, `planedrops_inserts.py`, and `suppressionstats_inserts.py` in `/db/scripts`
1. Execute `stats.sql` or `stats_local.sql` in `/db` to populate the statistical tables in the database
