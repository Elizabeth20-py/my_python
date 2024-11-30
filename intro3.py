from tkinter import Tk, Label, Entry, Button

def show_name():
    name = entry.get()
    label.config(text=f"Hello, {name}!")
    
def entry_label_app():
    root = Tk()
    root.title("Entry and Label")
    
    global entry, Label
    entry = Entry(root)
    entry.pack(padx=20, pady=5)
    
    button = Button(root, text="Show Name", command=show_name)
    button.pack(padx=20, pady=5)
    
    label = Label(root, text="")
    label.pack(padx=20, pady=5)
    
    root.mainloop()
    
entry_label_app()
