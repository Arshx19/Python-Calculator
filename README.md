# Basic Calculator

A simple, interactive console-based calculator application written in Python. This project is designed for beginners learning the core concepts of Python programming.

## Project Description

This project is a text-based calculator that runs in the command line interface. It allows users to perform basic arithmetic operations (addition, subtraction, multiplication, and division) repeatedly. The code is written in a beginner-friendly manner, emphasizing readability, basic control flow (loops and conditionals), and simple error handling.

## Features

- **Menu-Driven Interface:** Clear and easy-to-use menu for choosing mathematical operations.
- **Basic Arithmetic Operations:** Supports Addition, Subtraction, Multiplication, and Division.
- **Decimal Number Support:** Utilizes `float` to handle both whole numbers and decimal calculations.
- **Error Handling:**
  - Prevents division by zero with custom error messages.
  - Validates user input to prevent program crashes when non-numeric values are entered.
  - Warns the user of invalid menu choices.
- **Continuous Mode:** Allows the user to execute multiple calculations consecutively until they choose to exit.

## Technologies Used

- **Python 3.x** (Only built-in standard libraries)

## How to Run the Project

1. Make sure you have Python installed on your computer. You can check this by running the following command in your terminal or command prompt:
   ```bash
   python --version
   ```

2. Download or clone this repository to your local machine.

3. Navigate to the project directory:
   ```bash
   cd Basic-Calculator
   ```

4. Run the calculator script:
   ```bash
   python calculator.py
   ```

## Example Output

Here is a preview of how the calculator works in the terminal:

```
Welcome to the Basic Calculator!

===== BASIC CALCULATOR =====
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
----------------------------
Choose an option (1-5): 1
Enter the first number: 12.5
Enter the second number: 8
----------------------------
12.5 + 8.0 = 20.5
----------------------------
Do you want to perform another calculation? (yes/no): y

===== BASIC CALCULATOR =====
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
----------------------------
Choose an option (1-5): 4
Enter the first number: 10
Enter the second number: 0
----------------------------
Error: Division by zero is not allowed!
----------------------------
Do you want to perform another calculation? (yes/no): n

Thank you for using the calculator. Goodbye!
```

## Future Improvements

If you're looking to expand this project as you learn, here are some great next steps:
1. **More Math Operations:** Add support for exponentiation (power), square roots, and modulus (remainder).
2. **History Log:** Keep track of past calculations performed during the session.
3. **Graphical User Interface (GUI):** Build a visual desktop interface using Python's built-in `tkinter` library.
