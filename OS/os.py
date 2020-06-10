from threading import Thread
import tkinter as tk
import time

root = tk.Tk()
canvas = tk.Canvas(root, width=650, height=400, bg='white')
canvas.pack()
up = canvas.create_oval(300, 5, 300+50, 5+50, fill='red')
down = canvas.create_oval(300, 295, 300+50, 295+50, fill='blue')

def upper(ball):
    x = 0
    y=1
    while True:
        if canvas.coords(ball)[1] > 200:
           y = -1
        if canvas.coords(ball)[1] < 0:
           y = 1
        canvas.move(ball, x, y)
        time.sleep(0.005)

def lower(ball):
    x1 = -1
    y1 = -1
    while True:
        if canvas.coords(ball)[0] < 300 and canvas.coords(ball)[1] == 150:
           x1 = 1
           y1 = 1
        if canvas.coords(ball)[0] > 300 and canvas.coords(ball)[1] == 150:
           x1 = -1
           y1 = 1
        if canvas.coords(ball)[1] == 295:
            y1 = -1
        canvas.move(ball, x1, y1)
        time.sleep(0.005)    

Thread(target=upper,args=[up]).start()
Thread(target=lower,args=[down]).start()
root.mainloop()