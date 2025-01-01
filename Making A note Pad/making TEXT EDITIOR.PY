from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Initialize the main window
window = Tk()
window.title("Sreinknok")
window.geometry("500x600")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Function to open a file
def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    window.title(f"Sreinknok")
def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath,"w")as output_file:
        text = txt_edit.get(1.0,END)
        output_file.write(text)
    window.title("Sreinknok - {filepath}")
txt_edit = Text(window)
fr_button = Frame(window,relief=RAISED,bd=2)
btn_open = Button(fr_button,text="Open",command=open_file)
btn_save = Button(fr_button,text="Save As....",command=save_file)

btn_open.grid(row=0,column=1,sticky="ew",padx=5,pady=5)
btn_save.grid(row=1,column=0,sticky="ew",padx=5)

fr_button.grid(row=0,column=0,sticky="es")
txt_edit.grid(row=0,column=1,sticky="nsew")
window.mainloop()
