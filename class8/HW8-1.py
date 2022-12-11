from tkinter import *
from tkinter import messagebox 
from PIL import Image, ImageTk
root = Tk()
root.geometry("300x200")

def add():
    #numlable的text+1
    label5["text"] = int(label5("text"))+1
def minus():
    #當numlabel大於0時，才會進行減1
    if int(label5["text"])>0:
        #numlabel的text-1
        label5["text"] = int(label5["text"])-1


label1 = Label(root,text = "kube shop").grid(row = 0,column = 0,columnspan =4,sticky = W+E+N+S)

img = Image.open("/Users/silvia/Documents/Python_2022Autumn/class8/sofa.jpg")
resized_image = img.resize((150,100))
tk_img = ImageTk.PhotoImage(resized_image)
label2 = Label(root, image = tk_img).grid(row = 1,column = 0,columnspan =2)

label3 = Label(root,text = "沙發組").grid(row = 2,column = 0,columnspan =2,sticky = W)

label4 = Label(root,text = "$1200").grid(row = 2,column = 2,sticky = W)

label5 = Label(root,text = "0").grid(row = 3,column = 2,sticky = W+E+N+S)

mystringvar = StringVar()
button1 = Button(root,text = "-",command=minus).grid(row = 3,column = 2,sticky=W)
button2 = Button(root,text = "+",command=add).grid(row = 3,column = 2,sticky=E)

root.mainloop()