import tkinter
from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tkinter.Tk()
root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())

var1 = StringVar()
w = Label(root, textvariable=var1,font=("Helvetica", 16)).pack()
var1.set("GeoPi Tracker")


def generate_ui(status,rl,rlo,d):
    def our_coordnates():
        print(var5.get())
        print(var6.get())
        return

    #
    w = Label(root, text="Status : ",font=("Helvetica", 10))
    w.place(x = 200, y = 100 , width=120, height=25)
    var2 = StringVar()
    w1 = Label(root, textvariable=var2,font=("Helvetica", 10),bg="white")
    w1.place(x =300 , y = 100 , width=120, height=25)
    var2.set(status)
    #
    s = Label(root, text="Our Latitude : ",font=("Helvetica", 10))
    s.place(x = 200, y = 175 , width=120, height=25)
    var5 = StringVar()
    s1 = Entry(root, textvariable=var5,font=("Helvetica", 10),bg="white")
    s1.place(x =350 , y = 175 , width=120, height=25)
    #
    t = Label(root, text="Our Longitude : ",font=("Helvetica", 10))
    t.place(x = 600, y = 175 , width=120, height=25)
    var6 = StringVar()
    t1 = Entry(root, textvariable=var6,font=("Helvetica", 10),bg="white")
    t1.place(x = 750 , y = 175 , width=120, height=25)
    #
    b = tk.Button(root, text="Submit", command=our_coordnates).pack()
    #b.place(x = 900, y = 175)
    #
    x = Label(root, text="Remote Latitude : ",font=("Helvetica", 10))
    x.place(x = 200, y = 250 , width=120, height=25)
    var3 = StringVar()
    x1 = Label(root, textvariable=var3,font=("Helvetica", 10),bg="white")
    x1.place(x =350 , y = 250 , width=120, height=25)
    var3.set(rl)
    #
    y = Label(root, text="Remote Longitude : ",font=("Helvetica", 10))
    y.place(x = 600, y = 250 , width=120, height=25)
    var4 = StringVar()
    y1 = Label(root, textvariable=var4,font=("Helvetica", 10),bg="white")
    y1.place(x =750 , y = 250, width=120, height=25)
    var4.set(rlo)
    #
    z = Label(root, text="Distance : ", font=("Helvetica", 10))
    z.place(x=900, y=250, width=120, height=25)
    var7 = StringVar()
    z1 = Label(root, textvariable=var4, font=("Helvetica", 10), bg="white")
    z1.place(x=1020, y=250, width=120, height=25)
    var7.set(d)


generate_ui(30,40,50,60)
root.mainloop()
