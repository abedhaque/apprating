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
frameworks_to_apps = {}
app_to_frameworks = {}

for framework in framework_strings.keys():
    frameworks_to_apps[framework] = []

for app_file in file_names:
    f = open("../sample_outputs/{}".format(app_file), "r")
    text = f.read()
    app_to_frameworks[app_file] = []
    for framework_name in framework_strings.keys():
        if framework_strings[framework_name] in text:
            frameworks_to_apps[framework_name].append(app_file)
            app_to_frameworks[app_file].append(framework_name)

#print(framework_results)

# for framework_name, matching_apps in framework_results.iteritems():
#     print (framework_name + ': ' + str(len(matching_apps)) + '\t\t\t' + str(matching_apps))

for app_name, matching_frameworks in app_to_frameworks.iteritems():
    print(app_name + ':    ' + str(matching_frameworks))
