from tkinter import *
from tkinter import messagebox 
from PIL import Image, ImageTk
root = Tk()
root.geometry("300x200")
def createNewWindow():
    newWindow = Toplevel(root)
    label = Label(root,text = "目前存庫最多只能五件")
    label.pack()
    destroybutton = Button(newWindow,text= "Quit",command=newWindow.destroy)
    destroybutton.pack()

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
label2 = Label(root, image = tk_img).grid(row = 1,column = 0,columnspan =2,rowspan = 3)

label3 = Label(root,text = "沙發組").grid(row = 4,column = 0,sticky = W)

label4 = Label(root,text = "$1200").grid(row = 4,column = 2,sticky = W)

label5 = Label(root,text = "0").grid(row = 5,column = 2,sticky = W+E+N+S)

mystringvar = StringVar()

button1 = Button(root,text = "-",command=minus).grid(row = 3,column = 2,sticky=W)
button2 = Button(root,text = "+",command=add).grid(row = 3,column = 2,sticky=E)


val = StringVar()

def clickradiobtn1():
    selectlabel["textvariable"] = val
def clickradiobtn2():
    selectlabel["textvariable"] = val
def clickradiobtn3():
    selectlabel["textvariable"] = val
    
titlelabel = Label(root,text="Please select the color you want")


radiobtn1 = Radiobutton(root, text="黑色",variable=val,value = "黑色",command=clickradiobtn1)
radiobtn1.grid(row=1,column=2,sticky=W+E+N+S)

radiobtn2 = Radiobutton(root,text="灰色",variable=val,value = "灰色",command=clickradiobtn2)
radiobtn1.grid(row=2,column=2,sticky=W+E+N+S)

radiobtn2.select()

radiobtn3 = Radiobutton(root,text="咖啡色",variable=val,value = "咖啡色",command=clickradiobtn3)
radiobtn1.grid(row=3,column=2,sticky=W+E+N+S)

selectlabel = Label(root,textvariable=val,font=("Arial",20))
selectlabel.pack()





root.mainloop()