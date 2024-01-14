import requests
import re
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
driver_stats = []
for drivers in drivers_json['Result']:
        stI = str(i)
        driverName = drivers['DriverName']
        qPos = int(drivers['GridPosition'])
        diffPos = qPos-i
        driverLine = "{stI}. {driverName} ".format(stI=stI, driverName=driverName)
        fstLapMs=int(drivers['BestLap'])
        fstlap=str(timedelta(milliseconds=fstLapMs))
        a = fstlap.replace("0:0","0")
        b = a.replace("000","")
        fstlap = b
        if len(driverLine) > lenMax:
                lenMax = len(driverLine)

        driver_info.append(driverLine) # 
        driver_stats.append('{}{}'.format(str(diffPos).ljust(10), fstlap))
        i=i+1


# for info in drivers_json['SessionConfig']:
#         print(info)
#print(driver_info)
with open("names.txt", "w") as f:
       for driver in driver_info:
                f.write("%s\n" % driver)

with open("result.txt", "w") as g:
               for driver in driver_stats:
                g.write("%s\n" % driver)
