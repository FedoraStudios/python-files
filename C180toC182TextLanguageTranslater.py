from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.config(bg="grey")
root.geometry("1000x400")
root.title("Translator")


language = list(LANGUAGES.values())

TitleLabel = Label(root, text="Language Translator", bg="white", font=("Sylfazn", 18, "bold", "italic"))
TitleLabel.place(relx=0.5, rely=0.1, anchor=CENTER)

inputLabel = Label(root, text="Enter Text", font="arial 13 bold")
inputLabel.place(relx=0.02, rely=0.2, anchor=W)

strComboBox = ttk.Combobox(root, values=language, width = 22, state="readonly")
strComboBox.place(relx=0.13, rely=0.2, anchor=W)
strComboBox.set("english")

OutputLabel = Label(root, text="Output", font="arial 13 bold", bg="#f2CCC3")
OutputLabel.place(relx=0.80, rely=0.2, anchor=E)

DestComboBox = ttk.Combobox(root, values=language, width = 22, state="readonly")
DestComboBox.place(relx=0.98, rely=0.2, anchor=E)
DestComboBox.set("Show Output Language")

InputText = Text(root, font = "arial 13", height=11, wrap=WORD, padx=5, pady=5, width=26, bg="white")
InputText.place(relx = 0.02, rely=0.6,anchor=W)

OutputText = Text(root, font = "arial 13", height=11, wrap=WORD, padx=5, pady=5, width=26, bg="white")
OutputText.place(relx = 0.98, rely=0.6,anchor=E)

#def translater():
    

Btn = Button(root, text="Translate") #command=translater
Btn.place(relx = 0.5, rely=0.9, anchor=CENTER)

root.mainloop()


