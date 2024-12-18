from tkinter import *
from datetime import date
root = Tk()
root.title('Root of Groot')
root.geometry('300x400')
bl= Label(text="hey Ther!",fg='white',height=1,width= 300)
name_bl = Label(text= 'Full Form',bg = "#30245D")
name_entry = Entry()
def display():
    name = name_entry.get()
    global message
    message = "Welcome to all to aplication \nToday 's date is: "
    greet = "hello "+name + "\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box = Text(height=3)
btn = Button(text= "begin",command=display,height=1,bg="#1261A0",fg='white')

bl.pack()
name_bl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()