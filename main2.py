import tkinter as tk
from tkinter import ttk, messagebox

# Global list to store books
books = []

def create_main_window():
    root = tk.Tk()
    root.title("Simple Library Management")
    root.geometry("500x600")
    return root

def create_widgets(root):
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both"padx=10, pady=10)
    
    add_frame = ttk.Frame(notebook)
    view_frame = ttk.Frame(notebook)
    search_frame = ttk.Frame(notebook)
    
    notebook.add(add_frame, text="Add Book")
    notebook.add(view_frame, text="Add Book")
    notebook.add(search_frame, text="Add Book")
    
    create_add_book_widgets(add_frame)
    create_view_book_widgets(view_frame)
    create_search_book_widgets(search_frame)
    
def create_add_book_widgets(parents):
    tk.Label(parent, text="Title:").grid(row=0, column=0, padx=5, pady=5)
    title_entry = tk.Entry(parent)
    title_entry.grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(parent, text="Author:").grid(row=1, column=0, padx=5, pady=5)
    title_entry = tk.Entry(parent)
    title_entry.grid(row=1, column=1, padx=5, pady=5)
    
    add_button = tk.Button(parent, text="Add Book", command=lambda: add_book(title_entry, author_entry))
    add_button.grid(row=2, column=1, padx=5, pady=10)
    
def create_add_book_widgets(parents):
    tk.Label(parent, text="Title:").grid(row=0, column=0, padx=5, pady=5)
    title_entry = tk.Entry(parent)
    title_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(parent, text="Author:").grid(row=1, column=0, padx=5, pady=5)
    author_entry = tk.Entry(parent)
    author_entry.grid(row=1, column=1, padx=5, pady=5)

    add_button = tk.Button(parent, text="Add Book", command=lambda: add_book(title_entry, author_entry))
    add_button.grid(row=2, column=1, padx=5, pady=10)
    
def create_view_books_widgets(parent):
    global tree
    tree = ttk.Treeview(parent, columns=("Title", "Author"), show="headings")
    tree.heading("Title", text="Title")
    tree.heading("Author", text="Author")
    tree.pack(expand=True, fill="both", padx=10, pady=10)

    refresh_button = tk.Button(parent, text="Refresh", command=refresh_book_list)
    refresh_button.pack(pady=5)
    
def create_search_book_widgets(parent):
    tk.Label(parent, text="Search:").grid(row=0, column=0, padx=5, pady=5)
    search_entry = tk.Entry(parent)
    search_entry.grid(row=0, column=1, padx=5, pady=5)

    search_button = tk.Button(parent, text="Search", command=lambda: search_book(search_entry))
    search_button.grid(row=1, column=1, padx=5, pady=5)

    global search_result
    search_result = ttk.Treeview(parent, columns=("Title", "Author"), show="headings")
    search_result.heading("Title", text="Title")
    search_result.heading("Author", text="Author")
    search_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    
def add_book(title_entry, author_entry):
    title = title_entry.get()
    author = author_entry.get()
    if title and author:
        books.append({"title": title, "author": author})
        messagebox.showinfo("Success", "Book added successfully!")
        title_entry.delete(0, tk.END)
        author_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter both title and author.")
        
def refresh_book_list():
    tree.delete(*tree.get_children())
    for book in books:
        tree.insert("", "end", values=(book["title"], book["author"]))
        
def search_book(search_entry):
    search_term = search_entry.get().lower()
    search_result.delete(*search_result.get_children())
    for book in books:
        if search_term in book["title"].lower() or search_term in book["author"].lower():
            search_result.insert("", "end", values=(book["title"], book["author"]))
            
root = create_main_window()
create_widgets(root)
root.mainloop()

def create_delete_book_widgets(parent):
    global delete_tree
    delete_tree = ttk.Treeview(parent, columns=("Title", "Author"), show="headings")
    delete_tree.heading("Title", text="Title")
    delete_tree.heading("Author", text="Author")
    delete_tree.pack(expand=True, fill="both", padx=10, pady=10)

    delete_button = tk.Button(parent, text="Delete Selected", command=delete_selected_book)
    delete_button.pack(pady=5)

def delete_selected_book():
    selected_item = delete_tree.selection()
    if selected_item:
        item = delete_tree.item(selected_item)
        book = {"title": item["values"][0], "author": item["values"][1]}
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{book['title']}' by {book['author']}?")
        if confirm:
            books.remove(book)
            refresh_book_list()
            refresh_delete_book_list()
            messagebox.showinfo("Success", "Book deleted successfully!")
    else:
        messagebox.showerror("Error", "Please select a book to delete.")

def refresh_delete_book_list():
    delete_tree.delete(*delete_tree.get_children())
    for book in books:
        delete_tree.insert("", "end", values=(book["title"], book["author"]))

# Don't forget to add this to your create_widgets function:
# delete_frame = ttk.Frame(notebook)
# notebook.add(delete_frame, text="Delete Book")
# create_delete_book_widgets(delete_frame)