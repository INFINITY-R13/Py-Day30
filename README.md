# Py-Day30

# MyPass Password Manager

MyPass is a simple, local password manager application built with Python and Tkinter. It allows you to generate strong, unique passwords, save them for different websites, and easily retrieve them when needed. All data is stored locally in a `data.json` file.

## ✨ Features

  * **Generate Strong Passwords**: Creates secure passwords with a random combination of letters, numbers, and symbols.
  * **Copy to Clipboard**: Automatically copies newly generated or retrieved passwords to the clipboard for convenience.
  * **Save Credentials**: Stores website names, email/usernames, and passwords securely in a local JSON file.
  * **Search Functionality**: Quickly find saved login credentials for any website.
  * **Intuitive GUI**: A clean and simple graphical user interface built with Python's native Tkinter library.
  * **Overwrite Protection**: Asks for user confirmation before overwriting an existing entry for a website.

-----

## 🛠️ How It Works

The application is built around three core functions:

1.  **Password Generation**: When you click the "Generate Password" button, the `generate_password()` function creates a strong password using a mix of 8-10 letters, 2-4 symbols, and 2-4 numbers. The result is shuffled, inserted into the password field, and copied to your clipboard.

2.  **Saving Data**: The `save()` function takes the website, email, and password from the input fields. It reads the existing `data.json` file (or creates it if it doesn't exist), updates it with the new entry, and saves it back to the file. If an entry for the website already exists, it prompts for confirmation before overwriting.

3.  **Finding Passwords**: The `find_password()` function searches the `data.json` file for the website you've entered. If a match is found, it displays the corresponding email and password in a popup and copies the password to your clipboard.

-----

## 🚀 Getting Started

Follow these instructions to get the project running on your local machine.

### Prerequisites

You need to have Python 3 installed. Additionally, the project requires the `pyperclip` library.

  * **Python 3**: [Download Python](https://www.python.org/downloads/)
  * **pyperclip**: A cross-platform Python module for copy and paste clipboard functions.

### Installation & Execution

1.  **Clone or download the repository** to your local machine. Ensure all files (`main.py`, `logo.png`, and `data.json`) are in the same directory.

2.  **Install the required library** using pip:

    ```sh
    pip install pyperclip
    ```

3.  **Run the application** from your terminal:

    ```sh
    python main.py
    ```

The password manager window should now appear on your screen.

-----

## 📂 Files in the Project

  * `main.py`: The main Python script that contains all the application logic, function definitions, and the Tkinter GUI setup.
  * `logo.png`: The logo image displayed at the top of the application window.
  * `data.json`: The JSON file where all your saved website credentials are stored. It is created automatically on the first save if it doesn't exist.
