from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Fever Report")
root.geometry("600x600")
root.configure(bg = "royal blue")

QuestionOneRadioButton = StringVar(value = "0")
QuestionOne = Label(root, text = "Do you experience shortness of breath during activites?")
QuestionOne.pack()
QuestionOneR1 = Radiobutton(root, text = "Yes", variable = QuestionOneRadioButton, value = "Yes")
QuestionOneR1.pack()
QuestionOneR2 = Radiobutton(root, text="No", variable = QuestionOneRadioButton, value = "No")
QuestionOneR2.pack()


QuestionTwoRadioButton = StringVar(value = "0")
QuestionTwo = Label(root, text = "Do you have swelling in the feet/ankles/legs (shoes feel tighter) or abdomen areas?")
QuestionTwo.pack()
QuestionTwoR1 = Radiobutton(root, text = "Yes", variable = QuestionTwoRadioButton, value = "Yes")
QuestionTwoR1.pack()
QuestionTwoR2 = Radiobutton(root, text="No", variable = QuestionTwoRadioButton, value = "No")
QuestionTwoR2.pack()


QuestionThreeRadioButton = StringVar(value = "0")
QuestionThree = Label(root, text = "Do you expierence any of the following: Confusion, disorientation, or loss of memoy?")
QuestionThree.pack()
QuestionThreeR1 = Radiobutton(root, text = "Yes", variable = QuestionThreeRadioButton, value = "Yes")
QuestionThreeR1.pack()
QuestionThreeR2 = Radiobutton(root, text="No", variable = QuestionThreeRadioButton, value = "No")
QuestionThreeR2.pack()


QuestionFourRadioButton = StringVar(value = "0")
QuestionFour = Label(root, text = "Do you expierence have diffucalty breathing while rest?")
QuestionFour.pack()
QuestionFourR1 = Radiobutton(root, text = "Yes", variable = QuestionFourRadioButton, value = "Yes")
QuestionFourR1.pack()
QuestionFourR2 = Radiobutton(root, text="No", variable = QuestionFourRadioButton, value = "No")
QuestionFourR2.pack()


QuestionFiveRadioButton = StringVar(value = "0")
QuestionFive = Label(root, text = "Do you expierence peresistent wheezing/coughing that produces white or pink blood tinged mucus?")
QuestionFive.pack()
QuestionFiveR1 = Radiobutton(root, text = "Yes", variable = QuestionFiveRadioButton, value = "Yes")
QuestionFiveR1.pack()
QuestionFiveR2 = Radiobutton(root, text="No", variable = QuestionFiveRadioButton, value = "No")
QuestionFiveR2.pack()

def FeverScore():
    Score = 0
    if QuestionOneRadioButton.get() == "Yes":
        Score = Score + 20
        print(Score)
        
    if QuestionTwoRadioButton.get() == "Yes":
        Score = Score + 20
        print(Score)
        
    if QuestionThreeRadioButton.get() == "Yes":
        Score = Score + 20
        print(Score)
        
    if QuestionFourRadioButton.get() == "Yes":
         Score = Score + 20
         print(Score)
         
    if QuestionFiveRadioButton.get() == "Yes":
         Score = Score + 20
         print(Score)
    if Score <= 20:
        messagebox.showinfo("Report", "You Don't need to visit a doctor.")
        
    
    elif Score == 60 and Score == 40:
        messagebox.showinfo("Report", "You might be required to visit a doctor.")
        
        
    else:
        messagebox.showinfo("report", "It is strongly recomended to visit a doctor.")
        
AnswerButton = Button(root, text = "Click For Report", command=FeverScore)
AnswerButton.pack()

root.mainloop()