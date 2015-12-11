from tkinter import *

root = Tk()
size = 500
c = Canvas(root, width = size, height = size)
c.pack()

def animate():
    i = 1
    while i != 0:
        c.move(ball, 6, )
        root.after(33, animate)


ball = c.create_oval(0, 25, 50, 75)
animate()
root.mainloop()
