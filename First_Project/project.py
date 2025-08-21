import tkinter as tk

# Function to handle form submission
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    print(f"Name: {name}, Email: {email}")

# Create main window
root = tk.Tk()
root.title("Simple Form")

# Labels and text fields
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1)

# Submit button
tk.Button(root, text="Submit", command=submit_form).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
