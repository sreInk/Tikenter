import tkinter as tk
from tkinter import messagebox

# Function to convert inches to centimeters
def convert_to_cm():
    try:
        # Getting the input value
        inches = float(entry_inches.get())
        
        # Conversion formula
        centimeters = inches * 2.54
        
        # Display the result
        messagebox.showinfo("Conversion Result", f"{inches} inches is equal to {centimeters:.2f} centimeters.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numerical value.")

# Setting up the GUI
root = tk.Tk()
root.title("Inches to Centimeters Converter")

# Label and Entry field
tk.Label(root, text="Length in Inches:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_inches = tk.Entry(root)
entry_inches.grid(row=0, column=1, padx=10, pady=5)

# Button to convert
btn_convert = tk.Button(root, text="Convert", command=convert_to_cm)
btn_convert.grid(row=1, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
