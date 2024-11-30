from tkinter import Tk, Label

def colorful_grid():
    root = Tk()
    root.title("Colorful Grid")
    
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    
    for i in range(2):
        for j in range(3):
            label = Label(root, text=f"Label {i* + j + 1}", bg=colors[i*3 + j])
            label.grid(row=i, column=j, padx=5, pady=5 sticky="nsew")
            
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    
    root.mainloop()
    
    colorful_grid()