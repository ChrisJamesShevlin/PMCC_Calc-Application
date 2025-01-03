import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        long_call_strike = float(long_call_strike_entry.get())
        short_call_strike = float(short_call_strike_entry.get())
        premium_paid = float(premium_paid_entry.get())
        premium_received = float(premium_received_entry.get())

        max_risk = premium_paid - premium_received
        max_profit = (short_call_strike - long_call_strike) - max_risk

        messagebox.showinfo(
            "Results",
            f"Maximum Risk: £{max_risk:.2f}\nMaximum Profit: £{max_profit:.2f}"
        )
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")


# Create the main application window
app = tk.Tk()
app.title("Diagonal Spread Calculator")
app.geometry("400x300")
app.configure(bg="#2C2F33")

# Long Call Strike
long_call_strike_label = tk.Label(app, text="Long Call Strike", bg="#2C2F33", fg="white")
long_call_strike_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
long_call_strike_entry = tk.Entry(app, width=20)
long_call_strike_entry.grid(row=0, column=1, padx=10, pady=10)

# Short Call Strike
short_call_strike_label = tk.Label(app, text="Short Call Strike", bg="#2C2F33", fg="white")
short_call_strike_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
short_call_strike_entry = tk.Entry(app, width=20)
short_call_strike_entry.grid(row=1, column=1, padx=10, pady=10)

# Premium Paid
premium_paid_label = tk.Label(app, text="Premium Paid (£)", bg="#2C2F33", fg="white")
premium_paid_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
premium_paid_entry = tk.Entry(app, width=20)
premium_paid_entry.grid(row=2, column=1, padx=10, pady=10)

# Premium Received
premium_received_label = tk.Label(app, text="Premium Received (£)", bg="#2C2F33", fg="white")
premium_received_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
premium_received_entry = tk.Entry(app, width=20)
premium_received_entry.grid(row=3, column=1, padx=10, pady=10)

# Calculate Button
calculate_button = tk.Button(app, text="Calculate", command=calculate, bg="#7289DA", fg="white", width=15)
calculate_button.grid(row=4, column=0, columnspan=2, pady=20)

# Start the application
app.mainloop()
