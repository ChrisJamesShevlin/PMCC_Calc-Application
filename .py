import tkinter as tk
from tkinter import messagebox

# Function to calculate max risk and max profit
def calculate():
    try:
        # Get user inputs
        long_strike = float(long_strike_entry.get())
        short_strike = float(short_strike_entry.get())
        premium_paid = float(premium_paid_entry.get())
        premium_received = float(premium_received_entry.get())
        
        # Calculate max risk and max profit
        net_debit = premium_paid - premium_received
        max_risk = net_debit
        max_profit = (short_strike - long_strike) - net_debit
        
        # Display results
        result_text.set(f"Maximum Risk: £{max_risk:.2f}\nMaximum Profit: £{max_profit:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Diagonal Spread Calculator")
root.geometry("400x300")
root.configure(bg="#1e1e2e")

# Result display variable
result_text = tk.StringVar()

# Create and place widgets
tk.Label(root, text="Long Call Strike", bg="#1e1e2e", fg="white").grid(row=0, column=0, pady=5, padx=10, sticky="w")
long_strike_entry = tk.Entry(root, width=20)
long_strike_entry.grid(row=0, column=1, pady=5, padx=10)

tk.Label(root, text="Short Call Strike", bg="#1e1e2e", fg="white").grid(row=1, column=0, pady=5, padx=10, sticky="w")
short_strike_entry = tk.Entry(root, width=20)
short_strike_entry.grid(row=1, column=1, pady=5, padx=10)

tk.Label(root, text="Premium Paid (£)", bg="#1e1e2e", fg="white").grid(row=2, column=0, pady=5, padx=10, sticky="w")
premium_paid_entry = tk.Entry(root, width=20)
premium_paid_entry.grid(row=2, column=1, pady=5, padx=10)

tk.Label(root, text="Premium Received (£)", bg="#1e1e2e", fg="white").grid(row=3, column=0, pady=5, padx=10, sticky="w")
premium_received_entry = tk.Entry(root, width=20)
premium_received_entry.grid(row=3, column=1, pady=5, padx=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate, bg="#007acc", fg="white")
calculate_button.grid(row=4, column=0, columnspan=2, pady=20)

result_label = tk.Label(root, textvariable=result_text, bg="#1e1e2e", fg="white", font=("Helvetica", 12))
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
