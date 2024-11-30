import tkinter as tk
from tkinter import ttk, messagebox

# Global list to store books
books = []

def creat_main_window():
    root = tk.Tk()
    root.title("Simple Library Management")
    root.geometry("500x600") # SET THE SIZE OF THE WINDOW
    return root

def creat_widgets(root):
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both", padx=10, pady=10)
    
    add_frame = ttk.Frame(notebook)
    view_frame = ttk.Frame(notebook)
    search_frame = ttk.Frame(notebook)
    
    notebook.add(add_frame, text="Add Books")
    notebook.add(view_frame, text="Frame Books")
    notebook.add(search_frame, text="Search Books")
    
    create_add_book_widgets(add_frame)
    create_view_books_widgets(view_frame)
    create_search_book_widgets(search_frame)

def create_add_book_widgets(parent):
    tk.Label(parent, text="Title:").grid(row=0, column=0, padx=5, pady=5)
    title_entry = tk.Entry(parent)
    title_entry.grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(parent, text="Author:").grid(row=0, column=0, padx=5, pady=5)
    author_entry = tk.Entry(parent)
    author_entry.grid(row=1, column=1, padx=5, pady=5)
    
    add_button = tk.Button(parent, text="Add book", command=lambda: add_book(title_entry, author_entry))
    add_button.grid(row=2, column=1, padx=5, pady=5)
    
def create_view_books_widgets(parent):
    global tree
    tree = ttk.Treeview(parent, columns=("Title", "Author"), show="headings")
    tree.heading("Title", text="Title")
    tree.heading("Author", text="Author")
    tree.pack(expand=True, fill="both", padx=10, pady=10)
    
    refresh_button = tk.Button(parent, text="Refresh", command=refresh_book_list)
    refresh_button.pack(pady=15)
    
def create_search_book_widgets(parent):
    tk.Label(parent, text="Title:").grid(row=0, column=0, padx=5, pady=5)
    title_entry = tk.Entry(parent)
    title_entry.grid(row=0, column=1, padx=5, pady=5)
    
    search_button = tk.Button(parent, text="Search", command=lambda: search_book(title_entry))
    search_button.grid(row=1, column=1, padx=5, pady=5)
    
    global search_result
    search_result = ttk.Treeview(parent, columns=("Title", "Author"), show="headings")
    search_result.heading("Title", text="Title")
    search_result.heading("Author", text="Author")
    search_result.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
    
def add_book(title_entry, author_entry):
     title = title_entry.get()# used to take the text from the entry widget
     author = author_entry.get()
     if title and author:
         books.append({"title":title, "author":author})
         messagebox.showinfo("Success", "Book added successfully!")
         title_entry.delete(0, tk.END)
         author_entry.delete(0, tk.END)
     else:
         messagebox.showerror("Error", "Please enter both title and author.")
        
def refresh_book_list():
    tree.deleted(*tree.get_children())
    for book in books:
        tree.insert("","end", values=(book["title"], book["author"]))
        
def search_book(search_entry):
    search_term = search_entry.get().lower()
    search_result.delete(*search_result.get_children())
    for book in books:
        if search_term in book["title"].lower() or search_term in book["author"].lower():
            search_result.insert("","end", values=(book["title"], book["author"]))

def create_delete_book_widgets(parent):
    global delete_tree
    delete_tree = ttk.Treeview(parent, columns=("Title", "Author"), show="headings")
    delete_tree.heading("Title", text="Title")
    delete_tree.heading("Author", text="Author")
    delete_tree.pack(expand=True, fill="both", padx=10, pady=10)

    delete_button = tk.Button(parent, text="Delete Selected", command=delete_selected_book)
    delete_button.grid(row=1, column=1, padx=5, pady=5)

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
# Main program
root = creat_main_window()
creat_widgets(root)
root.mainloop()
# Main program
root = create_main_window()
root.withdraw()  # Hide the main window until the user logs in

# Start with the signup window (or login if the user has already signed up)
if not users:
    signup()
else:
    login()
    
