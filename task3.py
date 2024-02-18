import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(entry_length.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    messagebox.showinfo("Generated Password", f"Your password is: {password}")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create GUI elements
label_length = tk.Label(root, text="Password Length:")
label_length.pack()
entry_length = tk.Entry(root)
entry_length.pack()
button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack()

# Run the Tkinter event loop
root.mainloop()
