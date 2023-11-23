from location_tracking import *
from button_press import *
from threading import Thread

# define alpha for filtering
alpha = 0.5
filtered_value = None

def exponential_filter(incoming_value):
   global filtered_value

   if(filtered_value == None):
      filtered_value = incoming_value
   else:
      filtered_value = alpha * incoming_value + (1 - alpha) * incoming_value

   return filtered_value

# this is used for streaming 2 endpoints at the same time
def streaming_endpoints():
    # create websocket threads
    location_thread = Thread(target=location_streaming)
    event_thread = Thread(target=event_streaming)

    # start the threads
    location_thread.start()
    event_thread.start()

if __name__ == "__main__":
   # stream endpoints simutaneously
   streaming_endpoints()