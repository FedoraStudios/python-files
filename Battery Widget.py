from tkinter import *
from tkinter import ttk
import psutil
from psutil._common import BatteryTime
import datetime
import time

root = Tk()
root.geometry("500x250")
root.config(bg="black")
root.overrideredirect(True)

style = ttk.Style(root)
style.layout("ProgressBarStyle", [("Horizontal.Progressbar.trough", {"children" : 
  [("Horizontal.Progressbar.pbar", {"side": "right", "sticky" : "ns"})], 
  "sticky" : "nsew"}), 
                      ("Horizontal.Progressbar.label", {"sticky": ""})])
    
bar = ttk.Progressbar(root, maximum=100, style="ProgressBarStyle")
bar.place(relx=0.5, rely=0.2, anchor=CENTER)

BatteryLife = Label(root, font=("arial 15 bold"), bg="black", fg="white")
BatteryLife.place(relx=0.5, rely=0.5, anchor=CENTER)

def ConvertTime(second):
    get_time = time.gmtime(seconds)
    time_remain = time.strftime('%H:%M:%S', get_time)
    return time_remain
    
def GetBatteryLife():
    battery = psutil.sensors_battery()
    bar["value"] = battery.percent
    style.configure("ProgressBarStyle", text=str(battery.percent) + "%")
    Battery_left = ConvertTime(battery.secsleft)
    if battery.secsleft == BatteryTime.POWER_TIME_UNLIMITED:
        BatteryLife["text"] = "Unplug the battery because your time is unlimited. \n And read on the code again."
    elif battery.secsleft == BatteryTime.POWER_TIME_UNKNOWN:
        BatteryLife["text"] = "Battery life not detected. \n Please run the code again."
    else:
        batteryLife["text"] = "Battery Life: " + Battery_left
        root.after(1000, GetBatteryLife)
        
GetBatteryLife()
root.mainloop()