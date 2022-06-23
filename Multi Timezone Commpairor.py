from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from datetime import datetime
import pytz
import time

root = Tk()
root.title("Multi Timezone Compairor")
root.geometry("600x450")
root.configure(bg = "grey")

TimeZones = ["USAEST", "Australia", "JapanTokyo", "MexicoMexicoCity", "VenezuelaCaracas", "London", "GermanyBerlin", "FranceParis", "ItalyRome"]

selectedVAL = StringVar()
dropdown1 = ttk.Combobox(root, values=TimeZones, textvariable = selectedVAL)
dropdown1.place(relx=0.3, rely=0.05, anchor=CENTER)
DropdownGet1 = dropdown1.get()
label1 = Label(root, text=DropdownGet1)
label1.place(relx= 0.3, rely=0.1, anchor=CENTER)
Label12 = Label(root)
Label12.place(relx= 0.3, rely=0.65, anchor=CENTER)

selectedVAL = StringVar()
dropdown2 = ttk.Combobox(root, values=TimeZones, textvariable = selectedVAL)
dropdown2.place(relx=0.7, rely=0.05, anchor=CENTER)
DropdownGet2 = dropdown2.get()
label2 = Label(root, text=DropdownGet2)
label2.place(relx= 0.7, rely=0.1, anchor=CENTER)
Label22 = Label(root)
Label22.place(relx= 0.7, rely=0.65, anchor=CENTER)



class USAEST(): 
    
       def time(self):
         Location = pytz.timezone('US/Eastern')
         LocalTime = datetime.now(Location)
         CurrentTime = LocalTime.strftime("%H: %M: %S")
         if DropdownGet1 == "USAEST":
             Label12["text"] = "Time: " +  CurrentTime
             print("e1")
         elif DropdownGet2 == "USAEST":
             Label22["text"] = "Time: " +  CurrentTime
             print("e2")
            
class Australia(): 
    
       def time(self):
         Location = pytz.timezone('Australia/ACT')
         LocalTime = datetime.now(Location)
         CurrentTime = LocalTime.strftime("%H: %M: %S")
         if DropdownGet1 == "Australia":
             Label12["text"] = "Time: " +  CurrentTime
             print("e3")
         elif DropdownGet2 == "Australia":
             Label22["text"] = "Time: " +  CurrentTime
             print("e4")

class JapanTokyo(): 
    
       def time(self):
         Location = pytz.timezone('Asia/Tokyo')
         LocalTime = datetime.now(Location)
         CurrentTime = LocalTime.strftime("%H: %M: %S")
         if DropdownGet1 == "JapanTokyo":
             Label12["text"] = "Time: " +  CurrentTime
             print("e5")
         elif DropdownGet2 == "JapanTokyo":
             Label22["text"] = "Time: " +  CurrentTime
             print("e6")
            
class MexicoMexicoCity(): 
        
       def time(self):
          Location = pytz.timezone('America/Mexico_City')
          LocalTime = datetime.now(Location)
          CurrentTime = LocalTime.strftime("%H: %M: %S")
          if DropdownGet1 == "MexicoMexicoCity":
             Label12["text"] = "Time: " +  CurrentTime
             print("e7")
          elif DropdownGet2 == "MexicoMexicoCity":
             Label22["text"] = "Time: " +  CurrentTime
             print("e8")
             
            
class VenezuelaCaracas(): 
        
       def time(self):
          Location = pytz.timezone('America/Caracas')
          LocalTime = datetime.now(Location)
          CurrentTime = LocalTime.strftime("%H: %M: %S")
          if DropdownGet1 == "VenezuelaCaracas":
             Label12["text"] = "Time: " +  CurrentTime
             print("e9")
          elif DropdownGet2 == "VenezuelaCaracas":
             Label22["text"] = "Time: " +  CurrentTime
             print("e10")
             
class London(): 
        
       def time(self):
          Location = pytz.timezone('Europe/London')
          LocalTime = datetime.now(Location)
          CurrentTime = LocalTime.strftime("%H: %M: %S")
          if DropdownGet1 == "London":
             Label12["text"] = "Time: " +  CurrentTime
             print("e11")
          elif DropdownGet2 == "London":
             Label22["text"] = "Time: " +  CurrentTime
             print("e12")
             
class GermanyBerlin(): 
        
       def time(self):
          Location = pytz.timezone('Europe/Berlin')
          LocalTime = datetime.now(Location)
          CurrentTime = LocalTime.strftime("%H: %M: %S")
          if DropdownGet1 == "GermanyBerlin":
             Label12["text"] = "Time: " +  CurrentTime
             print("e13")
          elif DropdownGet2 == "GermanyBerlin":
             Label22["text"] = "Time: " +  CurrentTime
             print("e14")

class FranceParis(): 
        
       def time(self):
          Location = pytz.timezone('Europe/Paris')
          LocalTime = datetime.now(Location)
          CurrentTime = LocalTime.strftime("%H: %M: %S")
          if DropdownGet1 == "FranceParis":
             Label12["text"] = "Time: " +  CurrentTime
             print("e15")
          elif DropdownGet2 == "FranceParis":
             Label22["text"] = "Time: " +  CurrentTime
             print("e16")

class ItalyRome(): 
        
        def time(self):
           Location = pytz.timezone('Europe/Rome')
           LocalTime = datetime.now(Location)
           CurrentTime = LocalTime.strftime("%H: %M: %S")
           if DropdownGet1 == "ItalyRome":
              Label12["text"] = "Time: " +  CurrentTime
              print("e17")
           elif DropdownGet2 == "ItalyRome":
              Label22["text"] = "Time: " +  CurrentTime
              print("e18")

ObjectUSAEST = USAEST()
ObjectAustralia = Australia()
ObjectJapanTokyo = JapanTokyo()
ObjectMexicoMexicoCity = MexicoMexicoCity()
ObjectVenezuelaCaracas = VenezuelaCaracas()
ObjectLondon = London()
ObjectGermanyBerlin = GermanyBerlin()
ObjectFranceParis = FranceParis()
ObjectItalyRome = ItalyRome()

def CommandFunction1():
    global ObjectUSAEST
    global ObjectAustralia
    global ObjectJapanTokyo
    global ObjectMexicoMexicoCity
    global ObjectVenezuelaCaracas
    global ObjectLondon
    global ObjectGermanyBerlin
    global ObjectFranceParis
    global ObjectItalyRome

    
    if DropdownGet1 == "USAEST":
        ObjectUSAEST.time()
        
    elif DropdownGet1 == "Australia":
          ObjectAustralia.time()
    
    elif DropdownGet1 == "JapanTokyo":
          ObjectJapanTokyo.time()
         
    elif DropdownGet1 == "MexicoMexicoCity":
          ObjectMexicoMexicoCity.time()
    
    elif DropdownGet1 == "VenezuelaCaracas":
          ObjectVenezuelaCaracas.time()
          
    elif DropdownGet1 == "London":
          ObjectLondon.time()
    
    elif DropdownGet1 == "GermanyBerlin":
          ObjectGermanyBerlin.time()
    
    elif DropdownGet1 == "FranceParis":
          ObjectFranceParis.time()
    
    elif DropdownGet1 == "ItalyRome":
          ObjectItalyRome.time()
        
def CommandFunction2():
    global ObjectUSAEST
    global ObjectAustralia
    global ObjectJapanTokyo
    global ObjectMexicoMexicoCity
    global ObjectVenezuelaCaracas
    global ObjectLondon
    global ObjectGermanyBerlin
    global ObjectFranceParis
    global ObjectItalyRome

    
    if DropdownGet2 == "USAEST":
        ObjectUSAEST.time()
        
    elif DropdownGet2 == "Australia":
          ObjectAustralia.time()
    
    elif DropdownGet2 == "JapanTokyo":
          ObjectJapanTokyo.time()
         
    elif DropdownGet2 == "MexicoMexicoCity":
          ObjectMexicoMexicoCity.time()
    
    elif DropdownGet2 == "VenezuelaCaracas":
          ObjectVenezuelaCaracas.time()
          
    elif DropdownGet2 == "London":
          ObjectLondon.time()
    
    elif DropdownGet2 == "GermanyBerlin":
          ObjectGermanyBerlin.time()
    
    elif DropdownGet2 == "FranceParis":
          ObjectFranceParis.time()
    
    elif DropdownGet2 == "ItalyRome":
          ObjectItalyRome.time()
          
        #Command is Still not working for the buttons
Btn1 = Button(root, text="Get Time", command=CommandFunction1)
Btn2 = Button(root, text="Get Time", command=CommandFunction2)
Btn1.place(relx=0.3, rely=0.8)
Btn2.place(relx=0.7,rely=0.8)
             
root.mainloop()