# the pack geometry manager organizes widgets in blocks before placing them i the parent widget.
# it is suitable for simple layouts where widgets are stacked vertically or horizontally

#       USAGE
# side:specifies which side of the parent widget the child widget is packed against(top, bottom, left, right)
# fill:specifies how the widget should expand to fill any extra space (x, y, both, none)
# expand: if set to true, the widget expands to fill any extra space in the parent widget
# padx:horizontal padding around the widget
# pady:vertical padding around the widget

#       EXAMPLE
from tkinter import Tk, Label

root = Tk()
label1 = Lable(root, text="Label 1", bg="red")
label2 = Lable(root, text="Label 2", bg="blue")
label3 = Lable(root, text="Label 3", bg="green")

label1.pack(side="top", fill="x", padx=5, pady=5)
label2.pack(side="top", fill="x", padx=5, pady=5)
label3.pack(side="top", fill="x", padx=5, pady=5)

root.mainloop()

# grid geometry maneger places widgets in a 2D grid
# this is usefulfor more complex layouts where widgets need to be allined in rows and columns

#       USAGE

# row : row number where the widget is placed
# column : column number where the widget is placed
# columnspan : Number of columns the widget should span
# rowspan : Number of rows the widget should span
# sticy : specifies which sides of the cell the widget sticks to (e.g. N, S, E, W)
# padx:horizontal padding around the widget
# pady:vertical padding around the widget

from tkinter import Tk, Label

label1 = Lable(root, text="Label 1", bg="red")
label2 = Lable(root, text="Label 2", bg="blue")
label3 = Lable(root, text="Label 3", bg="green")
label4 = Lable(root, text="Label 4", bg="yellow")