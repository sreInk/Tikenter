import tkinter as tk
from tkinter import messagebox

# Function to calculate interest
def calculate_interest():
    try:
        # Getting input values
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())
        
        # Calculating Simple Interest
        simple_interest = (principal * rate * time) / 100
        
        # Calculating Compound Interest
        compound_interest = principal * ((1 + rate / 100) ** time) - principal
        
        # Displaying results
        result = f"Simple Interest: ₹{simple_interest:.2f}\nCompound Interest: ₹{compound_interest:.2f}"
        messagebox.showinfo("Interest Calculation", result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numerical values.")

# Setting up the GUI
root = tk.Tk()
root.title("Interest Calculator")

# Labels and Entry fields
tk.Label(root, text="Principal Amount (₹):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Rate of Interest (%):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_rate = tk.Entry(root)
entry_rate.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Time Period (years):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_time = tk.Entry(root)
entry_time.grid(row=2, column=1, padx=10, pady=5)

# Button to calculate
btn_calculate = tk.Button(root, text="Calculate", command=calculate_interest)
btn_calculate.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
