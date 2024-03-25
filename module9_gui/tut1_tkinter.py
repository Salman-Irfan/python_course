import tkinter as tk
from tkinter import ttk


def submit_data():
    name_value = name_var.get()
    email_value = email_var.get()
    age_value = age_var.get()
    print("Name:", name_value)
    print("Email:", email_value)
    print("Age:", age_value)

    # Update labels to display the form data
    name_display_label.config(text=f"Name: {name_value}")
    email_display_label.config(text=f"Email: {email_value}")
    age_display_label.config(text=f"Age: {age_value}")


win = tk.Tk()

# UI development
win.title("Python GUI with Tkinter")

# Create variables to store user input
name_var = tk.StringVar()
email_var = tk.StringVar()
age_var = tk.IntVar()

# Create labels for form input
name_label = ttk.Label(win, text="Enter your name: ")
name_label.grid(row=0, column=0, sticky=tk.W)

email_label = ttk.Label(win, text="Enter your email: ")
email_label.grid(row=1, column=0, sticky=tk.W)

age_label = ttk.Label(win, text="Enter your age: ")
age_label.grid(row=2, column=0, sticky=tk.W)

# Create entry boxes and link them to variables
name_entry = ttk.Entry(win, textvariable=name_var)
name_entry.grid(row=0, column=1)

email_entry = ttk.Entry(win, textvariable=email_var)
email_entry.grid(row=1, column=1)

age_entry = ttk.Entry(win, textvariable=age_var)
age_entry.grid(row=2, column=1)

# Create a submit button
submit_btn = ttk.Button(win, text="Submit", command=submit_data)
submit_btn.grid(row=3, column=0, columnspan=2)

# Create labels to display form data
name_display_label = ttk.Label(win, text="")
name_display_label.grid(row=4, column=0, columnspan=2)

email_display_label = ttk.Label(win, text="")
email_display_label.grid(row=5, column=0, columnspan=2)

age_display_label = ttk.Label(win, text="")
age_display_label.grid(row=6, column=0, columnspan=2)

# Main loop
win.mainloop()
