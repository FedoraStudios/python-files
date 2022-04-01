from tkinter import *
import random

root = Tk()
root.title("Country and Capitals")
root.geometry("600x600")
root.configure(background="dark orange")

Countries = Entry(root)
Capitals = Entry(root)

Countries.place(relx = 0.5, rely = 0.2, anchor=CENTER)
Capitals.place(relx = 0.5, rely = 0.3, anchor=CENTER)



CountriesLabel = Label(root)
CapitalsLabel = Label(root)

RandomCountry = Label(root)
RandomCapital = Label(root)

CountryList = []
CapitalList = []

Footer = Label(root, text="Made by Emir R. Frias-Suzuki")

def CountryCityList():
    CountryVar = Countries.get()
    CapitalVar = Capitals.get()
    
    CountryList.append(CountryVar)
    CapitalList.append(CapitalVar)
    
    CountriesLabel["text"] = "List of Countries: " + str(CountryList)
    CapitalsLabel["text"] = "List of Capitals: " + str(CapitalList)
    
def RandomCountriesCities():
    length = len(CountryList)
    RandomNumber = random.randint(0, length-1)
    
    RandomCountryVar = CountryList[RandomNumber]
    RandomCapitalVar = CapitalList[RandomNumber]
    
    RandomCountry["text"] = str(RandomCountryVar)
    RandomCapital["text"] = str(RandomCapitalVar)

    
btn = Button(root, text="Add Country, And Capital", command=CountryCityList)
btn.place(relx = 0.5, rely = 0.4, anchor=CENTER)

CountriesLabel.place(relx = 0.5, rely = 0.5, anchor=CENTER)
CapitalsLabel.place(relx = 0.5, rely = 0.6, anchor=CENTER)

btnTwo = Button(root, text="Display a Random Country and Capital", command=RandomCountriesCities)
btnTwo.place(relx = 0.5, rely = 0.7, anchor=CENTER)

RandomCountry.place(relx = 0.5, rely = 0.8, anchor=CENTER)
RandomCapital.place(relx = 0.5, rely = 0.9, anchor=CENTER)

Footer.place(relx = 0.5, rely = 0.98, anchor=CENTER)

root.mainloop()