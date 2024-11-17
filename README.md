

# Diagonal Spread Calculator

A simple **Python GUI application** built with Tkinter to calculate the **Maximum Risk** and **Maximum Profit** for diagonal call spreads in spread betting or options trading. This tool allows users to input key trade details, such as strike prices and premiums, and instantly see the results.

---

## Features

- **Input Fields**:
  - Long Call Strike Price
  - Short Call Strike Price
  - Premium Paid for the Long Call
  - Premium Received from the Short Call
- **Calculations**:
  - **Maximum Risk**: The maximum amount you can lose in the trade.
  - **Maximum Profit**: The potential profit if the underlying reaches the short call strike at expiration.
- **User-Friendly GUI**:
  - Intuitive layout.
  - Dark theme for a modern, visually appealing interface.
  - Error handling for invalid inputs.

---

## How to Use

1. Clone or download this repository to your local machine.
2. Install Python (if not already installed).
3. Run the script:
   ```bash
   python diagonal_spread_calculator.py
   ```
4. Enter the following values in the provided fields:
   - **Long Call Strike**: Strike price of the long call option.
   - **Short Call Strike**: Strike price of the short call option.
   - **Premium Paid**: The cost of the long call (in £).
   - **Premium Received**: The premium received from selling the short call (in £).
5. Click the **Calculate** button.
6. The **Maximum Risk** and **Maximum Profit** will be displayed below the button.

---

## Example

Here’s an example calculation:

- **Long Call Strike**: 5475  
- **Short Call Strike**: 6100  
- **Premium Paid**: £555.84  
- **Premium Received**: £23.8  

The results:
- **Maximum Risk**: £532.04  
- **Maximum Profit**: £92.96  

---

## Installation

1. Ensure Python 3.x is installed on your machine.
2. Install Tkinter (it comes pre-installed with most Python distributions).
3. Clone the repository:
   ```bash
   git clone https://github.com/your-username/diagonal-spread-calculator.git
   ```
4. Navigate to the project folder:
   ```bash
   cd diagonal-spread-calculator
   ```
5. Run the script:
   ```bash
   python diagonal_spread_calculator.py
   ```

---

## Code Explanation

The core logic is implemented in Python using the Tkinter library. Here’s an overview of how the calculations are made:

- **Maximum Risk**:
  \[
  \text{Maximum Risk} = \text{Premium Paid} - \text{Premium Received}
  \]
- **Maximum Profit**:
  \[
  \text{Maximum Profit} = (\text{Short Call Strike} - \text{Long Call Strike}) - \text{Maximum Risk}
  \]

These values are dynamically calculated based on the inputs provided.

---

## Screenshots

### Input Fields and Results
![Screenshot](diagonal_spread_calculator_screenshot.png)

---

## Future Enhancements

- Add support for other option strategies.
- Include a real-time price feed integration.
- Save calculation history for further analysis.

---

## Contributions

Contributions, bug reports, and feature requests are welcome! Please feel free to submit an issue or a pull request.

---

## Contact

For questions or feedback, reach out to **[Your Name]** at [your-email@example.com].

---

Let me know if you need adjustments or additional sections!
