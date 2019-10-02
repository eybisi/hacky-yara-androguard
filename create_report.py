#!/usr/bin/python
from androguard.core.bytecodes import apk
import json
import sys
import os
#use rules for only defined key variables
def create_report(f):
    if not os.path.isfile(f):
        filename = os.getcwd()+"/"+sys.argv[1]+"/"+f
    print (filename)
    try:
        a = apk.APK(filename)
    except:
        print("We have a badboy here: not apk {}".format(filename))
        return
    d = {}
    d["app_name"] = a.get_app_name()
    d["package_name"] = a.get_package()
    d['permissions'] = a.get_permissions()
    d['activities'] = a.get_activities()
    d['receivers'] = a.get_receivers()
    d['providers'] = a.get_providers()
    d['main_activity'] = a.get_main_activity()
    d['services'] = a.get_services()
    d['max_sdk_version'] = a.get_max_sdk_version()
    d['min_sdk_version'] = a.get_min_sdk_version()
    d['version_code'] = a.get_androidversion_code()
    d['libraries'] = [x for x in a.get_libraries()]
    d['target_sdk_version'] = a.get_target_sdk_version()
    jaysin = json.dumps(d)
    f = open(os.getcwd()+'/reports/'+f+'-report.json','w')
    f.write(jaysin)
    f.close()
if os.path.isdir(sys.argv[1]):
    files = [f for f in os.listdir(sys.argv[1])]
    os.mkdir("reports")
    for f in files:
        create_report(f)
else:
    create_report(sys.argv[1])

