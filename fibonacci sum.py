from tkinter import *
root = Tk()
root.title("fibonacci series")
root.geometry("500x500")

label_series = Label(root, text = "fibonacci series")
input_sum = Entry(root)
label_sum = Label(root)



def fibonacci():
    num = int(input_sum.get())
    firNum = 0
    secNum = 1
    sum = 0
    sum2 = 0
    counter = 1
    while (counter <= num):
        label_series["text"] += str(sum) + " "
        label_sum["text"] = "fibonaccu sum: " + str(sum2)
        counter = counter + 1
        firNum = secNum
        secNum = sum
        sum = firNum + secNum
        sum2 = sum2 + sum
        

btn = Button(root, text = "show fibonnaci series", command = fibonacci)

btn.pack()
input_sum.pack()
label_series.pack()
label_sum.pack()

root.mainloop()

