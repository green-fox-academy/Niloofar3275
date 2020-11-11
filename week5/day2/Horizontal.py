from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def create_line(x,y):  
    x0 = x
    y0 = y

    canvas.create_line(x0, y0, 150, 150, fill='red')
    
    canvas.create_line(x0, y0, x0+50, y0, fill="blue")

for i in range(1,4):  
    create_line(10*i,10*i)



# Create a function that draws a single line and takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# Draw at least 3 lines with that function using a loop.

root.mainloop()