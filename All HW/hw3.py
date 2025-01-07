import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to calculate age
def calculate_age():
    try:
        # Get user input
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())
        
        # Get the current date
        today = datetime.today()
        
        # Calculate age
        birth_date = datetime(year, month, day)
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        # Display result
        messagebox.showinfo("Age Calculation", f"Your age is: {age} years.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numerical values for day, month, and year.")

# Setting up the GUI
root = tk.Tk()
root.title("Age Calculator")

# Labels and Entry fields for Day, Month, and Year
tk.Label(root, text="Day of Birth (1-31):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_day = tk.Entry(root)
entry_day.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Month of Birth (1-12):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_month = tk.Entry(root)
entry_month.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Year of Birth:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root)
entry_year.grid(row=2, column=1, padx=10, pady=5)

# Button to calculate age
btn_calculate = tk.Button(root, text="Calculate Age", command=calculate_age)
btn_calculate.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
