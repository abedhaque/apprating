import pandas as pd
from tabulate import tabulate


df = pd.read_table('../top_apps.txt', sep='|')
print tabulate(df, headers='keys', tablefmt='psql')