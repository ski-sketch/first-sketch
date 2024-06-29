from tkinter import *

window = Tk()
window.geometry('500x500')


canvas = Canvas(window, width = 500, height = 500, bg = 'white')
oval = canvas.create_oval(0, 0, 25, 25, fill='black')
canvas.pack()

def w(event):
    x=0
    y=-5
    canvas.move(oval, x, y)

def a(event):
    x=-5
    y=0
    canvas.move(oval, x, y)

def s(event):
    x=0
    y=5
    canvas.move(oval, x, y)

def d(event):
    x=5
    y=0
    canvas.move(oval, x, y)

window.bind('<w>',w)
window.bind('<a>',a)
window.bind('<s>',s)
window.bind('<d>',d)


window.mainloop()