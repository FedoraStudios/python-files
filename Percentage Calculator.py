from tkinter import *


root = Tk()
root.title("Percentage Calculator")
root.geometry("600x600")
root.configure(bg="dark orange")

PercentageLabelOne = Label(root)
PercentageLabelTwo = Label(root)
PercentageLabelThree = Label(root)

class GradeThree():
    
    Percentage = 0
    
    def Calculate(self, marksOne, marksTwo):
        Percentage = ((marksOne + marksTwo) / 200) * 100
        PercentageLabelOne["text"] = str(Percentage)
    
class GradeFive():
    
    Percentage = 0
    
    def Calculate(self, marksOne, marksTwo, marksThree):
        Percentage = ((marksOne + marksTwo) / 300) * 100
        PercentageLabelTwo["text"] = str(Percentage)
    
class GradeNine():
    
    Percentage = 0
    
    def Calculate(self, marksOne, marksTwo, marksThree, marksFour):
        Percentage = ((marksOne + marksTwo) / 400) * 100
        PercentageLabelThree["text"] = str(Percentage)

#calculate seems to be called when the object is created, like __init__, I don't know how to fix it. 
GradeThreeObject = GradeThree()
GradeFiveObject = GradeFive()
GradeNineObject = GradeNine()


PercentageButtonOne = Button(root, text="Grade Three", command=GradeThreeObject.Calculate(60, 100))
PercentageButtonOne.place(relx = 0.5, rely = 0.1, anchor=CENTER)
PercentageLabelOne.place(relx = 0.5, rely = 0.2, anchor=CENTER)

PercentageButtonTwo = Button(root, text="Grade Five", command=GradeFiveObject.Calculate(55, 100, 69))
PercentageButtonTwo.place(relx = 0.5, rely = 0.4, anchor=CENTER)
PercentageLabelTwo.place(relx = 0.5, rely = 0.5, anchor=CENTER)

PercentageButtonThree = Button(root, text="Grade Nine", command=GradeNineObject.Calculate(50, 100, 76, 66))

PercentageButtonThree.place(relx = 0.5, rely = 0.7, anchor=CENTER)
PercentageLabelThree.place(relx = 0.5, rely = 0.8, anchor=CENTER)


root.mainloop()