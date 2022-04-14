from tkinter import *
import random

root = Tk()
root.title("Testing Random Function")
root.geometry("400x400")
root.configure(bg="dark blue")

BlankLabel = Label(root)
CopyRightFooterTHing = Label(root, text="Made By Emir R. Frias-Suzuki")
GuessPassword = Entry(root)
GuessedPasswordLabel = Label(root)
array3D = [[["1","2","3","4","5","6"], ["head", "Tail", "BosG", "Coral"], ["A","B", "C","D", "E","F","G","H"]]]
print(array3D[0][2][3])

def newPassword():
    randomNumberOne = random.randint(0,5)
    randomNumberTwo = random.randint(0,3)
    randomNumberThree = random.randint(0,7)
    
    IntigerOne = str(array3D[0][0][randomNumberOne])
    IntigerTwo = array3D[0][1][randomNumberTwo]
    IntigerThree = array3D[0][2][randomNumberThree]
    
    BlankLabel["text"] =  IntigerOne +""+ IntigerTwo +""+ IntigerThree

    GuessedPasswordLabel["text"] = "Your Guessed Password Is: " + GuessPassword.get()
    
btn = Button(root, text="Create New Password", command=newPassword)


GuessedPasswordLabel.place(relx=0.5, rely=0.3, anchor=CENTER)

GuessPassword.place(relx=0.5, rely=0.4, anchor=CENTER)

btn.place(relx=0.5, rely=0.5, anchor=CENTER)

BlankLabel.place(relx=0.5, rely=0.6, anchor=CENTER)
CopyRightFooterTHing.place(relx=0.5, rely=0.97, anchor=CENTER)

root.mainloop()