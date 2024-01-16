import requests
import re
from datetime import timedelta

#mainigo deklaresana
i=1
lenMax=0
driver_info = []
driver_stats = []

#Json iegūšana
resList = requests.get("http://75.119.157.74:8772/api/results/list.json?q=%RACE&sort=date&server=0&page=0")
resJson = re.search(r'"results_json_url": "(.*?)"', resList.text)
resLink = str(resJson.group(1))
resFile = requests.get("http://75.119.157.74:8772{}".format(resLink))
drivers_json = resFile.json()


for drivers in drivers_json['Result']:
        #braucēju vārdi
        stI = str(i)
        driverName = drivers['DriverName']
        driverLine = "{stI}. {driverName} ".format(stI=stI, driverName=driverName)
        #kvalifikācijas dati
        qPos = int(drivers['GridPosition'])
        diffPos = qPos-i
        fstLapMs=int(drivers['BestLap'])
        fstlap=str(timedelta(milliseconds=fstLapMs))
        a = fstlap.replace("0:0","0")
        b = a.replace("000","")
        fstlap = b
        #finiša atstums no līdera
        lapsCompl = sum(driverName in s['DriverName'] for s in drivers_json['Laps'])  
        timeTotal = drivers['TotalTime']
        timeGap = 0
        if i==1:
                lapsLeader = lapsCompl
                timeLeader = timeTotal
                timeGap = '{}{}'.format(lapsLeader, " laps")
        elif lapsCompl==lapsLeader:
                timeGap = str((timeTotal-timeLeader)/1000.0)
                timeGap = '{}{}{}'.format('+', timeGap, "s")
        else:
                timeGap = str(lapsLeader-lapsCompl)
                timeGap = '{}{}{}'.format('+', timeGap, " laps")

        #gala sarakstu veidošana
        driver_info.append(driverLine) #
        driver_stats.append('{}{}{}'.format(str(diffPos).ljust(8), fstlap.ljust(15), timeGap))
        i=i+1
#teksta failu izveide
with open("names.txt", "w") as f:
       for driver in driver_info:
                f.write("{}\n".format(driver))

with open("result.txt", "w") as g:
               for driver in driver_stats:
                g.write("{}\n".format(driver))

print("Done!")