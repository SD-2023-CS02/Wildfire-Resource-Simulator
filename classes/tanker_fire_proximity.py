import pandas as pd
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
        # self.clean_tanker_lat_long()
        for _, fire in self.fire_locations.iterrows():
            fire_lat_long = (float(fire['latitude']), float(fire['longitude']))
            distances = []
            for _, tanker in self.tanker_locations.iterrows():
                tanker_lat_long = (tanker['latitude'], tanker['longitude'])
                distances.append(haversine(fire_lat_long, tanker_lat_long, unit=Unit.MILES))
            tanker_idx = (distances.index(min(distances)))
            distance = min(distances)

            self.tanker_locations.at[tanker_idx, 'proximity'] += distance
            self.tanker_locations.at[tanker_idx, 'close_fires_count'] += 1

    def average(self):
        """
        Calculates the average proximity by dividing the value in the proximity attribute by the number in the closefires attribute
        """
        zero_count = 0
        for index, row in self.tanker_locations.iterrows():
            if row['close_fires_count'] != 0:
                self.tanker_locations.at[index, 'proximity'] /= row['close_fires_count']
            if row['close_fires_count'] != 0:
                zero_count += 1
        print(self.tanker_locations[['base_name', 'proximity']])
        print("zero count: " + str(zero_count))