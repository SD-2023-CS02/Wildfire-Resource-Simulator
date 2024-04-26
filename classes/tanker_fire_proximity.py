import pandas as pd
import numpy as np
from haversine import haversine, Unit
# NOTE: must >>pip install haversine<< to run this code

class ProximityCalculator:
    def load_data(self, fires, tankers):
        self.fire_locations = fires
        self.tanker_locations = tankers
        self.tanker_locations['proximity'] = 0.0
        self.tanker_locations['close_fires_count'] = 0

    # def clean_tanker_lat_long(self):
    #     """
    #     Ideally this would be in a cleaning notebook, but we didn't realize it'd be an issue til just now
    #     """
    #     # a lambda that converts from degree decimal minutes to degree decimal
    #     ddm_to_dd = lambda ddm: int(ddm.split()[0]) + float(ddm.split()[1]) / 60

    #     # Apply the conversion function to the 'Latitude' and 'Longitude' columns
    #     self.tanker_locations['Latitude'] = self.tanker_locations['Latitude'].apply(lambda x: ddm_to_dd(x[:-1]) if x[-1].isalpha() else ddm_to_dd(x))
    #     self.tanker_locations['Longitude'] = self.tanker_locations['Longitude'].apply(lambda x: -1 * ddm_to_dd(x[:-1]) if x[-1].isalpha() else -1 * ddm_to_dd(x))

    def fire_distances(self):
        """
        Calculates the distance between each fire and each of the tanker bases. Chooses the shortest and adds that distance
        to the value in the Proximity attribute for that tanker base. Adds one to the CloseFires attribute
        """
        # print(len(self.fire_locations))
        # # self.clean_tanker_lat_long()
        # fire_count = 0
        # for _, fire in self.fire_locations.iterrows():
        #     fire_count += 1
        #     if fire_count%100 == 0:
        #         print("count: " + str(fire_count))
        #     fire_lat_long = (float(fire['latitude']), float(fire['longitude']))
        #     distances = []
        #     # print("fire: " + str(fire))
        #     # num_tankers = 0
        #     for _, tanker in self.tanker_locations.iterrows():
        #         tanker_lat_long = (tanker['latitude'], tanker['longitude'])
        #         # print("tanker: " + str(tanker) + "num tankers: " + num_tankers)
        #         # num_tankers += 1
        #         distances.append(haversine(fire_lat_long, tanker_lat_long, unit=Unit.MILES))
        #     # print("num tankers: " + str(num_tankers))
        #     tanker_idx = (distances.index(min(distances)))
        #     distance = min(distances)
        #     # print(str(min(distances)))
        #     self.tanker_locations.at[tanker_idx, 'proximity'] += distance
        #     self.tanker_locations.at[tanker_idx, 'close_fires_count'] += 1
        # print("done")
        fire_latitudes = self.fire_locations['latitude'].values
        fire_longitudes = self.fire_locations['longitude'].values
        tanker_latitudes = self.tanker_locations['latitude'].values
        tanker_longitudes = self.tanker_locations['longitude'].values
        
        distances = np.zeros((len(fire_latitudes), len(tanker_latitudes)))
        print('starting nested loops')
        fire_count = 0
        for i, (fire_lat, fire_long) in enumerate(zip(fire_latitudes, fire_longitudes)):
            fire_count += 1
            if fire_count%10000 == 0:
                print("count: " + str(fire_count))
            for j, (tanker_lat, tanker_long) in enumerate(zip(tanker_latitudes, tanker_longitudes)):
                distances[i, j] = haversine((fire_lat, fire_long), (tanker_lat, tanker_long), unit=Unit.MILES)
        print('done calculating distances')
        closest_tanker_indices = np.argmin(distances, axis=1)
        min_distances = np.min(distances, axis=1)
        
        self.tanker_locations['proximity'] += np.bincount(closest_tanker_indices, weights=min_distances, minlength=len(self.tanker_locations))
        self.tanker_locations['close_fires_count'] += np.bincount(closest_tanker_indices, minlength=len(self.tanker_locations))

    def average(self):
        """
        Calculates the average proximity by dividing the value in the proximity attribute by the number in the closefires attribute
        """
        zero_count = 0
        for index, row in self.tanker_locations.iterrows():
            if row['close_fires_count'] != 0:
                self.tanker_locations.at[index, 'proximity'] /= row['close_fires_count']
            if row['close_fires_count'] == 0:
                zero_count += 1
        print(self.tanker_locations[['base_name', 'proximity']])
        print("zero count: " + str(zero_count))