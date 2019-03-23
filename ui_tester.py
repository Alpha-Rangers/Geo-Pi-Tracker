import time

from ui import UI

user = UI()
time.sleep(3)
user.render()
time.sleep(5)

user.set_status("Hell")
user.set_our_location(100, 500)
user.set_remote_location(1000, 5000)
user.set_distance(10)
