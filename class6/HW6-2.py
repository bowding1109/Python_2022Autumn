from tkinter import*

root = Tk()

root.title("Class6")
root.geometry("350x100")


menu = Menu(root)

menubar1 = Menu(menu)
menubar1.add_command(label="Open")
menubar1.add_command(label="Execute")
menubar1.add_command(label="Close")

menu.add_cascade(label="File",menu=menubar1)

menubar2 = Menu(menu)
menubar2.add_command(label="AAA")
menubar2.add_command(label="BBB")



menubar2.add_separator()

menubar2more = Menu(menubar1)
menubar2more.add_command(label="X")
menubar2more.add_command(label="Y")


menubar2.add_cascade(label="File",menu=menubar2more)

menu.add_cascade(label ="Triple",menu=menubar2)

root.config(menu=menu)

root.mainloop()