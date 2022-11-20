from tkinter import *
root = Tk()
root.geometry("500x500+150+200")
#side:排列方向:Top,BOTTOM,LEFT,RIGHT

# 建立 label 標籤
mybutton1 = Button (root, text = "West")
mybutton2 = Button (root, text = "East")
mybutton3 = Button (root, text = "East2")

# 加入視窗中
# mybutton1.pack(side = "left")
# mybutton2.pack(side = "right")
# mybutton3.pack(side = "right")

#fill:填滿所分配空間之方向:NONE,X,Y,BOTH
mybutton1.pack(fill = "x")
mybutton2.pack(side = "right",fill = "y")

#expand:填滿容器:True/False
# mybutton1 = Button(root, width = 10)
# mybutton1.pack(fill = "both",expand =0)
# mybutton2 = Button(root, width = 10)
# mybutton2.pack(fill = "both",expand =1)

#padx/pady:元件邊框與容器之距離(px,預設 = 0)
# mybutton1.pack(side = "left",padx = 20)
# mybutton2.pack(side = "right", pady = 30)
#ipadx/ipady:元件內容(文字/圖像)與其邊框之距離(px,預設=0)
# mybutton1.pack(side = "left")
# mybutton2.pack(side = "right")
# mybutton1.pack(side = "left",ipadx = 30)
# mybutton2.pack(side = "right", ipady = 30)


#mybutton2.pack(side = "left")
#mybutton1.pack(side = "top")
#mybutton3.pack(side = "bottom")
mainloop()
