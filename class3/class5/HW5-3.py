from tkinter import *
root = Tk()
root.geometry("200x100")

label1 = Label(root,text = "三人座沙發/綠色/灰色/黑色")
label2 = Label(root,text = "NT.28900")
label3 = Label(root,text = "0")
button1 = Button(root,text = "+")
button2 = Button(root,text = "-")
label1.pack(side = "top")
label2.pack(side = "left")
button1.pack(side = "right")
label3.pack(side = "right")
button2.pack(side = "right")

mainloop()