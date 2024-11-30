from tkinter import Tk, Button

def on_click():
    print("Button clicked!")

def clickable_button():
    root = Tk()
    root.title("Clickable Button")
    
    button = Button(root, text="Click Me", command=on_click)
    button.pack(padx=20, pady=20)
    
    root.mainloop()
    
    clickable_button()