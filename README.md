Diagonal Spread Calculator
A simple Python GUI application built with Tkinter to calculate the Maximum Risk and Maximum Profit for diagonal call spreads in spread betting or options trading. This tool allows users to input key trade details, such as strike prices and premiums, and instantly see the results.

Features
Input Fields:
Long Call Strike Price
Short Call Strike Price
Premium Paid for the Long Call
Premium Received from the Short Call
Calculations:
Maximum Risk: The maximum amount you can lose in the trade.
Maximum Profit: The potential profit if the underlying reaches the short call strike at expiration.
User-Friendly GUI:
Intuitive layout.
Dark theme for a modern, visually appealing interface.
Error handling for invalid inputs.
How to Use
Clone or download this repository to your local machine.
Install Python (if not already installed).
Run the script:
bash
Copy code
python diagonal_spread_calculator.py
Enter the following values in the provided fields:
Long Call Strike: Strike price of the long call option.
Short Call Strike: Strike price of the short call option.
Premium Paid: The cost of the long call (in £).
Premium Received: The premium received from selling the short call (in £).
Click the Calculate button.
The Maximum Risk and Maximum Profit will be displayed below the button.
Example
Here’s an example calculation:

Long Call Strike: 5475
Short Call Strike: 6100
Premium Paid: £555.84
Premium Received: £23.8
The results:

Maximum Risk: £532.04
Maximum Profit: £92.96
Installation
Ensure Python 3.x is installed on your machine.
Install Tkinter (it comes pre-installed with most Python distributions).
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/diagonal-spread-calculator.git
Navigate to the project folder:
bash
Copy code
cd diagonal-spread-calculator
Run the script:
bash
Copy code
python diagonal_spread_calculator.py
Code Explanation
The core logic is implemented in Python using the Tkinter library. Here’s an overview of how the calculations are made:

Maximum Risk:
Maximum Risk
=
Premium Paid
−
Premium Received
Maximum Risk=Premium Paid−Premium Received
Maximum Profit:
Maximum Profit
=
(
Short Call Strike
−
Long Call Strike
)
−
Maximum Risk
Maximum Profit=(Short Call Strike−Long Call Strike)−Maximum Risk
These values are dynamically calculated based on the inputs provided.

Screenshots
Input Fields and Results

Future Enhancements
Add support for other option strategies.
Include a real-time price feed integration.
Save calculation history for further analysis.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributions
Contributions, bug reports, and feature requests are welcome! Please feel free to submit an issue or a pull request.

