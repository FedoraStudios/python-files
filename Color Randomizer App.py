from tkinter import *
import random
root = Tk()
root.config(bg="grey")
root.title("Color Randomizer")
root.geometry("400x400")

#self.text = ["RED", "BLUE", "GREEN", "YELLOW", "PINK",  "BLACK"]
#self.randomValText = random.randint(0, 5)

#self.Color = ["red", "blue", "green", "yellow", "pink",  "black"]
#self.randomValCol = random.randint(0, 5)


LabelScore = Label(root, bg="grey", text="Score: 0", fg="cyan", font=("Bahnschnrift Light", 15))
LabelScore.place(relx=0.1, rely=0.03, anchor=CENTER)

LabelName = Label(root, bg="grey", fg="cyan", font=("Bahnschnrift Light", 15))
LabelName.place(relx=0.3, rely=0.3, anchor=CENTER)

Input_Value = Entry(root, bg="grey")
Input_Value.place(relx=0.48, rely=0.45, anchor=CENTER)

class Game():
    def __init__(self):
        self.__score = 0
        
    def updateGame(self):
        self.text = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "White", "Black"]
        self.randomValText = random.randint(0, 8)

        self.Color = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "White", "Black"]
        self.randomValCol = random.randint(0, 8)
        
        LabelName["text"] = self.text[self.randomValText]
        LabelName["fg"] = self.Color[self.randomValCol]
        
    def __updateScore(self, InputValue):
        print("E2")
        
        if(InputValue == self.Color[self.randomValCol]):
            print(self.Color[self.randomValCol])
            print("E3")
            
            self.__score = self.__score + random.randint(0, 10)
            LabelScore["text"] = "Score: " + str(self.__score)
            
    def getUserValue(self, InputValue):
        self.__updateScore(InputValue)    
    

GameClassObj = Game()


def getInput():
    print("E")
    value = Input_Value.get()
    GameClassObj.getUserValue(value)
    GameClassObj.updateGame()
    Input_Value.delete(0, END)


btnStart = Button(root, text="Start", bg="green", fg="black", command = GameClassObj.updateGame())
btnStart.place(relx=0.65, rely=0.65, anchor=CENTER)

btnCheck = Button(root, text="Check", bg="white", fg="black", command = getInput)
btnCheck.place(relx=0.35, rely=0.65, anchor=CENTER)


root.mainloop()


