# This script will read in the parsed tanker base data from the pdf and
# output a MySQL script to insert rows into the TankerBase table
import pandas as pd


IN_FOLDER = 'data'
IN_FILE = 'tankerbases'

OUT_FOLDER = 'db'
OUT_FILE = 'tankerbase_data'

TABLE = 'TankerBase'


def convert_coord(coord):
    '''
    Use on latitude / longitude coordinates from
    degrees & degree minutes to decimal degrees
    '''
    coord = coord.strip()
    coord = coord[:-1].strip() if coord[-1] in ['N', 'W'] else coord
    deg, deg_min = coord.split()

    return float(deg) + float(deg_min)/60


base_df = pd.read_csv(f'{IN_FOLDER}/{IN_FILE}.csv')


with open(f'{OUT_FOLDER}/{OUT_FILE}.sql', 'w') as f:
    f.write(f'INSERT INTO {TABLE} VALUES\n')

    for i in range(len(base_df)): 
        row = base_df.iloc[i]

        base_code = row['Base Code']
        base_name = row['Base Name'].replace('\'', '\\\'')
        airport = row['Airport Name'].replace('\'', '\\\'')
        region = row['Region']
        elevation = row['Elevation']
        latitude = convert_coord(row['Latitude'])
        longitude = -1 * convert_coord(row['Longitude'])
        single_rwl = row['RWL: Single']
        double_rwl = row['RWL: Dual']
        twos_rwl = row['RWL: 2S']
        twod_rwl = row['RWL: 2D']
        vlat = row['VLATs']
        lat = row['LATs']
        seat = row['SEATs']
        maffs = row['MAFFS']
        hot_load = row['Hot Loading']
        fuel_load = row['Fuel and Load']
        hot_refuel = row['Hot Refueling']
        retardant_type = row['Retardant Type']
        pit_total = row['Pit Total']
        parking_total = row['Parking Total']
        load_simul = row['Load Simultaneously']
        offload_capacity = row['Offload Capacity']

        s = f'  (\'{base_code}\', \'{base_name}\', \'{airport}\', \'{region}\','
        s += f' {elevation}, {latitude}, {longitude},'
        s += f' {single_rwl}, {double_rwl}, {twos_rwl}, {twod_rwl},'
        s += f' \'{vlat}\', \'{lat}\', \'{seat}\', \'{maffs}\','
        s += f' \'{hot_load}\', \'{fuel_load}\', \'{hot_refuel}\', \'{retardant_type}\','
        s += f' {pit_total}, {parking_total}, {load_simul}, {offload_capacity})'
        s += (',' if i < (len(base_df) - 1) else ';') + '\n'

        f.write(s)
