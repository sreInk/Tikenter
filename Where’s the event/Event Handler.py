from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry("300x400")
def handle_key(event):
    print(event.char)
window.bind("<Key>",handle_key)
def handle_click(event):
    print("The button was clicked")
button = Button(text="Click me")
button.pack()
button.bind("<Button-1>",handle_click)
window.mainloop()