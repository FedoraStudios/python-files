from tkinter import *
import random

root = Tk()

root.title("RandomWordGenerator")
root.geometry("500x500")
root.configure(bg="dark orange")

listOne = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
labelOne = Label(root)
CopyRightFooterThing = Label(root, text="Made by Emir R. Frias-Suzuki")

def GenerateRandomWord():
    randomNumberOne = random.randint(0, 50)
    randomNumberTwo = random.randint(0, 50)
    randomNumberThree = random.randint(0, 50)
    randomNumberFour = random.randint(0, 50)
    
    labelOne ["text"] = listOne[randomNumberOne] + listOne[randomNumberTwo] + listOne[randomNumberThree] + listOne[randomNumberFour]

btn = Button(root, text="Generate Random Word", command=GenerateRandomWord)
btn.place(relx = 0.5, rely = 0.4, anchor=CENTER)
labelOne.place(relx = 0.5, rely = 0.5, anchor=CENTER)
CopyRightFooterThing.place(relx = 0.5, rely = 0.98, anchor=CENTER)


root.mainloop()