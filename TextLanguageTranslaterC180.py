from tkinter import *
from tkinter import ttk
#from googletrans import Translator, LANGUAGES as gt

root = Tk()
root.config(bg="grey")
root.geometry("1000x400")
root.title("Translator")


#Language = list(LANGUAGES.value())

TitleLabel = Label(root, text="Language Translator", bg="white", font=("Sylfazn", 18, "bold", "italic"))
TitleLabel.place(relx=0.5, rely=0.1, anchor=CENTER)

inputLabel = Label(root, text="Enter Text", font="arial 13 bold")
inputLabel.place(relx=0.02, rely=0.2, anchor=W)

InputText = Text(root, font = "arial 13", height=11, wrap=WORD, padx=5, pady=5, width=16, bg="white")
InputText.place(relx = 0.02, rely=0.5,anchor=W)

root.mainloop()


