import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create a SQLite database
conn = sqlite3.connect('python_glossary.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (name TEXT, username TEXT, email TEXT, password TEXT)''')
conn.commit()


# Function to handle successful login
def handle_successful_login():
    global logged_in
    logged_in = True


# Function to handle login button click
def login():
    email = email_entry.get()
    password = password_entry.get()

    # Check if user exists in the database
    c.execute('SELECT * FROM users WHERE email=? AND password=?', (email, password))
    user = c.fetchone()

    if user:
        handle_successful_login()
        loginRoot.destroy()
        import crud
    else:
        messagebox.showerror("Login Failed", "Invalid email or password")


# Function to open the registration window
def open_register_window():
    loginRoot.destroy()
    import register

    # Implement the registration form here


# Create main window
loginRoot = tk.Tk()
loginRoot.title("Login")
loginRoot.geometry("{0}x{1}+0+0".format(loginRoot.winfo_screenwidth(), loginRoot.winfo_screenheight()))
loginRoot['background'] = "#D2E1FE"
# Create and position the Python Glossary header
header = tk.Label(loginRoot, text="PYTHON GLOSSARY", font=("Arial", 24, "bold"), fg="#FFFFFF", bg="#D2E1FE")
header.pack(pady=(20, 10))

# Create a frame to hold the login form
login_frame = tk.Frame(loginRoot, bg="white", padx=20, pady=30, borderwidth=1, relief="flat",)
login_frame.pack(pady=(10, 0))

email_label = tk.Label(login_frame, text="Email", bg="white", fg="black")
email_label.grid(row=0, column=0, sticky="w")
email_entry = tk.Entry(login_frame, width=30, bg="grey", highlightbackground="lightgrey")
email_entry.grid(row=0, column=1, padx=(10, 0))

password_label = tk.Label(login_frame, text="Password", bg="white", fg="black")
password_label.grid(row=1, column=0, sticky="w", pady=(10, 0))
password_entry = tk.Entry(login_frame, show="*", width=30, bg="grey", highlightbackground="lightgrey")
password_entry.grid(row=1, column=1, padx=(10, 0), pady=(10, 0))

login_button = tk.Button(login_frame, text="Login", command=login, width=30, height=2, font=("Arial", 12, "bold"),
                         fg="green", bg="#FFFFFF", highlightbackground="#FFFFFF")
login_button.grid(row=2, columnspan=2, pady=(20, 0))

register_label = tk.Label(login_frame, text="Don't have an account yet?", bg="white", fg="black")
register_label.grid(row=3, columnspan=2, pady=(10, 0))
register_link = tk.Label(login_frame, text="Register", fg="blue", cursor="hand2", bg="white")
register_link.grid(row=4, columnspan=2)

# Bind the label to open the registration window
register_link.bind("<Button-1>", lambda e: open_register_window())

loginRoot.mainloop()
