#引入 tkinter module
from tkinter import*

root = Tk()
root.title("Class7")
root.geometry("350x100")

#加入Frame框架
# frame = Frame(root)
# frame.pack()

# #將Label放在指定的Frame裡
# label = Label(frame, text = "Hello World")
# label.pack()

# #Frame元件
# frame1 = Frame(root, pady = 5, padx=20, bg = "lightblue")
# frame2 = Frame(root, pady = 20, padx=10, bg = "pink")
# #放到framel1裡的label1
# label1 = Label(frame1, text="hello",width=10)
# label1.pack()
# #放到frame2裡的label
# label2 = Label(frame2, text="world",width=20)
# label2.pack()

# #先放frame2
# frame2.pack()
# #先放frame2
# frame1.pack()

#更改label文字內容
#建立StringVar
# mystringvar = StringVar()
# mystringvar.set("Hello world!")
# #建立計算按鈕次數label標籤
# mylabel = Label(root,textvariable=mystringvar)
# mylabel.pack()

#獲取label文字內容
#way1
# mylabel = Label(root,text = "Hellow World")
# mylabel.pack()
# # get mylabel的文字內容
# Label(root, text=mylabel["text"]).pack()
#way2
#建立StringVar
mystrinvgar = StringVar()
mystrinvgar.set("Hello World!")
#建立計算紐次數label標籤
mylabel = Label(root,textvariable=mystrinvgar)
mylabel.pack()
#get mylabel的文字內容
Label(root, text= mystrinvgar.get()).pack()


#執行主程式
root.mainloop()