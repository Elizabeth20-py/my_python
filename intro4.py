from tkinter import Tk, Label, Entry, Button

def add_numbers():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    label_result.config(text=f"Result: {result}")
    
def simple_calculator():
    root = Tk()
    root.title("Simple Calculator") 
    
    global entry1, entry2, label_result
    entry1 = Entry(root)
    entry1.pack(padx=20, pady= 5)
    
    entry2 = Entry(root)
    entry2.pack(padx=20, pady= 5)
    
    button = Button(root, text="Add", command=add_numbers)
    button.pack(padx=20, pady=5)
    
    label_result = Label(root, text="Result: ")
    label_result.pack(padx=20, pady=5)
    
    root.mainloop()
    
simple_calculator()