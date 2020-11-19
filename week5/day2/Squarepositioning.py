from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()


def create_square(x,y): 
    x0 = x
    y0 = y
    x1 = x + 50
    y1 = y + 50

    canvas.create_line(x0, y0, x1, y0, fill='red')
    
    canvas.create_line(x0, y0, x0, y1, fill='red')

    canvas.create_line(x0, y1, x1, y1, fill='red')

    canvas.create_line(x1, y1, x1, y0, fill='red')

for i in range (1,4): 
    create_square(i*10,i*10)



# Create a function that draws one square and takes 2 parameters:
# The x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# Draw 3 squares with that function.
# Avoid code duplication.

root.mainloop()