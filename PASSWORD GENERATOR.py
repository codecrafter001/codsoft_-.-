import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        # Get the password length from the user input
        length = int(entry_length.get())

        # Check if the length is less than 8 characters
        if length < 8:
            messagebox.showwarning("Invalid Length", "Password length should be at least 8 characters.")
            return

        # Initialize an empty string for characters
        characters = ''

        # Add uppercase letters if selected
        if var_uppercase.get() == "Yes":
            characters += string.ascii_uppercase

        # Add lowercase letters if selected
        if var_lowercase.get() == "Yes":
            characters += string.ascii_lowercase

        # Add digits if selected
        if var_numbers.get() == "Yes":
            characters += string.digits

        # Add special characters if selected
        if var_special.get() == "Yes":
            characters += string.punctuation

        # If no character types are selected, show a warning
        if not characters:
            messagebox.showwarning("No Character Type Selected", "Please select at least one character type.")
            return

        # Generate the password using the selected characters
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display the generated password in the entry field
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)

    except ValueError:
        # Handle case where the input is not a valid number
        messagebox.showerror("Invalid Input", "Please enter a valid number for the length.")

# Set up the main application window
root = tk.Tk()
root.title("Password Generator")

# Create and place the length label and entry
label_length = tk.Label(root, text="Password Length:")
label_length.grid(row=0, column=0, padx=10, pady=10)

entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

# Create and place the options for character types
label_uppercase = tk.Label(root, text="Include Uppercase Letters:")
label_uppercase.grid(row=1, column=0, padx=10, pady=10)

var_uppercase = tk.StringVar(value="Yes")
option_uppercase = tk.OptionMenu(root, var_uppercase, "Yes", "No")
option_uppercase.grid(row=1, column=1, padx=10, pady=10)

label_lowercase = tk.Label(root, text="Include Lowercase Letters:")
label_lowercase.grid(row=2, column=0, padx=10, pady=10)

var_lowercase = tk.StringVar(value="Yes")
option_lowercase = tk.OptionMenu(root, var_lowercase, "Yes", "No")
option_lowercase.grid(row=2, column=1, padx=10, pady=10)

label_numbers = tk.Label(root, text="Include Numbers:")
label_numbers.grid(row=3, column=0, padx=10, pady=10)

var_numbers = tk.StringVar(value="Yes")
option_numbers = tk.OptionMenu(root, var_numbers, "Yes", "No")
option_numbers.grid(row=3, column=1, padx=10, pady=10)

label_special = tk.Label(root, text="Include Special Characters:")
label_special.grid(row=4, column=0, padx=10, pady=10)

var_special = tk.StringVar(value="Yes")
option_special = tk.OptionMenu(root, var_special, "Yes", "No")
option_special.grid(row=4, column=1, padx=10, pady=10)

# Create and place the generate button
button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.grid(row=5, column=0, columnspan=2, pady=10)

# Create and place the password entry
label_password = tk.Label(root, text="Generated Password:")
label_password.grid(row=6, column=0, padx=10, pady=10)

entry_password = tk.Entry(root, width=30)
entry_password.grid(row=6, column=1, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
