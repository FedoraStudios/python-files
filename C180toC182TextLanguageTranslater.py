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

ComboBox = ttk.Combobox(root, values=language, width = 22, state="readonly")
ComboBox.place(relx=0.13, rely=0.2, anchor=W)
ComboBox.set("english")

OutputLabel = Label(root, text="Output", font="arial 13 bold", bg="#f2CCC3")
OutputLabel.place(relx=0.80, rely=0.2, anchor=E)

DestComboBox = ttk.Combobox(root, values=language, width = 22, state="readonly")
DestComboBox.place(relx=0.98, rely=0.2, anchor=E)
DestComboBox.set("Show Output Language")

InputText = Text(root, font = "arial 13", height=11, wrap=WORD, padx=5, pady=5, width=26, bg="white")
InputText.place(relx = 0.02, rely=0.6,anchor=W)

OutputText = Text(root, font = "arial 13", height=11, wrap=WORD, padx=5, pady=5, width=26, bg="white")
OutputText.place(relx = 0.98, rely=0.6,anchor=E)

def translate():
    translator = Translator()
    Val = ComboBox.get()
    DestVal = DestComboBox.get()
    print(Val)
    print(DestVal)
    s
    try:
        print("E")
        translated = translator.translate(text = InputText.get(1.0, END), src=ComboBox.get(), dest=DestComboBox.get())
        print("E2")
        OutputText.delete(1.0, END)
        print("E3")
        Outputtext.insert(END, translated.text)
        print("E4")
      
    except:
      print("Sorry, and error occurd, please try again later.")
        

Btn = Button(root, text="Translate", command=translate) 
Btn.place(relx = 0.5, rely=0.85, anchor=CENTER)

FooterLabel = Label(root, text="Created by Emir R. Frias Suzuki", bg="white")
FooterLabel.place(relx=0.5, rely=0.97, anchor=CENTER)

root.mainloop()


