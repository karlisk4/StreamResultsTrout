import requests
import re
import json

resList = requests.get("http://75.119.157.74:8772/api/results/list.json?q=%RACE&sort=date&page=0")
resJson = re.search(r'"results_json_url": "(.*?)"', resList.text)
resLink = str(resJson.group(1))
resFile = requests.get("http://75.119.157.74:8772{}".format(resLink))

drivers_json = resFile.json()
i=1
driver_info = []
for drivers in drivers_json['Result']:
        stI = str(i)
        driverName = drivers['DriverName']
        driver_info.append("{stI}. {driverName}".format(stI=stI, driverName=driverName))
        i=i+1

# for info in drivers_json['SessionConfig']:
#         print(info)
print(driver_info)
f = open("demofile3.txt", "w")
for driver in driver_info:
    f.write("%s\n" % driver)
