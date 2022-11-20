from tkinter import *
root = Tk()
root.geometry("500x500+150+200")

mybutton1 = Button (root, text = "West")
mybutton2 = Button (root, text = "East")
mybutton3 = Button (root, text = "East2")

mybutton2.pack(side = "left")
mybutton1.pack(side = "top")
mybutton3.pack(side = "bottom")
mainloop()