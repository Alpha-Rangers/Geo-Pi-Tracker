import tkinter
from tkinter import *


root = tkinter.Tk()
root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())

var1 = StringVar()
w = Label(root, textvariable=var1,font=("Helvetica", 16)).pack()
var1.set("GeoPi Tracker")

def generate_ui(ol,olo,rl,rlo,d,status):
    #
    w = Label(root, text="Status : ",font=("Helvetica", 10))
    w.place(x = 200, y = 100 , width=120, height=25)
    var2 = StringVar()
    w = Label(root, textvariable=var2,font=("Helvetica", 10),bg="white")
    w.place(x =300 , y = 100 , width=120, height=25)
    var2.set(status)
    #
    s = Label(root, text="Our Latitude : ",font=("Helvetica", 10))
    s.place(x = 200, y = 175 , width=120, height=25)
    var5 = StringVar()
    s = Entry(root, textvariable=var5,font=("Helvetica", 10),bg="white")
    s.place(x =350 , y = 175 , width=120, height=25)
    var5.set(ol)
    #
    t = Label(root, text="Our Longitude : ",font=("Helvetica", 10))
    t.place(x = 600, y = 175 , width=120, height=25)
    var6 = StringVar()
    t = Entry(root, textvariable=var6,font=("Helvetica", 10),bg="white")
    t.place(x =750 , y = 175 , width=120, height=25)
    var6.set(olo)
    #
    x = Label(root, text="Remote Latitude : ",font=("Helvetica", 10))
    x.place(x = 200, y = 250 , width=120, height=25)
    var3 = StringVar()
    x = Label(root, textvariable=var3,font=("Helvetica", 10),bg="white")
    x.place(x =350 , y = 250 , width=120, height=25)
    var3.set(rl)
    #
    y = Label(root, text="Remote Longitude : ",font=("Helvetica", 10))
    y.place(x = 600, y = 250 , width=120, height=25)
    var4 = StringVar()
    y = Label(root, textvariable=var4,font=("Helvetica", 10),bg="white")
    y.place(x =750 , y = 250, width=120, height=25)
    var4.set(rlo)

generate_ui(10,20,30,40,50,60)

#graphFrame = LabelFrame(root, height = 500, width = 800, text = "Trajectory Covered")
#graphFrame.place(x=350,y=300)




root.mainloop()
