from location_tracking import *
from button_press import *
from threading import Thread

# this is used for streaming 2 endpoints at the same time
def streaming_endpoints():
   # create websocket threads
   location_thread = Thread(target=location_streaming)
   event_thread = Thread(target=event_streaming)

   # start the threads
   location_thread.start()
   event_thread.start()

# this is an example of streaming locations and events simutaneously
# this one should be called similarly in robot.py in the end
if __name__ == "__main__":
   # stream endpoints simutaneously
   streaming_endpoints()