from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_list = (
            [choice(letters) for _ in range(randint(8, 10))] +
            [choice(symbols) for _ in range(randint(2, 4))] +
            [choice(numbers) for _ in range(randint(2, 4))]
    )

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)  # Clear field before inserting
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().strip().lower()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not website or not password:
        messagebox.showinfo(title="Oops", message="Please don't leave fields empty.")
        return

    new_data = {website: {"email": email, "password": password}}

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):  # Handle file not found or corrupt JSON
        data = {}

    data.update(new_data)

    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().strip().lower()

    if not website:
        messagebox.showinfo(title="Error", message="Please enter a website.")
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showinfo(title="Error", message="No Data File Found.")
        return

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        pyperclip.copy(password)  # Automatically copy found password
    else:
        messagebox.showinfo(title="Error", message=f"No details for {website} exist.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
Label(text="Website:").grid(row=1, column=0)
Label(text="Email/Username:").grid(row=2, column=0)
Label(text="Password:").grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
Button(text="Search", width=13, command=find_password).grid(row=1, column=2)
Button(text="Generate Password", command=generate_password).grid(row=3, column=2)
Button(text="Add", width=36, command=save).grid(row=4, column=1, columnspan=2)

window.mainloop()
