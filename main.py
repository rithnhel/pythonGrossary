import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def fetch_technical_word():
    word = entry.get()
    response = requests.get(f"https://docs.python.org/3/glossary.html#term-{word}")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content_text = soup.find("dl", class_="glossary").text
        content.delete(1.0, tk.END)
        content.insert(tk.END, content_text)
    else:
        content.delete(1.0, tk.END)
        content.insert(tk.END, "Word not found in Python Glossary.")

root = tk.Tk()
root.title("Python Technical Glossary")

# Left sidebar for search
left_sidebar = tk.Frame(root, width=200, bg="#f0f0f0", height=600)
left_sidebar.pack_propagate(False)
left_sidebar.pack(side=tk.LEFT, fill=tk.Y)

label = tk.Label(left_sidebar, text="Search Technical Word:")
label.pack(pady=(20, 10))

entry = tk.Entry(left_sidebar, width=20)
entry.pack(pady=10)

search_button = tk.Button(left_sidebar, text="Search", command=fetch_technical_word)
search_button.pack(pady=(10, 20))

# Right sidebar for content display
right_sidebar = tk.Frame(root, width=400, bg="#ffffff", height=600)
right_sidebar.pack_propagate(False)
right_sidebar.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

content = tk.Text(right_sidebar, wrap=tk.WORD)
content.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

root.mainloop()
