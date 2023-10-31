import json
from tkinter import *
from db import Database

db = Database("python_glossary.db")
root = Tk()
root.title("Python Glossary")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.config(bg="Whitesmoke")
root.minsize(width=600, height=400)
lighColor = "#D2E1FE"


wordList=[]
filteredList = []
data = db.fetch()

# Convert the data into a list of dictionaries
wordList = [{'title': row[1], 'description': row[2], 'example': row[3]} for row in data]

# You can also filter the data if needed
filteredList = wordList

# Convert to JSON
json_data = json.dumps(wordList)



mainFrame = Frame(root, bg=lighColor, padx=10, pady=10)
mainFrame.pack(side=TOP, fill=BOTH, expand=1)
mainFrame.grid_columnconfigure(1, weight=1)
mainFrame.grid_rowconfigure(1, weight=1)

title = Label(mainFrame, text="Python Glossary", font=("Arial", 18), fg="black", background=lighColor, anchor='w')
title.grid(row=0, columnspan=2, sticky="nsew", )
# login_link = Label(mainFrame, text="Login", fg="blue", cursor="hand2", bg="#D2E1FE")
# login_link.grid(row=0, columnspan=2)
#
# login_link.bind("<Button-1>", lambda e: open_login_window())

wordsFrame = Frame(mainFrame, width=50, background='Whitesmoke', )
wordsFrame.grid(row=1, column=0, pady=(10, 0), sticky="nsew", )
wordsFrame.grid_columnconfigure(1, weight=1)

searchBox = Entry(wordsFrame, font=("Times", 16))
searchBox.pack(fill=X, anchor='nw', side=TOP, padx=10, pady=(10, 0))


# searchBox.grid(row=0, column=0,padx=10, pady=10, sticky="nsew")

#
# def open_login_window():
#     root.destroy()
#     import login

def on_resize_window(event):
    parent_width = defFrame.winfo_width()
    defDescription.config(wraplength=parent_width - 20)


def on_entry_change(word):
    w = searchBox.get()
    if not word:
        filteredList = wordList
    else:
        filteredList = [_w for _w in wordList if _w['title'].startswith(w)]
    renderList(filteredList)


searchBox.bind("<KeyRelease>", on_entry_change)


def on_select(event):
    selected_index = listbox.curselection()  # Get the selected item's index
    if selected_index:
        item = listbox.get(selected_index)

        index = None
        for i, obj in enumerate(wordList):
            if obj["title"] == item:
                index = i
                break
        selected_item = filteredList[index]
        if not 'example' in selected_item:
            selected_item['example'] = ''
        setWordDefinition(selected_item['title'], selected_item['description'], selected_item['example'])


def renderList(list):
    listbox.delete(0, END)
    for item in list:
        listbox.insert(END, item['title'])


def setWordDefinition(title: str, description: str = '', example: str = ""):
    defTitle.config(text=title)
    defDescription.config(text=description)

    if not example:
        exFrame.pack_forget()
    else:
        exFrame.pack(fill=X, anchor='nw', padx=10, pady=10)
        exLabel.config(text=example)


wordListFrame = Frame(wordsFrame, background='white')
wordListFrame.pack(fill=BOTH, expand=True, anchor='nw', side=TOP, padx=10, pady=10)
listbox = Listbox(wordListFrame, borde=0, takefocus=0, highlightcolor='#ffffff', height=16, borderwidth=0,
                  highlightthickness=0)
listbox.pack(expand=True, fill=BOTH, padx=10, pady=10)
listbox.bind("<<ListboxSelect>>", on_select)
renderList(wordList)

defFrame = Frame(mainFrame)
defFrame.grid(row=1, column=1, padx=(10, 0), pady=(10, 0), sticky="nsew")

defTitle = Label(defFrame, text='', font=('ubuntu', 18), anchor='w')
defTitle.pack(fill=X, anchor='nw', side=TOP, padx=10, pady=(10, 0))

defDescription = Label(defFrame, text='', anchor="w", justify='left')
defDescription.pack(fill=X, anchor='nw', padx=10, pady=(4, 10))


exFrame = Frame(defFrame, background='#1F2122')
exFrame.pack(fill=X, anchor='nw', padx=10, pady=10)
exLabel = Label(exFrame, text='', anchor="w", justify='left', background='#1F2122', fg='white')
exLabel.pack(fill=X, anchor='nw', padx=10, pady=(4, 10))
exFrame.pack_forget()

entries_frame = Frame(root, bg=lighColor)
root.bind("<Configure>", on_resize_window)
root.mainloop()