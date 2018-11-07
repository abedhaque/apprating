import os

file_names = os.listdir("../sample_outputs/")

framework_strings = {'xamarin': 'xamarin', 'react_native': 'com/facebook/react'}
framework_results = {}

for key in framework_strings.keys():
    framework_results[key] = []

for file in file_names:
    f = open("../sample_outputs/{}".format(file), "r")
    for key in framework_strings.keys():
        print(framework_strings[key])
        for line in f.readlines():
            if framework_strings[key] in line:
                framework_results[key].append(file)
                break

print(framework_results)
