# Import necessary modules from Tkinter for the GUI, random for password generation,
# pyperclip for clipboard operations, and json for data storage.
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generates a random, strong password and inserts it into the password entry field."""
    # Define the character sets for the password
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    # Create a list of random characters: 8-10 letters, 2-4 symbols, and 2-4 numbers
    password_list = (
            [choice(letters) for _ in range(randint(8, 10))] +
            [choice(symbols) for _ in range(randint(2, 4))] +
            [choice(numbers) for _ in range(randint(2, 4))]
    )

    # Shuffle the list to ensure the character types are mixed
    shuffle(password_list)

    # Join the characters in the list to form the final password string
    password = "".join(password_list)

    # Clear the password entry field before inserting the new password
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    
    # Automatically copy the generated password to the clipboard for convenience
    pyperclip.copy(password)
    messagebox.showinfo(title="Success", message="New password generated and copied to clipboard!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Saves the website, email, and password to the data.json file."""
    # Get and clean the input from the entry fields
    website = website_entry.get().strip().lower()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    
    # A dictionary to hold the new data entry
    new_data = {website: {"email": email, "password": password}}

    # Validate that the website and password fields are not empty
    if not website or not password:
        messagebox.showinfo(title="Oops", message="Please don't leave the Website or Password fields empty.")
        return

    try:
        # Try to open and read the existing data file
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is empty/corrupt, start with an empty dictionary
        data = {}
    
    # *** FIX IMPLEMENTED HERE ***
    # Check if an entry for the website already exists
    if website in data:
        # Ask the user for confirmation before overwriting existing data
        is_ok = messagebox.askokcancel(
            title=website, 
            message=f"An entry for {website} already exists.\nEmail: {data[website]['email']}\n"
                    f"Do you want to overwrite it?"
        )
        if not is_ok:
            return  # If user clicks "Cancel", do not save and exit the function

    # Update the dictionary with the new data (either adds a new entry or overwrites an existing one after confirmation)
    data.update(new_data)

    # Write the updated dictionary back to the JSON file
    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    # Clear the website and password fields after saving
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    messagebox.showinfo(title="Success", message="Your details have been saved successfully.")


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    """Searches for a website's credentials in the data.json file."""
    # Get and clean the website name from the entry field
    website = website_entry.get().strip().lower()

    # Ensure the website field is not empty
    if not website:
        messagebox.showinfo(title="Error", message="Please enter a website to search for.")
        return

    try:
        # Open and load the data from the JSON file
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Handle case where data file doesn't exist or is invalid
        messagebox.showinfo(title="Error", message="No Data File Found. Try saving an entry first.")
        return

    # Check if the website exists as a key in the loaded data
    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        # Display the found credentials in a message box
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        # Automatically copy the found password to the clipboard
        pyperclip.copy(password)
    else:
        # Inform the user if no entry was found for that website
        messagebox.showinfo(title="Error", message=f"No details for '{website}' exist.")


# ---------------------------- UI SETUP ------------------------------- #
# Initialize the main window
window = Tk()
window.title("MyPass Password Manager")
window.config(padx=50, pady=50)  # Add padding around the window content

# Create a Canvas widget to display the logo
canvas = Canvas(height=200, width=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)  # Place the canvas in the grid

# --- Labels ---
Label(text="Website:").grid(row=1, column=0)
Label(text="Email/Username:").grid(row=2, column=0)
Label(text="Password:").grid(row=3, column=0)

# --- Entry Fields ---
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky="ew") # Use sticky to make widget fill the column
website_entry.focus()  # Place the cursor in this field on startup

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(0, "example@gmail.com")  # Pre-fill with a default email

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")

# --- Buttons ---
Button(text="Search", command=find_password).grid(row=1, column=2, sticky="ew")
Button(text="Generate Password", command=generate_password).grid(row=3, column=2, sticky="ew")
Button(text="Add", width=36, command=save).grid(row=4, column=1, columnspan=2, sticky="ew")

# Start the Tkinter event loop
window.mainloop()