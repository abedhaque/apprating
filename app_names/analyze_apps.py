import pandas as pd
import os
from tabulate import tabulate


df = pd.read_table('../top_apps.txt', sep='|')

# Use the sample_outputs folder to figure that out which APKs were actually downloaded
file_names = os.listdir("../sample_outputs/")
is_package_downloaded = []
for index, row in df.iterrows():
    if row['Package Name'] + '.txt' in file_names:
        is_package_downloaded.append(1)
    else:
        is_package_downloaded.append(0)

# Add a column that indicates that we actually downloaded the APK
df['Downloaded'] = is_package_downloaded

print tabulate(df, headers='keys', tablefmt='psql')

print(df['Downloaded'].value_counts())

