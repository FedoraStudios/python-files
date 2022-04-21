from tkinter import *
import random

root=Tk()
root.title("Random Colors")
root.geometry("500x500")

dictionary = {"colors" : ["red", "dark orange", "gray", "cyan", "yellow", "lime green", "blue", "brown", "pink", "purple", "black"] }
CopyRightThing = Label(root, text="Made by Emir R. Frias-Suzuki")

def randomNumber():
    randomNumber = random.randint(0, 10)
    color = dictionary["colors"][randomNumber]
    root.configure(background = color)



btn = Button(root, text="Change Background", command=randomNumber)
btn.place(relx = 0.5, rely = 0.5, anchor=CENTER)

CopyRightThing.place(relx = 0.5, rely = 0.97, anchor=CENTER)

root.mainloop()
