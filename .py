import tkinter as tk
from tkinter import ttk

def calculate_stake():
    try:
        # Get input values
        etf1_price = float(etf1_entry.get())
        etf2_price = float(etf2_entry.get())
        etf2_stake = float(min_stake_entry.get())
        account_balance = float(account_balance_entry.get())
        etf1_margin = float(etf1_margin_entry.get())
        etf2_margin = float(etf2_margin_entry.get())
        
        # Calculate the required stake per point for ETF1 to balance monetary exposure
        etf1_stake = round(etf2_stake * (etf2_price / etf1_price), 2)
        
        # Calculate new ETF sizes using 25% of margin
        total_margin = etf1_margin + etf2_margin
        available_margin = account_balance * 0.25
        scaling_factor = available_margin / total_margin
        new_etf1_size = round(etf1_stake * scaling_factor, 2)
        new_etf2_size = round(etf2_stake * scaling_factor, 2)
        
        # Display the results
        result_label.config(
            text=f"To balance:\n"
                 f"ETF1 stake per point = £{etf1_stake}\n"
                 f"ETF2 stake per point = £{etf2_stake}\n\n"
                 f"With 25% margin:\n"
                 f"New ETF1 size = £{new_etf1_size}\n"
                 f"New ETF2 size = £{new_etf2_size}"
        )
    except ValueError:
        result_label.config(text="Please enter valid numeric values.")

# Set up main window
root = tk.Tk()
root.title("Spread Bet Pairs Trade Calculator")
root.geometry("500x500")

# Set dark theme with bright blue text
root.configure(bg='#1e1e1e')
style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", foreground="#00bfff", background="#1e1e1e")
style.configure("TButton", foreground="#00bfff", background="#3e3e3e")
style.configure("TEntry", foreground="#00bfff", background="#1e1e1e", fieldbackground="#3e3e3e")

# Input labels and entries
etf1_label = ttk.Label(root, text="ETF1 Price per Share:")
etf1_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
etf1_entry = ttk.Entry(root)
etf1_entry.grid(row=0, column=1, padx=10, pady=5)

etf2_label = ttk.Label(root, text="ETF2 Price per Share:")
etf2_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
etf2_entry = ttk.Entry(root)
etf2_entry.grid(row=1, column=1, padx=10, pady=5)

min_stake_label = ttk.Label(root, text="Minimum Stake for ETF2 (£):")
min_stake_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
min_stake_entry = ttk.Entry(root)
min_stake_entry.insert(0, "1")  # Default value of 1
min_stake_entry.grid(row=2, column=1, padx=10, pady=5)

account_balance_label = ttk.Label(root, text="Account Balance (£):")
account_balance_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
account_balance_entry = ttk.Entry(root)
account_balance_entry.grid(row=3, column=1, padx=10, pady=5)

etf1_margin_label = ttk.Label(root, text="ETF1 Margin Requirement (£):")
etf1_margin_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
etf1_margin_entry = ttk.Entry(root)
etf1_margin_entry.grid(row=4, column=1, padx=10, pady=5)

etf2_margin_label = ttk.Label(root, text="ETF2 Margin Requirement (£):")
etf2_margin_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
etf2_margin_entry = ttk.Entry(root)
etf2_margin_entry.grid(row=5, column=1, padx=10, pady=5)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_stake)
calculate_button.grid(row=6, column=0, columnspan=2, pady=20)

# Result display
result_label = ttk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=7, column=0, columnspan=2)

# Center the window
root.eval('tk::PlaceWindow . center')

# Run the application
root.mainloop()
