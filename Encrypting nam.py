from tkinter import *

root= Tk()
root.title("Ascii")
root.geometry("600x600")
root.configure(background="grey")

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label=Label(root, text="Name in Ascii: ",bg="light yellow", fg="black")
label2=Label(root, text="Encrypted name: ",bg="cyan", fg="black")
label3=Label(root, text="Made by: Emir R. Frias-Suzuki",bg="orange", fg="black")


def asciiConveter():
    input_word=enter_word.get()
    
    for letter in input_word:
        label["text"]+= str(ord(letter)) + " "
        ascii=int(ord(letter))
        Encrypted=ascii-2
        label2["text"] += str(chr(Encrypted)) + " "

btn = Button(root, text="Show name in Ascii", command=asciiConveter, bg="gold", fg="black")
btn.place(relx=0.5, rely=0.5,anchor=CENTER)
label.place(relx=0.5, rely=0.6, anchor=CENTER)
label2.place(relx=0.5, rely=0.7, anchor=CENTER)
label3.place(relx=0.5, rely=0.98, anchor=CENTER)


root.mainloop()