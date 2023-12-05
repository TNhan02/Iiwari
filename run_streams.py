import person_stream
import event_stream
import robot_stream
#import robot
import settings
from threading import Thread

# this is used for streaming 2 endpoints at the same time
def streaming_endpoints():
   settings.init()

   # create websocket threads
   person_thread = Thread(target=person_stream.person_streaming)
   event_thread = Thread(target=event_stream.event_streaming)
   robot_thread = Thread(target=robot_stream.robot_streaming)
   #robot_movement_thread = Thread(target=robot.movement)

   # start the threads
   person_thread.start()
   event_thread.start()
   robot_thread.start()
   #robot_movement_thread.start()

if __name__ == "__main__":
   streaming_endpoints()