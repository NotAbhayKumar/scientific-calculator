import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x480")
        self.root.configure(bg="#333333")

        self.equation = tk.StringVar()
        self.equation.set("")

        # Entry widget for displaying the equation
        self.entry = tk.Entry(root, textvariable=self.equation, font=('Arial', 18), bd=5, insertwidth=4, width=20, justify='right')
        self.entry.grid(row=0, column=0, columnspan=5, pady=10, padx=10, sticky="nsew")

        # Create buttons with colors and functionalities
        buttons = [
            ('C', '#FF4C4C'), ('(', '#666666'), (')', '#666666'), ('/', '#FF9500'),
            ('7', '#666666'), ('8', '#666666'), ('9', '#666666'), ('*', '#FF9500'),
            ('4', '#666666'), ('5', '#666666'), ('6', '#666666'), ('-', '#FF9500'),
            ('1', '#666666'), ('2', '#666666'), ('3', '#666666'), ('+', '#FF9500'),
            ('0', '#666666'), ('.', '#666666'), ('=', '#FF4C4C'), ('⌫', '#FF4C4C'), 
            ('pi', '#333333'), ('sin', '#333333'), ('cos', '#333333'), ('tan', '#333333'),
            ('sqrt', '#333333'), ('log', '#333333'), ('log10', '#333333'), ('e', '#333333')
        ]

        row = 1
        column = 0
        for (text, color) in buttons:
            tk.Button(root, text=text, command=lambda t=text: self.on_button_click(t), width=5, height=2, bg=color, fg='white', font=('Arial', 12, 'bold')).grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
            column += 1
            if column > 3:
                column = 0
                row += 1

        # Configure grid resizing
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(7):
            root.grid_rowconfigure(i, weight=1)

    def on_button_click(self, text):
        if text == '=':
            try:
                result = str(eval(self.equation.get().replace('sqrt', 'math.sqrt').replace('log10', 'math.log10').replace('log', 'math.log').replace('sin', 'math.sin').replace('cos', 'math.cos').replace('tan', 'math.tan')))
                self.equation.set(result)
            except:
                self.equation.set("Error")
        elif text == 'C':
            self.equation.set("")
        elif text == '⌫':
            self.equation.set(self.equation.get()[:-1])
        elif text == 'pi':
            self.equation.set(self.equation.get() + str(math.pi))
        elif text == 'e':
            self.equation.set(self.equation.get() + str(math.e))
        elif text == 'sqrt':
            self.equation.set(self.equation.get() + "sqrt(")
        elif text in ['sin', 'cos', 'tan', 'log', 'log10']:
            self.equation.set(self.equation.get() + text + "(")
        else:
            self.equation.set(self.equation.get() + text)

def main():
    root = tk.Tk()
    root.resizable(False, False)
    app = ScientificCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
