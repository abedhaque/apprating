import pandas as pd
import os
from tabulate import tabulate
from detect_framework import *


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
print(df['Downloaded'].value_counts())

print('The following files were additional APK downloads that were not in top downloaded apps list:')
for file in file_names:
    if file[:-4] not in df['Package Name'].tolist():
        print(file)

# To make it easier, remove all apps that were not downloaded from the dataframe
df = df[df['Downloaded'] == 1]

category_percentages_df = pd.DataFrame({'Percentage': df.groupby('Category').size() / len(df),
                                        'Count': df.groupby('Category').size()})
print('Categories by percentage:\n\n')
print(category_percentages_df.to_latex())


# Add a column to the dataframe that indicates which frameworks were detected
detected_apps_to_frameworks, detected_frameworks_to_apps = get_detected_frameworks_for_apps()
detected_frameworks_for_df = []
for index, row in df.iterrows():
    detected_frameworks_for_df.append(detected_apps_to_frameworks[row['Package Name']])

df['Frameworks'] = detected_frameworks_for_df
print tabulate(df, headers='keys', tablefmt='psql')

# Also create a separate dataframe for framework occurrences
frameworks = []
framework_counts = []
for framework_name, matching_apps in detected_frameworks_to_apps.iteritems():
    if len(matching_apps) > 0:
        frameworks.append(framework_name)
        framework_counts.append(len(matching_apps))

framework_count_df = pd.DataFrame({'Framework': frameworks, 'Count': framework_counts}, columns=['Framework', 'Count'])

#print tabulate(framework_count_df, headers='keys', tablefmt='psql')
print(framework_count_df.to_latex(index=False))

# Create a dataframe that sees how categories correlate to framework usage
category_to_framework_usage_dict_no_kotlin = {}
category_to_kotlin_usage = {}

for index, row in df.iterrows():
    if len(row['Frameworks']) > 0 and 'kotlin' not in row['Frameworks']:
        if row['Category'] not in category_to_framework_usage_dict_no_kotlin:
            category_to_framework_usage_dict_no_kotlin[row['Category']] = 1
        else:
            category_to_framework_usage_dict_no_kotlin[row['Category']] += 1
    if 'kotlin' in row['Frameworks']:
        if row['Category'] not in category_to_kotlin_usage:
            category_to_kotlin_usage[row['Category']] = 1
        else:
            category_to_kotlin_usage[row['Category']] += 1

#
# category_to_framework_usage_df = pd.DataFrame.from_dict(category_to_framework_usage_dict_no_kotlin, orient='index',
#                                                         columns=['Category', 'Apps that used a framework'])
category_to_framework_usage_no_kotlin_df = pd.DataFrame(
    list(category_to_framework_usage_dict_no_kotlin.iteritems()),
    columns=['Category', 'Apps that used a framework']).sort(columns='Apps that used a framework', ascending=0)

category_to_kotlin_usage_df = pd.DataFrame(
    list(category_to_kotlin_usage.iteritems()),
    columns=['Category', 'Apps that used Kotlin']).sort(columns='Apps that used Kotlin', ascending=0)

print category_to_framework_usage_no_kotlin_df.to_latex(index=False)
print category_to_kotlin_usage_df.to_latex(index=False)


