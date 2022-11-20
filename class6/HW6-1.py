from tkinter import *
root = Tk()
root.geometry("200x100")

label1 = Label(root,text = "kube shop").grid(row = 0,column = 0,columnspan =4,sticky = W+E+N+S)
label2 = Label(root,text = "戶外餐桌椅組").grid(row = 1,column = 0,columnspan =2,sticky = W)
label3 = Label(root,text = "NT.1200").grid(row = 2,column = 0,sticky = W)
label4 = Label(root,text = "0").grid(row = 3,column = 1,sticky = W)
button1 = Button(root,text = "+").grid(row = 3,column = 0,sticky = W)
button2 = Button(root,text = "-").grid(row = 3,column = 2,sticky = W)



root.mainloop()