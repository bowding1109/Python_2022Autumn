# anchor:元件在容器中的錨定位置,E,W,S,N,Center(預設),NE,SE,SW,NW
from tkinter import*
#建立主視窗Frame
root = Tk()
#設定視窗標題
root.title("Class6")
root.geometry("350x100")
#row:列索引
# mybutton1 = Button(root, text="東").pack(anchor=E)
# mybutton2 = Button(root, text="西").pack(anchor=W)
# mybutton3 = Button(root, text="南").pack(anchor=S)
# mybutton4 = Button(root, text="北").pack(anchor=N)
# mybutton5 = Button(root, text="東南").pack(anchor=SE)
# mybutton6 = Button(root, text="西北").pack(anchor=NW)


# mybutton1 = Button(root, text="mybutton1").grid(row = 0,column = 0)
# mybutton2 = Button(root, text="mybutton2").grid(row = 0,column = 1)
# mybutton3 = Button(root, text="mybutton3").grid(row = 0,column = 2)

# mybutton4 = Button(root, text="mybutton4").grid(row = 1,column = 0)
# mybutton5 = Button(root, text="mybutton5").grid(row = 1,column = 2)
# mybutton6 = Button(root, text="mybutton6").grid(row = 2,column = 1)

# mybutton1 = Button(root, text="mybutton1").grid(row = 0,column = 0)
# mybutton2 = Button(root, text="mybutton2").grid(row = 0,column = 1)
# mybutton3 = Button(root, text="mybutton3").grid(row = 0,column = 2)

# mybutton4 = Button(root, text="mybutton4").grid(row = 1,column = 0,columnspan=2)
# mybutton5 = Button(root, text="mybutton5").grid(row = 1,column = 2)

# mybutton1 = Button(root, text="mybutton1").grid(row = 0,column = 0)
# mybutton2 = Button(root, text="mybutton2").grid(row = 0,column = 1)
# mybutton3 = Button(root, text="mybutton3").grid(row = 0,column = 2)

# mybutton4 = Button(root, text="mybutton4").grid(row = 1,column = 0,columnspan=2,sticky=W+E)


# labelWidth = Label(root, text = "width")
# labelWidth.grid(row=0,column=0,sticky = W+N+S)

# labelHeight = Label(root, text = "Height")
# labelHeight.grid(row=1,column=0,sticky = W+N+S)

# entryWidth = Entry(root,width=20)
# entryHeight = Entry(root, width=20)

# entryWidth.grid(row=0, column = 1,sticky = N+S)
# entryHeight.grid(row=1, column = 1,sticky = N+S)

# resultButton = Button(root,text = "Result")
# resultButton.grid(row=0, column = 2,columnspan=2,rowspan = 2,sticky = W+E+N+S)

# menubar = Menu(root)

# filemenu = Menu(menubar)

# filemenu.add_command(label="Open")
# filemenu.add_command(label="Save")
# filemenu.add_command(label="Exit")

# menubar.add_cascade(label="File", menu=filemenu)

# root.config(menu=menubar)

#建立主選單
# menu = Menu(root)
# #建立第一個選單的子選單，有三個選項
# menubar1 = Menu(menu)
# menubar1.add_command(label="Open")
# menubar1.add_command(label="Save")
# menubar1.add_command(label="Exit")
# #建立第一個選單 File，綁定子選單
# menu.add_cascade(label="File",menu=menubar1)
# #建立第二個選單的子選單，有三個選項
# menubar2 = Menu(menu)
# menubar2.add_command(label="AAA")
# menubar2.add_command(label="BBB")
# menubar2.add_command(label="CCC")
# #子選單分隔線
# menubar2.add_separator()
# #建立子選單內的子選單，有三個選項
# menubar2more = Menu(menubar2)
# menubar2more.add_command(label="X")
# menubar2more.add_command(label="Y")
# menubar2more.add_command(label="Z")
# menubar2.add_cascade(label="File",menu=menubar2more)
# #建立第二個選單File，綁定子選單
# menu.add_cascade(label = "Test",menu=menubar2)
# #主視窗加入主選單
# root.config(menu=menu)
#rowspan:儲存格合並行數
#sticky:元件於網格中的確實位置E,W,S,N,Center(預設),NE,SE,SW,NW

def open():
    print("open")
    menubar.entryconfig('Save', state = "normal")
def save():
    print("save")
def exit():
    print("exit")
    menubar.entryconfig("Save",state="disabled")

menu = Menu(root)
menubar = Menu(menu)
menubar.add_command(label="Open",command = open, state = "normal")
menubar.add_command(label ="Save", command = save, state = "disable")
menubar.add_command(label ="Exit", command = exit)
menu.add_cascade(label = "File", menu=menubar)

root.config(menu=menu)

menubar.add_command(label = "Open", command = open, accelerator="Command+O")
menubar.add_command(label = "Save", command = save, accelerator="Command+S")
menubar.add_command(label = "Exit", command = exit, accelerator="Command+E")
menu.add_cascade(label = "File", menu = menubar)

root.bind_all("<Command-o>",open)
root.bind_all("<Command-s>",save)
root.bind_all("<Command-e>",exit)

root.mainloop()