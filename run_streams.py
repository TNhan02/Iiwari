from person_stream import *
from event_stream import *
from robot_stream import *
from threading import Thread

# this is used for streaming 2 endpoints at the same time
def streaming_endpoints():
   # create websocket threads
   location_thread = Thread(target=location_streaming)
   event_thread = Thread(target=event_streaming)
   #robot_thread = Thread(target=robot_streaming)

   # start the threads
   location_thread.start()
   event_thread.start()
   #robot_thread.start()

if __name__ == "__main__":
   settings.init()
   streaming_endpoints()