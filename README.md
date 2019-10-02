## hacky hacky 

Follow instruction page and compile yara with androguard module. You need to download yara-3.7.0, module doesnt work on 3.8
https://github.com/Koodous/androguard-yara

Androguard module works with reports. Normally koodous provides analysis report that you can download, But if your sample didn't analyzed on koodous you need to create report. Using androguard's python library I generate a report file. Not all components included but included components are import ones. Like permission, apk_name etc.. If you can add more components to report that missing, feel free to pr.

Needed components:

- [url](https://github.com/Koodous/androguard-yara/blob/master/androguard.c#L544)

## How to use it

There is 2 python script; 

- create_report.py
- scan.py
  
`create_report.py` will create apk reports that will be used with yara. You can give folder name that all your apks are staying or file name.

`create_report.py apk`

Script will create reports folder and put reports there.

yarame.py takes 3 parameter: report folder, apk folder and yara rule

`scan.py reports apk dropper.yar`

Since androguard module doesn't work on latest yara python library I used os.system, if you can run it with yara library feel free to pr.

[![asciicast](https://asciinema.org/a/nJ1Ag8qCWsfopJsXpi7ON4agh.svg)](https://asciinema.org/a/nJ1Ag8qCWsfopJsXpi7ON4agh)

