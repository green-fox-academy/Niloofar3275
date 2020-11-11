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