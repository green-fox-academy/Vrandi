from tkinter import *


master = Tk()
size = 400
w = Canvas(master, width=size, height=size)
w.pack()

color = 'grey'
for i in range(0, size+1, 20):
    w.create_line(0, i+20, i+20, size, fill=color, width=2)
    w.create_line(i+20, 0, size, i+20, fill=color, width=2)
    w.create_line(i+20, size, size, size-i, fill=color, width=2)
    w.create_line(0, i+20,  size-i, 0, fill=color, width=2)

w.create_line(200, 100, 200, size-100, fill='lightblue', width=2)
w.create_line(100, 200, size-100, 200, fill='lightblue', width=2)

for i in range(0, 101, 10):
    w.create_line(100+i, 200, 200, 200-i, fill='lightblue', width=2)
    w.create_line(200, 100+i, 200+i, 200, fill='lightblue', width=2)
    w.create_line(100+i, 200, 200, 200+i, fill='lightblue', width=2)
    w.create_line(200, 200+i, 300-i, 200, fill='lightblue', width=2)


mainloop()
