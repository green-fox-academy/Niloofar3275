from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

canvas.create_line(100, 100, 200, 100, fill='red')

canvas.create_line(100, 100, 100, 200, fill='green')


root.mainloop()