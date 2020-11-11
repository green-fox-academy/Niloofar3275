  
from tkinter import *
import random
root = Tk()

canvas = Canvas(root, width='500', height='500')
canvas.pack()
colors = ["red" , "green" , "blue" , "black"]

def draw_rectangles(x0,y0,x1,y1,c):  
    canvas.create_rectangle(x0,y0,x1,y1,fill = c)

for i in range(0,4): 
    c=colors[random.randint(0,3)]
    draw_rectangles(random.randint(0,300),random.randint(0,300),random.randint(0,300),random.randint(0,300),c)
# Draw four different size and color rectangles.
# Avoid code duplication.

root.mainloop()