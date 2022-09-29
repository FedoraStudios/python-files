import matplotlib.pyplot as plt
import psutil as p

appNameDict = {}


count = 0

for process in p.process_iter():
    count = count + 1
    if count <= 6:
        name = process.name()
        cpuUsage = p.cpu_percent()
        print("name: ", name, "cpuUsage", cpuUsage)
        appNameDict.update({name: cpuUsage})
        
        keymax=max(appNameDict, key=appNameDict.get)
        print(keymax)
        
        keymin=min(appNameDict, key=appNameDict.get)
        print(keymin)
        
        keyMinMax = [keymax, keymin]
        print(keyMinMax)
        
        appNameDictVal = appNameDict.values()
        
        maxApp=max(appNameDictVal)
        print(maxApp)
        
        minApp=min(appNameDictVal)
        print(minApp)
        
        appMinMax = [maxApp,minApp]
        print(appMinMax)
        
plt.figure(figsize = (15,7))
plt.xlabel("Application")
plt.ylabel("CPU Usage")
plt.bar(keyMinMax, appMinMax, width=0.6, color=("cyan", "crimson"))
plt.show()