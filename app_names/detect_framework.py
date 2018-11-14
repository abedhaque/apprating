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

for framework in framework_strings.keys():
    framework_results[framework] = []

for app_file in file_names:
    f = open("../sample_outputs/{}".format(app_file), "r")
    text = f.read()
    for framework_name in framework_strings.keys():
        if framework_strings[framework_name] in text:
            framework_results[framework_name].append(app_file)

#print(framework_results)

for framework_name, value in framework_results.iteritems():
    print (framework_name + ': ' + str(len(value)) + '\t\t\t' + str(value))

