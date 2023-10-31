import os
import shutil #Copy file From > To folder
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING
from db import Database

db = Database("python_glossary.db")
global logged_in


# Function to check if user is logged in
def is_logged_in():
    global logged_in
    return logged_in


# Function to open login window
def open_login_window():
    root.destroy()
    import login


def show_error():
    messagebox.showerror("Error", "User not logged in. Please login.")


root = Tk()
root['background'] = "#D2E1FE"
root.title("Keyword Management System")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.config(bg="Whitesmoke")
root.state("zoomed")
logged_in = False
titleName = StringVar()
description = StringVar()
example = StringVar()

entries_frame = Frame(root, bg="#D2E1FE", padx=30, pady=20) # Entries Frame
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="KEYWORD MANAGEMENT SYSTEM", font=( "Arial", 24, "bold"), bg="#D2E1FE", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

lblTitleName = Label(entries_frame, text="Keyword Name", font=("Arial", 16), bg="#D2E1FE", fg="black")
lblTitleName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtTitleName = Entry(entries_frame, textvariable=titleName, bg="grey", font=("Arial", 16), width=30)
txtTitleName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblDescription = Label( entries_frame, text="Description", font=("Arial", 16), bg="#D2E1FE", fg="black")
lblDescription.grid (row=2, column=0, padx=10, pady=10, sticky="w")
txtDescription = Entry(entries_frame, textvariable=description, bg="grey", font=("Arial", 16), width=30 )
txtDescription.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblExample = Label(entries_frame, text="Example", font=( "Arial", 16), bg="#D2E1FE", fg="black")
lblExample.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtExample = Entry(entries_frame, textvariable=example, bg="grey", font=("Arial", 16), width=30)
txtExample.grid(row=2, column=3, padx=10, pady= 10, sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row, img
    row = data["values"]
    titleName.set(row[1])
    description.set(row[2])
    example.set(row[3])


def dispalyAll():
    tv.delete(*tv.get_children())
    for i, row in enumerate(db.fetch()):
        if i % 2 == 0:
            tv.insert("", END, values=row, tags=("EvenRow",))
        else:
            tv.insert("", END, values=row, tags=("OddRow",))


def add_Keyword():
    if txtTitleName.get() == "" or txtDescription.get() == "" or txtExample.get() == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return

    db.insert(txtTitleName.get(), txtDescription.get(), txtExample.get())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()


def update_Keyword():
    if txtTitleName.get() == "" or txtDescription.get() == "" or txtExample.get() == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0], txtTitleName.get(), txtDescription.get(), txtExample.get())
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


def confirmDelete():
    answer = askokcancel(
        title='Confirmation',
        message='Do you want to delete this record?',
        icon=WARNING)

    if answer:
        delete_Keyword()
        showinfo(
            title='Deletion Record',
            message='The record is deleted successfully.')


def delete_Keyword():
    db.remove(row[0])
    clearAll()
    dispalyAll()


def clearAll():
    titleName.set("")
    description.set("")
    example.set("")


btn_frame = Frame(entries_frame, bg="#D2E1FE")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
Button(btn_frame, command=add_Keyword, text=" Add New ",
       width=15, height=2, font=("Arial", 16, "bold"), fg="Green",
       bg="White", bd=0, highlightbackground="#FFFFFF").grid(row=0, column=0)
Button(btn_frame, command=update_Keyword, text=" Update ",
       width=15, height=2, font=("Arial", 16, "bold"),
       fg="orange", bg="White",
       bd=0, highlightbackground="#FFFFFF").grid(row=0, column=1, padx=10)
Button(btn_frame, command=confirmDelete, text=" Delete ",
       width=15, height=2, font=("Arial", 16, "bold"),
       fg="Red", bg="White",
       bd=0, highlightbackground="#FFFFFF").grid(row=0, column=2, padx=10)
Button(btn_frame, command=clearAll, text=" Clear ",
       width=15, height=2, font=("Arial", 16, "bold"),
       fg="Black", bg="White",
       bd=0, highlightbackground="#FFFFFF").grid(row=0, column=3, padx=10)

style = ttk.Style()
# Modify the font of the body
style.configure("mystyle.Treeview", font= ('Arial', 12), rowheight=30)
style.configure("EvenRow.Treeview", background="lightblue")

# Add a style for odd rows
style.configure("OddRow.Treeview", background="lightgrey")
# Modify the font of the headings
style.configure("mystyle.Treeview.Heading", font= ( 'Arial', 12) )
tv = ttk.Treeview (root, columns=(1, 2, 3, 4), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=50)
tv.heading("2", text="Keyword Name" )
tv.column("2", width=150)
tv.heading("3", text="Description")
tv.column ("3", width=400)
tv.heading ("4", text="Example" )
tv.column("4", width=400)
tv['show'] = 'headings'
tv.bind("<Double-Button>", getData)
tv.pack(fill=X, padx=35)

# Configuring treeview (tv)
#tv.configure(xscrollcommand = v_scrlbar.set)

v_scrlbar = ttk.Scrollbar(root, orient = "vertical", command=tv.yview)

# Calling pack method to vertical scrollbar
#_scribar.pack( side ='right', fill ='x')
dispalyAll()
#root.bind("<Configure>", resize_image)

root.mainloop()
