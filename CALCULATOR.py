## Import the tkinter library for GUI creation
import tkinter as tk

# Define the Calculator class for creating the GUI-based calculator
class Calculator:
    def __init__(self, root):
        self.root = root
        self.entry_text = tk.StringVar()

        # Create the display entry box
        self.entry_box = tk.Entry(root, textvariable=self.entry_text, font=('Arial', 18), bd=10, insertwidth=4, width=14, borderwidth=4)
        self.entry_box.grid(row=0, column=0, columnspan=4)

        # Initialize the calculator buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '000', 'M', '+',
            '.' , 'C','M+','='
        ]

        row_val = 1
        col_val = 0

        # Create buttons and add them to the grid
        for button in buttons:
            if button == 'C':
                tk.Button(self.root, text=button, width=10, height=3, command=self.clear).grid(row=row_val, column=col_val)
            elif button == '=':
                tk.Button(self.root, text=button, width=10, height=3, command=self.calculate).grid(row=row_val, column=col_val)
            else:
                tk.Button(self.root, text=button, width=10, height=3, command=lambda x=button: self.click_button(x)).grid(row=row_val, column=col_val)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click_button(self, item):
        # Append the clicked button's label to the entry box
        current = self.entry_text.get()
        self.entry_text.set(current + str(item))

    def clear(self):
         # Clear the content of the entry box
        self.entry_text.set("")

    def calculate(self):
        # Evaluate the mathematical expression and display the result
        try:
            result = str(eval(self.entry_text.get()))
            self.entry_text.set(result)
        except Exception as e:
            self.entry_text.set("Error")

# Initialize the Tkinter root window and set up the calculator
root = tk.Tk()
root.title("Simple Calculator")
calc = Calculator(root)
root.mainloop()