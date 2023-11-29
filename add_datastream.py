import settings
import botVector

# define alpha for filtering
filtered_value = None
filtered_person_x = None
filtered_person_y = None
alpha = 0.5

#TODO: how to apply it when streaming?
# this function is used to filter data to make it more calm
def exponential_filter(incoming_value):
   global filtered_value
   if(incoming_value == None):
      filtered_value = incoming_value
   else:
      filtered_value = alpha * incoming_value + (1 - alpha) * incoming_value

   return filtered_value

def add_location_data(location):
    global filtered_person_x, filtered_person_y
    filtered_person_x = exponential_filter(location["x"])
    filtered_person_y = exponential_filter(location["y"])
    settings.person_location = botVector.Point(filtered_person_x, filtered_person_y)
