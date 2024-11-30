import tkinter as tk
from tkinter import ttk, messagebox

books = []

def create_main_window():
    root = tk.Tk()
    root.title("Simple Library Management")
    root.geometry("400x300")
    return root

def create_widgets(root):
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both", padx=10, pady=10)

    add_frame = ttk.Frame(notebook)
    view_frame = ttk.Frame(notebook)
    search_frame = ttk.Frame(notebook)

    notebook.add(add_frame, text="Add Book")
    notebook.add(view_frame, text="View Books")
    notebook.add(search_frame, text="Search Book")

    create_add_book_widgets(add_frame)
    create_view_books_widgets(view_frame)
    create_search_book_widgets(search_frame)

