import os

file_names = os.listdir("../sample_outputs/")

framework_strings = {'xamarin': 'xamarin',
                     'react_native': 'com/facebook/react',
                     'ionic': 'com/ionicframework',
                     'phonegap': 'phonegap',
                     'intel_xdk': 'intel_xdk',
                     'framework7': 'framework7',
                     'titanium': 'titanium',
                     'angular': 'angular',
                     'onsen': 'onsen',
                     'nativescript': 'nativescript',
                     'kendo': 'kendo',
                     'sencha': 'sencha'}
framework_results = {}

for key in framework_strings.keys():
    framework_results[key] = []

for file in file_names:
    f = open("../sample_outputs/{}".format(file), "r")
    text = f.read()
    for key in framework_strings.keys():
        if framework_strings[key] in text:
            framework_results[key].append(file)

print(framework_results)
