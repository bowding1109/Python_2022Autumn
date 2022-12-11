from tkinter import *
from tkinter import messagebox 
from PIL import Image, ImageTk

root = Tk()

root.title("KubeTech Shop")

root.geometry("880x650")
#row = 0
titleimg = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/image/logo_tree.png")
titleimg = titleimg.resize((32,32))
titleimg = ImageTk.PhotoImage(titleimg)
titlelabel = Label(root, image = titleimg,width = 32,height = 32).grid(column = 0,row = 0,sticky=W)

sofabutton = Button(root,font = ("Inter",18), text="沙發", fg = "#1E1E1E",bg = "#ECE8E7", width = 5,pady=2,)
sofabutton.grid(column=1,row=0,sticky = E+W,padx=5)

beddingbutton = Button(root,font = ("Inter",18), text="寢具", fg = "#1E1E1E",bg = "#ECE8E7", width = 5,pady=2,)
beddingbutton.grid(column=2,row=0,sticky = E+W,padx=5)

kitchenwarebutton = Button(root,font = ("Inter",18), text="廚具", fg = "#1E1E1E",bg = "#ECE8E7", width = 5,pady=2,)
kitchenwarebutton.grid(column=3,row=0,sticky = E+W,padx=5)

loginbutton = Button(root,font = ("Inter",18), text="會員登入/註冊", fg = "#1E1E1E",bg = "#ECE8E7", width = 12,padx=5,)
loginbutton.grid(column=7,row=0,sticky = E+W,padx=5)
#row=1
bannerimg = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/image/banner.jpg")
bannerimg = bannerimg.resize((852,298))
bannerimg = ImageTk.PhotoImage(bannerimg)
bannerlabel = Label(root, image = bannerimg).grid(column = 0, row= 1,columnspan=8,sticky=W,padx = 5)

#row=2
sofa1img = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/image/sofa1.jpg")
sofa1img = sofa1img.resize((202,200))
sofa1img = ImageTk.PhotoImage(sofa1img)
sofa1label = Label(root, image = sofa1img).grid(column = 0,row = 2,columnspan=2,sticky=W,padx = 5)

sofa2img = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/image/sofa2.jpg")
sofa2img = sofa2img.resize((202,200))
sofa2img = ImageTk.PhotoImage(sofa2img)
sofa2label = Label(root, image = sofa2img).grid(column = 2,row = 2,columnspan=2,sticky=W,padx = 5)

sofa3img = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/image/sofa3.jpg")
sofa3img = sofa3img.resize((202,200))
sofa3img = ImageTk.PhotoImage(sofa3img)
sofa3label = Label(root, image = sofa3img).grid(column = 4,row = 2,columnspan=2,sticky=W,padx = 5)

sofa4img = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/image/sofa4.jpg")
sofa4img = sofa4img.resize((202,200))
sofa4img = ImageTk.PhotoImage(sofa4img)
sofa4label = Label(root, image = sofa4img).grid(column = 6,row = 2,columnspan=2,sticky=W,padx = 5)

#row=3
productname1 = Label(root,font = ("Inter",11), text="三人座沙發, grann/bomstad 黑色/金屬", fg = "#000000",bg = "#ECE8E7")
productname1.grid(column=0,row=3,columnspan=2 ,padx=5)

productname2 = Label(root,font = ("Inter",11), text="三人座沙發, grann/bomstad 黑色/木材", fg = "#000000",bg = "#ECE8E7")
productname2.grid(column=2,row=3,columnspan=2,padx=5)

productname3 = Label(root,font = ("Inter",11), text="三人座沙發, grann/bomstad 米色/金屬", fg = "#000000",bg = "#ECE8E7")
productname3.grid(column=4,row=3,columnspan=2,padx=5)

productname4 = Label(root,font = ("Inter",11), text="三人座沙發, grann/bomstad 米色/木頭", fg = "#000000",bg = "#ECE8E7")
productname4.grid(column=6,row=3,columnspan=2,padx=5)

#row=4
productprice = Label(root,font = ("Inter",10), text="NT.28,900", fg = "#000000",bg = "#ECE8E7")
productprice.grid(column=0,row=4 ,padx=5)

product1price = Label(root,font = ("Inter",10), text="NT.28,900", fg = "#000000",bg = "#ECE8E7")
product1price.grid(column=2,row=4 ,padx=5)

product1price = Label(root,font = ("Inter",10), text="NT.28,900", fg = "#000000",bg = "#ECE8E7")
product1price.grid(column=4,row=4 ,padx=5)

product1price = Label(root,font = ("Inter",10), text="NT.28,900", fg = "#000000",bg = "#ECE8E7")
product1price.grid(column=6,row=4 ,padx=5)

productnumberlabel1 = Label(root,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
productnumberlabel1.grid(column=1,row=4,sticky=E+W)

productnumberlabel2 = Label(root,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
productnumberlabel2.grid(column=3,row=4,sticky=E+W)

productnumberlabel3 = Label(root,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
productnumberlabel3.grid(column=5,row=4,sticky=E+W)

productnumberlabel4 = Label(root,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
productnumberlabel4.grid(column=7,row=4,sticky=E+W)

addbutton1 = Button(root,font = ("Inter",10), text="+", fg = "#1E1E1E",bg = "#E7E2E2")
addbutton1.grid(column=1,row=4 ,sticky=E)

addbutton2 = Button(root,font = ("Inter",10), text="+", fg = "#1E1E1E",bg = "#E7E2E2")
addbutton2.grid(column=3,row=4 ,sticky=E)

addbutton3 = Button(root,font = ("Inter",10), text="+", fg = "#1E1E1E",bg = "#E7E2E2")
addbutton3.grid(column=5,row=4 ,sticky=E)

addbutton4 = Button(root,font = ("Inter",10), text="+", fg = "#1E1E1E",bg = "#E7E2E2")
addbutton4.grid(column=7,row=4 ,sticky=E)

minusbutton1 = Button(root,font = ("Inter",10), text="-", fg = "#1E1E1E",bg = "#E7E2E2")
minusbutton1.grid(column=1,row=4 ,sticky=W)

minusbutton2 = Button(root,font = ("Inter",10), text="-", fg = "#1E1E1E",bg = "#E7E2E2")
minusbutton2.grid(column=3,row=4 ,sticky=W)

minusbutton3 = Button(root,font = ("Inter",10), text="-", fg = "#1E1E1E",bg = "#E7E2E2")
minusbutton3.grid(column=5,row=4 ,sticky=W)

minusbutton4 = Button(root,font = ("Inter",10), text="-", fg = "#1E1E1E",bg = "#E7E2E2")
minusbutton4.grid(column=7,row=4 ,sticky=W)

root.mainloop()
