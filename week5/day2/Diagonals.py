from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()


x = 0
y = 0
if x == y == 0:  
    teal_line = canvas.create_line(x, y, 200, 50, fill='green')
else : 
    teal_line = canvas.create_line(x, y, 200, 50, fill='red')

root.mainloop()