import numpy as np
from haversine import haversine, Unit
# NOTE: must >>pip install haversine<< to run this code

class ProximityCalculator:
    def load_data(self, fires, tankers):
        """
        Stores the dataframes that are passed in as input. Creates columns for proximity (initially the sum of all closest
        distances and ultimately the average distance of closest fires) and close_fires_count (the number of fires whose
        closest tanker is the given one)

        Args:
            fires: a dataframe containing the latitude and longitude of fires
            tankers: a dataframe containing the latitude, longitude, and base name of tanker bases
        """
        self.fire_locations = fires
        self.tanker_locations = tankers
        self.tanker_locations['proximity'] = 0.0
        self.tanker_locations['close_fires_count'] = 0

    def fire_distances(self):
        """
        Calculates the distance between each fire and each of the tanker bases. Chooses the shortest and adds that distance
        to the value in the proximity attribute for that tanker base. Adds one to the close_fires_count attribute
        """
        # extract latitude and longitude values for fires and tankers
        fire_latitudes = self.fire_locations['latitude'].values
        fire_longitudes = self.fire_locations['longitude'].values
        tanker_latitudes = self.tanker_locations['latitude'].values
        tanker_longitudes = self.tanker_locations['longitude'].values
        
        # create a 2D array and calculate distances between each fire-tanker base pair
        distances = np.zeros((len(fire_latitudes), len(tanker_latitudes)))
        for i, (fire_lat, fire_long) in enumerate(zip(fire_latitudes, fire_longitudes)):
            for j, (tanker_lat, tanker_long) in enumerate(zip(tanker_latitudes, tanker_longitudes)):
                distances[i, j] = haversine((fire_lat, fire_long), (tanker_lat, tanker_long), unit=Unit.MILES)
        
        # for each fire, store the index of the tanker with the shortest distance. Store that shortest distance
        closest_tanker_indices = np.argmin(distances, axis=1)
        min_distances = np.min(distances, axis=1)

        # for each tanker, add all the distances of the closest fires to proximity. Add a count of the number of closest fires to close_fires_count
        self.tanker_locations['proximity'] += np.bincount(closest_tanker_indices, weights=min_distances, minlength=len(self.tanker_locations))
        self.tanker_locations['close_fires_count'] += np.bincount(closest_tanker_indices, minlength=len(self.tanker_locations))

    def average(self):
        """
        Calculates the average proximity by dividing the value in the proximity attribute by the number in the closefires attribute
        """
        for index, row in self.tanker_locations.iterrows():
            # make sure we're not trying to divide by zero
            if row['close_fires_count'] != 0:
                self.tanker_locations.at[index, 'proximity'] /= row['close_fires_count']
        print(self.tanker_locations[['base_name', 'proximity']])

        self.tanker_locations[['base_code', 'proximity']].to_csv('output/base_fire_proximity.csv', index=False)
