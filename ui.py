import time
import tkinter
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class UI:
    """Class to handle UI"""
    root = tkinter.Tk()

    status_variable = StringVar(root)
    our_lat_variable = StringVar(root)
    our_long_variable = StringVar(root)
    remote_lat_variable = StringVar(root)
    remote_long_variable = StringVar(root)
    distance_variable = StringVar(root)

    def __init__(self):
        self.root.attributes('-fullscreen', True)
        self.root.bind('<Escape>', lambda e: self.root.destroy())

        self.status_variable.set("-")
        self.our_lat_variable.set("-")
        self.our_long_variable.set("-")
        self.remote_lat_variable.set("-")
        self.remote_long_variable.set("-")
        self.distance_variable.set("-")
        print("before set status : ")
        print(self.status_variable.get())

        Label(self.root, text="GeoPi Tracker", font=("Helvetica", 16)).pack()

        Label(self.root, text="Status : ", font=("Helvetica", 10)).place(x=200, y=100, width=120, height=25)
        self.Status_label = Label(self.root, textvariable=self.status_variable, font=("Helvetica", 10), bg="white").place(x=300, y=100,width=120, height=25)

        Label(self.root, text="Our Latitude : ", font=("Helvetica", 10)).place(x=200, y=175, width=120, height=25)
        self.Self_Lat_label = Label(self.root, textvariable=self.our_lat_variable, font=("Helvetica", 10), bg="white").place(x=350, y=175, width=120, height=25)

        Label(self.root, text="Our Longitude : ", font=("Helvetica", 10)).place(x=600, y=175, width=120, height=25)
        self.Self_Long_label = Label(self.root, textvariable=self.our_long_variable, font=("Helvetica", 10), bg="white").place(x=750, y=175, width=120, height=25)

        Label(self.root, text="Remote Latitude : ", font=("Helvetica", 10)).place(x=200, y=250, width=120, height=25)
        self.Remote_Lat_label = Label(self.root, textvariable=self.remote_lat_variable, font=("Helvetica", 10), bg="white").place(x=350, y=250, width=120, height=25)

        Label(self.root, text="Remote Longitude : ", font=("Helvetica", 10)).place(x=600, y=250, width=120, height=25)
        self.Remote_Long_label = Label(self.root, textvariable=self.remote_long_variable, font=("Helvetica", 10), bg="white").place(x=750, y=250, width=120, height=25)

        Label(self.root, text="Distance : ", font=("Helvetica", 10)).place(x=900, y=250, width=120, height=25)
        self.distance_label = Label(self.root, textvariable=self.distance_variable, font=("Helvetica", 10), bg="white").place(x=1020, y=250, width=120, height=25)

        LabelFrame(self.root, text="Trajectory Covered", height=500, width=800).place(x=350, y=300)

    def render(self):
        self.root.update()
        time.sleep(10)

    def set_status(self, stat):
        self.status_variable.set(repr(stat))
        self.render()

    def set_our_location(self, lat, long):
        self.our_lat_variable.set(lat)
        self.our_long_variable.set(long)
        self.render()

    def set_remote_location(self, lat, long):
        self.remote_lat_variable.set(lat)
        self.remote_long_variable.set(long)
        self.render()

    def set_distance(self, distance):
        self.distance_variable.set(distance)
        self.render()

    def set_graph(self, graph):
        canvas = FigureCanvasTkAgg(graph, master=self.root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=350, y=300)
        canvas.get_tk_widget().grid_size(500, 800)

        toolbar = NavigationToolbar2Tk(canvas, self.root)
        toolbar.update()
        canvas.get_tk_widget().place(x=350, y=300)
