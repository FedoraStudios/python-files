from tkinter import *

root = Tk()
root.title("Profit Application")
root.geometry("600x600")
root.configure(background="cyan")

AllMonthsLabel = Label(root)
ProfitTupleLabel = Label(root)
maxProfitLabel = Label(root)
minProfitLabel = Label(root)
CopyRightLabelThing = Label(root, text="Made by Emir R. Frias-Suzuki")

AllMonths = ("january", "febuary", "march", "april", "may", "June", "july", "august", "september", "october", "november", "december")
ProfitTuple = (12608, 491238, 54673, 39285, 3607, 20009, 21738, 39583, 28403, 92830, 302837)

AllMonthsLabel["text"] = AllMonths
ProfitTupleLabel["text"] = ProfitTuple

def Profit():

    maxProfit = max(ProfitTuple)
    maxProfitIndex = ProfitTuple.index(maxProfit)
    
    maxProfitMonth = AllMonths[maxProfitIndex]
    maxProfitLabel["text"] = "The Maximum Profit Of " + str(maxProfit) + " In the month of " + maxProfitMonth
    
    
    
    minProfit = min(ProfitTuple)
    minProfitIndex = ProfitTuple.index(minProfit)
    
    minProfitMonth = AllMonths[minProfitIndex]
    minProfitLabel["text"] = "The Minimum Profit Of " + str(minProfit) + " In the month of " + minProfitMonth
    
btn = Button(root, text="Show Profits", command=Profit)

AllMonthsLabel.place(relx = 0.5, rely = 0.2, anchor=CENTER)
ProfitTupleLabel.place(relx = 0.5, rely = 0.3, anchor=CENTER)
maxProfitLabel.place(relx = 0.5, rely = 0.4, anchor=CENTER)
minProfitLabel.place(relx = 0.5, rely = 0.5, anchor=CENTER)
btn.place(relx = 0.5, rely = 0.6, anchor=CENTER)
CopyRightLabelThing.place(relx = 0.5, rely = 0.98, anchor=CENTER)


root.mainloop()