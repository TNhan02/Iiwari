#this is the 2nd python script to add robot's algorithm
from botVector import *
from enum import Enum
import location_tracking_2023 as data_streaming
from .Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi.Code.Server.Motor import *
from .Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi.Code.Server.Light import *

# this class is used for setting the robot's status when an event occurs
class RobotStatus(Enum):
    IDLE = 1
    DUTY = 2
    LOST = 3

robot_tag = "0d47-3234-0474-81b9"
person_tag = "0d47-3234-0474-848b" # could be changed since this one doesn't work at all at 17.11.2023
site = "017bcaaf-a074-f5fc-0b1e-083f26226deb" # savonia
token = data_streaming.login("savonia", "mAhti5aar1")

# initialize robot's components
motor = Motor()
light = Light()
status = RobotStatus()

# declare main points' coordinates

person_x = 0
person_y = 0
bot_x = 0
bot_y = 0

#should return a current position of a tag
def getLocation(tag_code: str) -> Point:
    pass


def move():
    motor(1000, 1000, 1000, 1000)

# for demonstration purpose 
# the main idea for the demonstration algorithm is to align first (x-coordinate) 
# then (y-coordinate) with usage of vectors
def movement(p_location: Point, buttonState: bool, state: int) -> None:
    r_location = getLocation(robot_tag)
    (r_x, r_y) = (r_location.getX(), r_location.getY())
    (p_x, p_y) = (p_location.getX(), )
    
    if(r_x - p_x > ):
        motor.setMotorModel(-1000,-1000,-1000,-1000)
    if(r_x < p_x):
    


    



def approaching_person(tag_id):
    data = data_streaming.button_pressed(site, token)
    if(data == True):
        status = 2 # robot on duty for approaching a person

        # first move is to move forward
        motor.setMotorModel(1000, 1000, 1000, 1000)
    else:
        print("Robot on idle state")
        
