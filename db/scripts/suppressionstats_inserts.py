import pandas as pd


IN_FOLDER = 'output'
IN_FILE = 'suppression_stats_with_drops'

OUT_FOLDER = 'db/data'
OUT_FILE = 'suppressionstats_data'

TABLE = 'SuppressionStats'


stats_df = pd.read_csv(f'{IN_FOLDER}/{IN_FILE}.csv')


with open(f'{OUT_FOLDER}/{OUT_FILE}.sql', 'w') as f:
    f.write(f'INSERT INTO {TABLE} VALUES\n')

    for i in range(len(stats_df)): 
        row = stats_df.iloc[i]

        s = f'  (\'{row["UniqueFireIdentifier"]}\', {row["HoursBurned"]}, {row["NormalizedTime"]},'
        s += f' {row["NormalizedAcreage"]}, {row["SuppressionResult"]}, {row["HasPlaneDrop"]})'
        s += (',' if i < (len(stats_df) - 1) else ';') + '\n'

        f.write(s)
