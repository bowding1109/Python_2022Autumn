from tkinter import *

root = Tk()

root.title("Class_HW1")

root.geometry("400x400+150+200")

mylabel = Label(root, text="點擊按鈕次數計算", fg = "orange",bg = "white", font=("Courier",18,"bold"))

mylabel.pack(pady=50)

l = 0
def clicked():
    global l
    l = l+1
    label1 = Label(root, text = l)
    label1.pack()

mybutton = Button(root, text = "Click me", command = clicked)
mybutton.pack()  

root.mainloop()