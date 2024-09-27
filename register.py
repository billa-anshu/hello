from tkinter import *

# Function to print user details
def submit():
    print(f"Name: {name_var.get()}")
    print(f"Email: {email_var.get()}")
    print(f"Phone: {phone_var.get()}")
    print(f"Address: {address_var.get()}")

# Create the main window
root = Tk()
root.title("Simple Registration Form")
root.geometry("300x200")

# Variables to store user input
name_var = StringVar()
email_var = StringVar()
phone_var = StringVar()
address_var = StringVar()

# Create and place labels and entry fields
Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
Entry(root, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Email").grid(row=1, column=0, padx=10, pady=5)
Entry(root, textvariable=email_var).grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Phone").grid(row=2, column=0, padx=10, pady=5)
Entry(root, textvariable=phone_var).grid(row=2, column=1, padx=10, pady=5)

Label(root, text="Address").grid(row=3, column=0, padx=10, pady=5)
Entry(root, textvariable=address_var).grid(row=3, column=1, padx=10, pady=5)

# Create and place the submit button
Button(root, text="Submit", command=submit).grid(row=4, column=1, pady=10)

# Run the main loop
root.mainloop()
