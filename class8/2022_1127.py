from tkinter import *
#引入tkinter的messagebox
from tkinter import messagebox 
#引入pillow module
from PIL import Image, ImageTk

root = Tk()

root.title("Class_HW1")

root.geometry("500x500")

mylabel = Label(root, text="點擊按鈕次數計算", fg = "orange",bg = "white", font=("Courier",18,"bold"))

mylabel.pack(pady=50)
#更改button文字內容 way1
# l = 0
# def clicked():
#     global l
#     l = l+1
#     #設定button的text點擊次數
#     mybutton["text"] = "click"+ str (l)
    

# mybutton = Button(root, text ="click", command = clicked)
# mybutton.pack()  
#更改button文字內容 way2
# mystringvar = StringVar()
# mystringvar.set("clicked")
# l = 0
# def clicked():
#     global l
#     l = l+1
#     #設定button的text點擊次數
#     mystringvar.set("click"+str(l))

# mybutton = Button(root, textvariable = mystringvar, command = clicked)

# mybutton.pack()  

#獲取button文字內容 way1
# 建立 計算按鈕次數 label 標籤
# mybutton = Button(root, text ="Hello World")
# mybutton.pack()
# # get mylabe的文字內容
# Label(root,text=mybutton["text"]).pack()
#獲取button文字內容 way2
#建立stringvar
# mystringvar = StringVar()
# mystringvar.set("Hello World!")
# # 建立建立 計算按鈕次數 label 標籤
# mybutton = Button(root, textvariable= mystringvar)
# mybutton.pack()
# #get mylabel的文字標籤
# Label(root,text = mystringvar.get()).pack

#label搭配image
# img = Image.open("/Users/silvia/Documents/Python_2022Autumn/class8/corgi1.jpg")
# #更改圖片大小
# resized_image = img.resize((100,100))
# #轉換為tk圖片圖片物件
# tk_img = ImageTk.PhotoImage(resized_image)
# # 在label放入圖片
# label = Label(root, image = tk_img)
# label.pack()
#在button裡放入圖片
# mybutton = Button(root, image = tk_img)
# mybutton.pack()

#pop up messagebox
#出現問題訊息框
# messagebox.askquestion("askquestion","Is it sunday")
# #出現"message test"的普通訊息
# messagebox.showinfo("showfin","message test")

# result = messagebox.askquestion("askquestion","Is it Sunday?")
# print("User click "+result)

val = StringVar()

radiobtn1 = Radiobutton(root, text="Black",variable=val,value="Black")
radiobtn1.pack()
#指定選取第一個單選按鈕
radiobtn1.select()
#放入第二個單選按鈕
radiobtn2 = Radiobutton(root,text="Red",variable=val,value="Red")
radiobtn2.pack()

root.mainloop()