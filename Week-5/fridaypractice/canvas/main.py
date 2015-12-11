from tkinter import *
from movingball import *

master = Tk()

canvas = Canvas(master, width=400, height=400)
canvas.pack()

canvas.create_rectangle(0, 0, 400, 400, fill='#fff')
ball = Ball((250, 200), (2, -2), 10)
while True:
    ball.move()
    bbox = ball.get_bbox()
    canvas.create_rectangle(0, 0, 400, 400, fill='#fff')
    canvas.create_oval(bbox, fill='pink')
    canvas.after(1000 // 60)
    canvas.update()

mainloop()
