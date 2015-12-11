from tkinter import *

master = Tk()
w = Canvas(master, width=400, height=300)
w.pack()

w.create_rectangle(0, 0, 400, 300, fill='#ecf0f1')

a = 0
b = 20
g = 0
h = 20

c = 20
d = 40
e = 20
m = 40

for y in range(4):
    for x in range(4):
        w.create_rectangle(a, g, b, h, fill='#2c3e50')
        a += 40
        b += 40
        w.create_rectangle(c, e, d, m, fill='#2c3e50')
        c += 40
        d += 40
    a = 0
    b = 20
    g += 40
    h += 40
    c = 20
    d = 40
    e += 40
    m += 40

mainloop()
