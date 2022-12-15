from tkinter import *
root=Tk()
root.title("Login")
root.config(bg="grey")
root.geometry("400x400")

NameEnt = Entry(root, text="Name", fg="black")
PasswordEnt = Entry(root, text="Password", fg="black")
CaptchaEnt = Entry(root, text="9xY4c7", fg="black")


labName = Label(root)
labPassword = Label(root)
labCaptcha = Label(root)

class UserDB():
    def __init__(self):
        self.__name="Emir R. Frias Suzuki"
        self.__Password="ikuzuS sairF .R rimE"
        self.Captcha="Mx3z6y"
        
    def showUser(self):
        labName["text"] = "Name: " + self.__name
        labPassword["text"] = "Password: " + self.__Password
        labCaptcha["text"] = "Captcha: " + self.Captcha
        
OBJuserDB = UserDB()
        
LoginBTN = Button(root, text="Login")
ShowProfileBTN = Button(root, text="Show Profile", command=OBJuserDB.showUser)


NameEnt.place(relx = 0.3, rely = 0.3, anchor=CENTER)
PasswordEnt.place(relx = 0.6, rely = 0.3, anchor=CENTER)    
CaptchaEnt.place(relx = 0.5, rely = 0.4, anchor=CENTER)   
 
labName.place(relx = 0.5, rely = 0.5, anchor=CENTER)    
labPassword.place(relx = 0.5, rely = 0.6, anchor=CENTER)    
labCaptcha.place(relx = 0.5, rely = 0.7, anchor=CENTER) 
   
LoginBTN.place(relx = 0.5, rely = 0.8, anchor=CENTER)    
ShowProfileBTN.place(relx = 0.5, rely = 0.9, anchor=CENTER)    

root.mainloop()