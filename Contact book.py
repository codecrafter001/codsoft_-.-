import tkinter as tk
from tkinter import messagebox, simpledialog

# Initialize the contact list
contacts = {}

# Function to add a new contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name and phone:
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Success", f"Added contact: {name}")
        clear_entries()
        show_contacts()
    else:
        messagebox.showwarning("Error", "Name and phone number are required!")

# Function to clear the input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to display contacts in the listbox
def show_contacts():
    contact_listbox.delete(0, tk.END)
    for name, info in contacts.items():
        contact_listbox.insert(tk.END, f"{name}: {info['phone']}")

# Function to search for a contact by name or phone number
def search_contact():
    search_term = simpledialog.askstring("Search", "Enter name or phone number:")
    if search_term:
        found = False
        for name, info in contacts.items():
            if search_term.lower() in name.lower() or search_term in info['phone']:
                messagebox.showinfo("Found", f"{name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}")
                found = True
                break
        if not found:
            messagebox.showinfo("Not Found", "Contact not found.")

# Function to update a contact
def update_contact():
    name = simpledialog.askstring("Update", "Enter the name of the contact to update:")
    if name in contacts:
        phone = simpledialog.askstring("Update", f"New phone number for {name}:", initialvalue=contacts[name]['phone'])
        email = simpledialog.askstring("Update", f"New email for {name}:", initialvalue=contacts[name]['email'])
        address = simpledialog.askstring("Update", f"New address for {name}:", initialvalue=contacts[name]['address'])
        
        if phone:
            contacts[name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Updated", f"Contact {name} updated!")
            show_contacts()
        else:
            messagebox.showwarning("Error", "Phone number can't be empty!")
    else:
        messagebox.showwarning("Error", f"Contact {name} not found.")

# Function to delete a contact
def delete_contact():
    name = simpledialog.askstring("Delete", "Enter the name of the contact to delete:")
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Deleted", f"Contact {name} deleted!")
        show_contacts()
    else:
        messagebox.showwarning("Error", f"Contact {name} not found.")

# Main window setup
root = tk.Tk()
root.title("Contact Manager")
root.configure(bg='#333333')  # Dark gray background

# Entry fields for contact details
tk.Label(root, text="Name:", bg='#333333', fg='white').grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:", bg='#333333', fg='white').grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:", bg='#333333', fg='white').grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address:", bg='#333333', fg='white').grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
address_entry = tk.Entry(root, width=30)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons for various actions
tk.Button(root, text="Add Contact", width=20, bg='#ff9966', fg='white', command=add_contact).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Search Contact", width=20, bg='#ff9966', fg='white', command=search_contact).grid(row=4, column=1, padx=10, pady=10)
tk.Button(root, text="Update Contact", width=20, bg='#ffcc99', fg='black', command=update_contact).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="Delete Contact", width=20, bg='#ff6666', fg='white', command=delete_contact).grid(row=5, column=1, padx=10, pady=10)

# Listbox to display contacts
contact_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12))
contact_listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
