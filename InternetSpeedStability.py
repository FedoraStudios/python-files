from tkinter import *
import speedtest
import matplotlib.pyplot as plt
import time
#pip install speedtest-cli
#speedtest-cli --version

listDS = []
listUS = []

x = [1, 2, 3, 4, 5]


for i in range(5):
    st1=speedtest.Speedtest()
    downloadS = round(st1.download() /1000000, 2)
    listDS.append(downloadS)
    
    uploadS = round(st1.upload() /1000000, 2)
    listUS.append(uploadS)
    
    time.sleep(60)
    
print(listDS)
print(listUS)

plt.plot(x, listDS, label="Download Speed")
plt.plot(x, listUS, label="Upload Speed")
plt.legend()

plt.show()
 