#引入Tkinter module
from tkinter import *
# 建立主視窗 Frame
root = Tk()
#設定視窗標題
root.title("Hellow World")
# 設定視窗大小為 300x100 視窗(左上角) 在螢幕上的座標位置為(500, 150)
root.geometry("300x100+500+150")
#寫法一
#建立 label 標籤
mylabel = Label(root, text="hellow world", fg = "blue",bg = "yellow", font=("Pilgi",20,"bold"))
#加入視窗中
mylabel.pack(pady=50)

# Label(root, text="secound world").pack(pady=20)

# 建立 button 按鈕
# mybutton = Button(root, text = "Click me !")
#加入視窗中
# mybutton.pack()
# 點擊按鈕函數function
def clicked():
    label1 = Label(root, text = "Button is clicked")
    label1.pack()
def a():
    f = Label(root, text = e.get())
    f.pack()
    # 建立 button 按鈕
mybutton = Button(root, text = "Click me", command = clicked)
mybutton.pack()  
#建立 Input Entry Boxed
e = Entry(root, width = 30, font=("comic Sans Ms", 16))
# 加入視窗中
e.pack()
#建立 button 按鈕
Enterbutton = Button(root, text="Enter!", command = a)
# 加入視窗中
Enterbutton.pack()

# 建立主程式
root.mainloop()





