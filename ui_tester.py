import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from ui import UI
from PIL import ImageTk,Image


def animate(x, y):
    xdata.append(x)
    ydata.append(y)
    graph.set_data(xdata, ydata)
    return graph


user = UI()

i = 10
fig = plt.figure()
plt.xlim(-100, 100)
plt.ylim(-100, 100)
plt.axhline(y=0, color='r')
plt.axvline(x=0, color='r')

plt.xlabel("Distance Units (meters)")
plt.ylabel("Distance Units (meters)")
plt.title("Trajectory of the other Device.")
xdata, ydata = [], []
graph, = plt.plot([], [], '-')

for x in range(0,10):
    ani = FuncAnimation(fig, animate(i, i), frames=10, interval=200)
    plt.savefig('graph.png')
    user.set_graph('graph.png')
    i = i + 10

time.sleep(3)
user.render()
time.sleep(5)

user.set_status("Hell")
user.set_our_location(100, 500)
user.set_remote_location(1000, 5000)
user.set_distance(10)
