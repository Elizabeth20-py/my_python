from tkinter import Tk, Label

def hello_tkinter():
    root = Tk()
    root.title("Hello Tkinter")
    
    label = Label(root, text="Hello, Tkinter!")
    label. pack(padx=10, pady=100)
    
    root.mainloop()
    
hello_tkinter()