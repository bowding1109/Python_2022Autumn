from tkinter import *
import datetime
root = Tk()

root.title("Class_HW1")

root.geometry("400x400+150+200")

c = Label(root, text="Enter your birth date:")
c.pack()
b = Label(root, text="Input format is yyyy.mm.dd")
b.pack

enterbox = Entry(root,width = 30,font = ("Arial",18,"bold"))
enterbox.pack()

def count():
    time_string = enterbox.get()
    t1 = datetime.strptime(time_string,"%Y.%m.%d")
    t2 = datetime.now()
    result = t2.year - t1.year
    label = Label(root, text = "You are"+str(result)+"year old.")
    label.pack()



Enterbutton = Button(root, text="Enter!", command = a)
Enterbutton.pack()

root.mainloop()