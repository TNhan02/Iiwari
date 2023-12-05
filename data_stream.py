import settings
import botVector

# define alpha for filtering, filtered x and y of person and robot
alpha = 0.5
filtered_value = 0.0
filtered_person_x = None 
filtered_person_y = None
filtered_robot_x = None
filtered_robot_y = None

#TODO: how to apply it when streaming?
# this function is used to filter data to make it more calm
def exponential_filter(incoming_value):
   global filtered_value
   if(incoming_value != None):
      filtered_value = alpha * incoming_value + (1 - alpha) * filtered_value

   return filtered_value

# return person_location - location of person when button is pressed
def person_location_data(location):
   global filtered_person_x, filtered_person_y
   filtered_person_x = exponential_filter(location["x"])
   filtered_person_y = exponential_filter(location["y"])
   settings.person_location = botVector.Point(filtered_person_x, filtered_person_y)

# return robot_location - location of robot while on duty
def robot_location_data(location):
   global filtered_robot_x, filtered_robot_y
   filtered_robot_x = exponential_filter(location["x"])
   filtered_robot_y = exponential_filter(location["y"])
   settings.robot_location = botVector.Point(filtered_robot_x, filtered_robot_y)