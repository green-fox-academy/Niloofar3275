  
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()
center_x = canvas.winfo_width()/2
center_y = canvas.winfo_height()/2

def create_line(x,y):  
    center_x  = x
    center_y = y

    canvas.create_line(x, y, 150, 150, fill='red')

for i in range(0,3):  
    create_line(0,i*40)


# Create a function that draws a single line and takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# Draw at least 3 lines with that function using a loop.

root.mainloop()