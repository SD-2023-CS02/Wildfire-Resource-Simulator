# Will select the first instance of each unique flight ID from flight_excess.csv,
# may result in incorrect source/destination values
import pandas as pd


flight_df = pd.read_csv('output/flight_route_locations.csv')
flight_ids = set(flight_df['flight_id'])

excess_df = pd.read_csv('output/flight_excess.csv')
excess_df.drop_duplicates(subset=['flight_id'], inplace=True)
excess_df = excess_df[excess_df['flight_id'].isin(flight_ids)]
excess_df['takeoff'] = '2000-01-01 00:00:00'
excess_df['landing'] = '2000-01-01 00:00:00'
excess_df.to_csv('output/flight_results.csv', index=False)
