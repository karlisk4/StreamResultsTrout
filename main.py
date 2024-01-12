import requests
import re
import json
from datetime import timedelta

resList = requests.get("http://75.119.157.74:8772/api/results/list.json?q=%RACE&sort=date&page=0")
resJson = re.search(r'"results_json_url": "(.*?)"', resList.text)
resLink = str(resJson.group(1))
resFile = requests.get("http://75.119.157.74:8772{}".format(resLink))

drivers_json = resFile.json()
#print(drivers_json)
i=1
lenMax=0
driver_info = []
for drivers in drivers_json['Result']:
        stI = str(i)
        driverName = drivers['DriverName']
        qPos = int(drivers['GridPosition'])
        diffPos = qPos-i
        driverLine = "{stI}. {driverName} ".format(stI=stI, driverName=driverName)
        fstLapMs=int(drivers['BestLap'])
        fstlap=timedelta(milliseconds=fstLapMs)
        if len(driverLine) > lenMax:
                lenMax = len(driverLine)

        driver_info.append('{}{}{}'.format(driverLine.ljust(32), str(diffPos).ljust(10), fstlap)) #"{stI}. {driverName} ".format(stI=stI, driverName=driverName)
        i=i+1


# for info in drivers_json['SessionConfig']:
#         print(info)
#print(driver_info)
f = open("demofile3.txt", "w")
for driver in driver_info:
    f.write("%s\n" % driver)
