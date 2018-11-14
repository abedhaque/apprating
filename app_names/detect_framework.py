import os

file_names = os.listdir("../sample_outputs/")

framework_strings = {'xamarin': 'xamarin',
                     'react_native': 'com/facebook/react',
                     'ionic': 'com/ionicframework',
                     'ionic2': 'ionic',
                     'phonegap': 'phonegap',
                     'intel_xdk': 'intel_xdk',
                     'framework7': 'framework7',
                     'titanium': 'titanium',
                     'angular': 'angular',
                     'onsen': 'onsenui',
                     'nativescript': 'nativescript',
                     'kendo': 'kendo',
                     'sencha': 'sencha',
                     'flutter': 'flutter',
                     'cordova': 'cordova',
                     'sencha_touch': 'sencha',
                     'kendo_ui': 'kendo',
                     'kotlin': 'kotlin'}
framework_results = {}

for key in framework_strings.keys():
    framework_results[key] = []

for file in file_names:
    f = open("../sample_outputs/{}".format(file), "r")
    text = f.read()
    for key in framework_strings.keys():
        if framework_strings[key] in text:
            framework_results[key].append(file)

#print(framework_results)

for key, value in framework_results.iteritems():
    print (key + ': ' + str(len(value)) + '\t\t\t' + str(value))

