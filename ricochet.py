import sys
import time
import tkinter as tk
import random
import math

x=192
y=108
v=80

velocity=int (1000/v)

size = (math.sqrt((x*y)/100))

number_of_colors=1

color="black"

def colorpick():
    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
    global particle
    canvas.itemconfig(particle,fill=color)
    

window = tk.Tk()
window.geometry(str(x)+"x"+str(y))

canvas = tk.Canvas(window, bg="white", height=y, width=x)

particle = canvas.create_oval(0,0,size,size,
                              fill=color)

canvas.grid()


def move():
    xm = 1
    ym = 1
    while True:
        canvas.move(particle, xm, ym)
        canvas.after(velocity)
        canvas.update()
        c = canvas.coords(particle)
        if c[3] >= y:
            ym=-1
            colorpick()
        elif c[0] <= 0:
            xm=1
            colorpick()
        elif c[2] >= x:
            xm=-1
            colorpick()
        elif c[1] <= 0:
            ym=1
            colorpick()
        

move()

window.mainloop()
