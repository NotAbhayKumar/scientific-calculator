# Scientific Calculator

This is a simple scientific calculator built using Python's Tkinter library. It supports basic arithmetic operations as well as some advanced mathematical functions like trigonometric calculations, logarithms, and more.

## Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division.
- **Advanced Mathematical Functions**: 
  - Sine, cosine, tangent
  - Square root
  - Natural logarithm
  - Logarithm base 10
  - Pi (π)
  - Euler's number (e)
- **Clear Button**: Resets the calculation.
- **Backspace Button**: Deletes the last character.
- **Decimal Point Support**: Allows for decimal calculations.

## Installation

To get started with the scientific calculator, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/NotAbhayKumar/scientific-calculator.git

2. **Navigate to the Project Directory**:
   ```bash
   cd scientific-calculator

4. **Ensure You Have Python Installed**:
   This project requires Python 3.6 or later.

## Usage

To run the calculator, execute the following command in your terminal:

```python calculator.py```

The calculator window will appear, and you can start performing calculations.

## Code Overview

The main logic of the calculator is contained within the ScientificCalculator class in the `calculator.py` file. Below is a brief overview of the code structure:

## ScientificCalculator Class

**Initialization (__init__)**:

1. Sets up the main window, entry widget, and buttons.
2. Configures the grid layout for the buttons.
   
**Button Creation**:
1. Buttons are created dynamically from a list of tuples, where each tuple contains the button text and its color.
   
**Button Click Handling (on_button_click)**:

1. Evaluates expressions.
2. Handles special buttons like clear, backspace, pi, and Euler's number.
3. Appends text to the equation displayed in the entry widget.
## Main Function
Initializes the Tkinter root and creates an instance of the ScientificCalculator class.
Starts the Tkinter event loop to display the calculator window.

**Example**

Here is a snippet of how to import the necessary libraries:

```python
import tkinter as tk
import math

# Rest of the code... 
```
For a complete implementation, see the calculator.py file.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

If you have any questions or feedback, feel free to reach out:
Email: mr.abhaykumar@outlook.com
GitHub: NotAbhayKumar
