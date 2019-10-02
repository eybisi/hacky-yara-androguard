import os
import sys
import re

if not os.path.isdir(sys.argv[1]):
    print('Give me report folder argv[1]')
    sys.exit()
reports = [f for f in os.listdir(sys.argv[1])]

if not os.path.isdir(sys.argv[2]):
    print('Give me apk folder argv[2]')
apks = [ f for f in os.listdir(sys.argv[2])]
for report in reports:
    apkname = re.findall('(.*)-report',report)[0]
    if ' ' in report:
        apkname = '\''+apkname+'\''
        report = '\''+report+ '\''
    os.system('yara -x androguard='+ '/'.join([sys.argv[1],report]) + ' ' + sys.argv[3] + ' ' +'/'.join([sys.argv[2],apkname])) 

