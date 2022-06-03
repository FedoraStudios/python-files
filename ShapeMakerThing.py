from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Image Drawer")
root.geometry("1000x600")
root.configure(bg="grey")

canvas = Canvas(root, width=980, height=490, highlightbackground="lightgrey", bg="white")
canvas.pack()

ChooseColorLabel = Label(root, text="Choose Color")
StartXLabel = Label(root, text="start X")
StartYLabel = Label(root, text="start Y")
EndXLabel = Label(root, text="end X")
EndYLabel = Label(root, text="end Y")

ChooseColorVar = ["crimson", "black", "blue", "cyan", "lime", "green", "yellow", "orange", "grey", "red"]
CordanateValues = [10, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400]


ChooseColorDrop = ttk.Combobox(root, values=ChooseColorVar, state="readonly")
D1X = ttk.Combobox(root, values=CordanateValues, state="readonly")
D1Y = ttk.Combobox(root, values=CordanateValues, state="readonly")
D2X = ttk.Combobox(root, values=CordanateValues, state="readonly")
D2Y = ttk.Combobox(root, values=CordanateValues, state="readonly")


ChooseColorLabel.place(relx=0.6 ,rely=0.9 ,anchor=CENTER)
StartXLabel.place(relx=0.1 ,rely=0.85 ,anchor=CENTER)
StartYLabel.place(relx=0.3 ,rely=0.85 ,anchor=CENTER)
EndXLabel.place(relx=0.5 ,rely=0.85 ,anchor=CENTER)
EndYLabel.place(relx=0.7 ,rely=0.85 ,anchor=CENTER)

ChooseColorDrop.place(relx=0.8 ,rely=0.9 ,anchor=CENTER)
D1X.place(relx=0.2 ,rely=0.85 ,anchor=CENTER)
D1Y.place(relx=0.4 ,rely=0.85 ,anchor=CENTER)
D2X.place(relx=0.6 ,rely=0.85 ,anchor=CENTER)
D2Y.place(relx=0.8 ,rely=0.85 ,anchor=CENTER)


def circle(event):
    oldX = D1X.get()
    oldY = D1Y.get()
    newX = D2X.get()
    newY = D2Y.get()
    keypress = "c"
    Draw(keypress, oldX, oldY, newX, newY)

def rectangle(event):
    oldX = D1X.get()
    oldY = D1Y.get()
    newX = D2X.get()
    newY = D2Y.get()
    keypress = "r"
    Draw(keypress, oldX, oldY, newX, newY)

def line(event):
    oldX = D1X.get()
    oldY = D1Y.get()
    newX = D2X.get()
    newY = D2Y.get()
    keypress = "l"
    Draw(keypress, oldX, oldY, newX, newY)
    
def triangle(event):
    oldX = D1X.get()
    oldY = D1Y.get()
    newX = D2X.get()
    newY = D2Y.get()
    keypress = "t"
    Draw(keypress, oldX, oldY, newX, newY)

def square(event):
    oldX = D1X.get()
    oldY = D1Y.get()
    newX = D2X.get()
    newY = D2Y.get()
    keypress = "s"
    Draw(keypress, oldX, oldY, newX, newY)
    
def arc(event):
    oldX = D1X.get()
    oldY = D1Y.get()
    newX = D2X.get()
    newY = D2Y.get()
    keypress = "a"
    Draw(keypress, oldX, oldY, newX, newY)

    
def Draw(keypress, oldX, oldY, newX, newY):
    color = ChooseColorDrop.get()
    if(keypress == "c"):
        drawCircle = canvas.create_oval(oldX, oldY, newX, newY, fill=color)
    if(keypress == "r"):
        drawRectangle = canvas.create_rectangle(oldX, oldY, newX, newY, fill=color)
    if(keypress == "l"):
        drawline = canvas.create_line(oldX, oldY, newX, newY, fill=color, width=3)
   # if(keypress == "t"): this dosnt work
     #   drawTriangle = canvas.create_polygon(args, kw)
   # if(keypress == "s"): nor those this
    #    drawSquare = canvas.create_polygon(oldX, oldY, newX, newY, fill=color)
    if(keypress == "a"):
        drawRectangle = canvas.create_arc(oldX, oldY, newX, newY, fill=color)
      
root.bind("<c>", circle)
root.bind("<r>", rectangle)
root.bind("<l>", line)
#root.bind("<t>", triangle)
#root.bind("<s>", square) 
root.bind("<a>", arc)

root.mainloop()