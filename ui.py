import tkinter
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class UI:
    """Class to handle UI"""

    def __init__(self):
        root = tkinter.Tk()
        root.attributes('-fullscreen', True)
        root.bind('<Escape>', lambda e: root.destroy())

        init_variable = "-"

        Label(root, text="GeoPi Tracker", font=("Helvetica", 16)).pack()

        Label(root, text="Status : ", font=("Helvetica", 10)).place(x=200, y=100, width=120, height=25)
        Label(root, textvariable=init_variable, font=("Helvetica", 10), bg="white").place(x=300, y=100,width=120, height=25)

        Label(root, text="Our Latitude : ", font=("Helvetica", 10)).place(x=200, y=175, width=120, height=25)
        Label(root, textvariable=init_variable, font=("Helvetica", 10), bg="white").place(x=350, y=175, width=120, height=25)

        Label(root, text="Our Longitude : ", font=("Helvetica", 10)).place(x=600, y=175, width=120, height=25)
        Label(root, textvariable=init_variable, font=("Helvetica", 10), bg="white").place(x=750, y=175, width=120, height=25)

        Label(root, text="Remote Latitude : ", font=("Helvetica", 10)).place(x=200, y=250, width=120, height=25)
        Label(root, textvariable=init_variable, font=("Helvetica", 10), bg="white").place(x=350, y=250, width=120, height=25)

        Label(root, text="Remote Longitude : ", font=("Helvetica", 10)).place(x=600, y=250, width=120, height=25)
        Label(root, textvariable=init_variable, font=("Helvetica", 10), bg="white").place(x=750, y=250, width=120, height=25)

        Label(root, text="Distance : ", font=("Helvetica", 10)).place(x=900, y=250, width=120, height=25)
        Label(root, textvariable=init_variable, font=("Helvetica", 10), bg="white").place(x=1020, y=250, width=120, height=25)

        LabelFrame(root, text="Trajectory Covered", height=500, width=800).place(x=350, y=300)

    def set_status(self, stat):
        Label(self.root, textvariable=stat, font=("Helvetica", 10), bg="white").place(x=300, y=100, width=120, height=25)

    def set_our_location(self, lat, long):
        Label(self.root, textvariable=lat, font=("Helvetica", 10), bg="white").place(x=350, y=175, width=120, height=25)
        Label(self.root, textvariable=long, font=("Helvetica", 10), bg="white").place(x=750, y=175, width=120, height=25)

    def set_remote_location(self, lat, long):
        Label(self.root, textvariable=lat, font=("Helvetica", 10), bg="white").place(x=350, y=250, width=120, height=25)
        Label(self.root, textvariable=long, font=("Helvetica", 10), bg="white").place(x=750, y=250, width=120, height=25)

    def set_distance(self, distance):
        Label(self.root, textvariable=distance, font=("Helvetica", 10), bg="white").place(x=1020, y=250, width=120, height=25)

    def set_graph(self, graph):
        canvas = FigureCanvasTkAgg(graph, master=self.root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().place(x=350, y=300)
        canvas.get_tk_widget().grid_size(500, 800)

        toolbar = NavigationToolbar2Tk(canvas, self.root)
        toolbar.update()
        canvas.get_tk_widget().place(x=350, y=300)

