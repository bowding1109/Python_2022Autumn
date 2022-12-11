from tkinter import *
from tkinter import messagebox 
from PIL import Image, ImageTk

root = Tk()

root.title("Class_HW1")

root.geometry("300x200")

val = StringVar()
# #label顏色一顏色內容更換
def clickradiobtn1():
    selectlabel["fg"] = "Blue"
    selectlabel["textvariable"] = val
def clickradiobtn2():
    selectlabel["fg"] = "Green"
    selectlabel["textvariable"] = val
def clickradiobtn3():
    selectlabel["fg"] = "Pink"
    selectlabel["textvariable"] = val
titlelabel = Label(root,text="Please select the color you want")
titlelabel.pack()
# #放入第一個單選按鈕
radiobtn1 = Radiobutton(root, text="Blue",variable=val,value="Blue",command=clickradiobtn1)
radiobtn1.pack()
#放入第二個單選按鈕
radiobtn2 = Radiobutton(root,text="Green",variable=val,value="Green",command=clickradiobtn2)
radiobtn2.pack()
#選定第二個單選按鈕
radiobtn2.select()
#放入第三個單選按鈕
radiobtn3 = Radiobutton(root,text="Pink",variable=val,value="Pink",command=clickradiobtn3)
radiobtn3.pack()

selectlabel = Label(root,textvariable=val,font=("Arial",20))
selectlabel.pack()


#點擊button跳出New Windows
# def createNewWindow():
# #建立新視窗New Windows
#     newWindow = Toplevel(root)
# #建立新label在New Windows裡
#     mylabel = Label(newWindow,text="New Window")
#     mylabel.pack()
# #建立新button在New Windows裡
#     # mybutton = Button(newWindow,text= "New Window button")
#     # mybutton.pack()
# #建立destory button在New Windows裡
#     destroybutton = Button(newWindow,text= "Quit",command=newWindow.destroy)
#     destroybutton.pack()
# #建立hide button 在New Windows裡
#     hidebutton = Button(newWindow,text = "Hide",command = root.iconify)
#     hidebutton.pack()
# #建立show button在New Windows裡
#     showbutton = Button(newWindow,text = "Show",command = root.deiconify)
#     showbutton.pack()
# #建立withdraw button 在New Windows裡
#     withdrawbutton = Button(newWindow,text = "Withdraw Main Window",command = root.withdraw)
#     withdrawbutton.pack()

#     newWindow.mainloop()

# #點擊button產生New Windows
# creatnewwindowbtn = Button(root, text="Click to Create New Windows!",command=createNewWindow)
# creatnewwindowbtn.pack()
#預設值
# def function(n, a=1, b=2):
#     print(n+a+b)
# #呼叫執行funtion，並給三個參數傳入該function
# function(1,2,3)# result:6 -> 1+2+3 = 6

# #呼叫執行function，只給一個參數傳入該function
# #當只給一個參數時，其餘參數會自動依照預設值來填入
# function(4)# result:7 -> 4+1+2 = 7
# #可變參數
# def funtion(n, *args):
#     print(n)
#     print(args)

# #呼叫執行function，並給多個(>2個)參數直傳入該function
# #除了1為變數n外，其餘都是*args的輸入值
# function(1,2,3,4,5,6,7)

# def function(*args,**kwargs):
#     print(kwargs)
#     print(args)
# #呼叫執行function，並給多個(>2個)參數直傳入該function
# #前四個值為*args可變參數，後兩個值為**kwargs關鍵字可變參數
# funtion(1,2,3,4,num1 = 5,num2=10)
root.mainloop()
