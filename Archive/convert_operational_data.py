import geopandas as gpd
import time as t

year = input("Provide input year for converting data (2020, 2021): ")
gdb = './data/Public_EventDataArchive_'+ year + '.gdb'

start_time = t.time

print('\nOpening gdb, Please wait...\n')

# Read gdb data (May take awhile)
fc = gpd.read_file(gdb, engine='fiona')

print('Converting to CSV, Please wait...\n')

# Write to CSV 
fc.to_csv('./output/output_op_data_' + year + '.csv')

print('Converting to GeoJSON, Please wait...\n')

# Write to GeoJSON
fc.to_file('./output/op_data_' + year + '.geojson', driver='GeoJSON')

# Job Runtime
end_time = t.time
total_runtime = end_time - start_time
print('Total Runtime:', total_runtime)