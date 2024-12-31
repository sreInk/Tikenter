from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("Window Name","Text to be displayed ")
buttom = Button(root,text= 'Scan for Virus',command=msg )
buttom.place(x=40,y=80)
root.mainloop()