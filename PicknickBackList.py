from tkinter import *
import random

root = Tk()
root.title("picknic bag list")
root.geometry("400x400")
root.configure(bg = "dark orange")

listOfItemsInBag = ["Fedora", "water bottle", "Rice cake", "napkins", "camera", "picknic blanket"]


listOfItemsInBagLabel = Label(root, text = listOfItemsInBag, bg = "gold", fg = "black")
listOfItemsInBagLabel.place(relx = 0.5, rely = 0.4, anchor = CENTER)
FooterThing = Label(root, text="Made by Emir R. Frias-Suzuki", bg = "grey", fg = "white")
FooterThing.place(relx = 0.5, rely = 0.98, anchor = CENTER)

randomLabel = Label(root)
def randomNumberGenerater():
    n = random.randint(1, 7)
    randomLabel["text"] = "Put Item " + str(n) + " in the bag"

btn = Button(root, text = "Put specific item in the bag", command = randomNumberGenerater, bg = "cyan", fg = "black")
randomLabel.place(relx  = 0.5, rely = 0.6, anchor = CENTER)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()
