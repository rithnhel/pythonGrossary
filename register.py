import tkinter as tk
from tkinter import messagebox
import sqlite3


def register_user():
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Validate password and confirm password
    if password != confirm_password:
        messagebox.showerror("Registration Failed", "Passwords do not match")
        return

    # Check if user already exists
    c.execute('SELECT * FROM users WHERE email=?', (email,))
    user = c.fetchone()

    if user:
        messagebox.showerror("Registration Failed", "User already exists")
    else:
        c.execute('INSERT INTO users VALUES (?, ?)', (email, password))
        conn.commit()
        messagebox.showinfo("Registration Successful", "User registered successfully")
        open_login_window()


def open_login_window():
    register.destroy()
    import login


register = tk.Tk()
register['background'] = "#D2E1FE"
register.title("Register")
register.geometry("{0}x{1}+0+0".format(register.winfo_screenwidth(), register.winfo_screenheight()))

conn = sqlite3.connect('python_glossary.db')
c = conn.cursor()

# Create and position the Python Glossary header
header = tk.Label(register, text="PYTHON GLOSSARY", font=("Arial", 24, "bold"), fg="#FFFFFF", bg="#D2E1FE")
header.pack(pady=(20, 10))

register_frame = tk.Frame(register, bg="white", padx=20, pady=30, borderwidth=1, relief="flat", bd=10, width=300)
register_frame.pack(pady=(10, 0))

email_label = tk.Label(register_frame, text="Email:", bg="white", fg="black", font=("Arial", 12))
email_label.grid(row=0, column=0, sticky="w")
email_entry = tk.Entry(register_frame, width=30, bg="grey", highlightbackground="lightgrey")
email_entry.grid(row=0, column=1, columnspan=2, pady=(0, 10))

password_label = tk.Label(register_frame, text="Password:", bg="white", fg="black", font=("Arial", 12))
password_label.grid(row=1, column=0, sticky="w")
password_entry = tk.Entry(register_frame, show="*", width=30, bg="grey", highlightbackground="lightgrey")
password_entry.grid(row=1, column=1, columnspan=2, pady=(0, 10))

confirm_password_label = tk.Label(register_frame, text="Confirm Password:", bg="white", fg="black", font=("Arial", 12))
confirm_password_label.grid(row=2, column=0, sticky="w")
confirm_password_entry = tk.Entry(register_frame, show="*", width=30, bg="grey", highlightbackground="lightgrey")
confirm_password_entry.grid(row=2, column=1, columnspan=2, pady=(0, 10))

register_button = tk.Button(register_frame, text="Register", command=register_user, width=30, height=2, font=("Arial", 12, "bold"),
                            fg="green", bg="#FFFFFF", highlightbackground="#FFFFFF")
register_button.grid(row=3, columnspan=3, pady=(10, 0))

login_label = tk.Label(register_frame, text="Already have an account? ", bg="white", fg="black")
login_label.grid(row=4, columnspan=3, pady=(10, 0))

login_link = tk.Label(register_frame, text="Login", fg="blue", cursor="hand2", bg="white")
login_link.grid(row=5, columnspan=3)

login_link.bind("<Button-1>", lambda e: open_login_window())

register.mainloop()
