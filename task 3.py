import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength():
    password = entry.get()
    score = 0
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        messagebox.showinfo("Password Strength", "Weak password: Password should be at least 8 characters long.")
        return
    
    # Check uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    
    # Check lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    
    # Check numbers
    if re.search(r'[0-9]', password):
        score += 1
    
    # Check special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    
    # Assess strength
    if score == 5:
        messagebox.showinfo("Password Strength", "Strong password: Your password meets all criteria.")
    elif score >= 3:
        messagebox.showinfo("Password Strength", "Medium password: Your password could be stronger.")
    else:
        messagebox.showinfo("Password Strength", "Weak password: Your password needs improvement.")

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create password entry field
entry_label = tk.Label(root, text="Enter your password:")
entry_label.pack()
entry = tk.Entry(root, show="*")
entry.pack()

# Create button to check password strength
check_button = tk.Button(root, text="Check Password Strength", command=check_password_strength)
check_button.pack()

# Run the main event loop
root.mainloop()