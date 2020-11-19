from tkinter import *

root = Tk()


canvas = Canvas(root, width='300', height='300')
canvas.pack()
Tk.update(root)
center_x = canvas.winfo_width()/2
center_y = canvas.winfo_height()/2

def create_square(coordinates):
    size = int(coordinates)
    x0 = y1 =  center_x - (int(coordinates) / 2)
    y0 = x1 =  center_y + (int(coordinates) / 2)
    
    

    canvas.create_line(x0, y0, x1, y0, fill='red')
    
    canvas.create_line(x0, y0, x0, y1, fill='red')

    canvas.create_line(x0, y1, x1, y1, fill='red')

    canvas.create_line(x1, y1, x1, y0, fill='red')


for i in range (1,4): 
    create_square(60*i)
 

# Create a function that draws one square and takes 1 parameters:
# The square size
# and draws a square of that size to the center of the canvas.
# Draw 3 squares with that function.
# Avoid code duplication.

root.mainloop()