#this is the 2nd python script to add robot's algorithm
import time
from botVector import *
from location_tracking import *
from button_press import *
from Iiwari.Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi.Code.Server.Motor import *
from Iiwari.Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi.Code.Server.Light import *
from enum import Enum

# this class is used for setting the robot's status when an event occurs
class RobotStatus(Enum):
    IDLE = 1
    DUTY = 2
    LOST = 3

robot_tag = "0d47-3234-0474-81b9"
person_tag = "0d47-3234-0474-848b"
site = "017bcaaf-a074-f5fc-0b1e-083f26226deb" # savonia
token = login("savonia", "mAhti5aar1")

# initialize robot's components
motor = Motor()
light = Light()
status = RobotStatus()

# declare main points' coordinates

person_x = 0
person_y = 0
bot_x = 0
bot_y = 0
satisf_inaccuracy = 3

#TODO: finish a function
#should return a current position of a tag
def getLocation(tag_code: str) -> Point:
    pass


#TODO finish a function
#should return a status of button (is it pressed or not) 
#if true - return 2
def getStatus(tag: str) -> int:
    pass


# for demonstration purpose 
# the main idea for the demonstration algorithm is to align first (x-coordinate) 
# then (y-coordinate) with usage of vectors
def move_x(p_location: Point, r_location: Point) -> None:
    p_x = p_location.getX()
    r_x = r_location.getX()
    error = p_x - r_x
    #move forward
    if(error > 0):
        while(abs(error) > satisf_inaccuracy):
            motor.setMotorModel(1000,1000,1000,1000)
            r_x = getLocation(robot_tag).getX()
            error = p_x - r_x
    #move backward
    if(error < 0):
        while(abs(error) > satisf_inaccuracy):
            motor.setMotorModel(-1000,-1000,-1000,-1000)
            r_x = getLocation(robot_tag).getX()
            error = p_x - r_x



def move_y(p_location: Point, r_location: Point) -> None:
    p_y = p_location.getY()
    r_y = r_location.getY()
    error = p_y - r_y
    #move forward
    if(error > 0):
        while(abs(error) > satisf_inaccuracy):
            motor.setMotorModel(1000,1000,1000,1000)
            r_y = getLocation(robot_tag).getY()
            error = p_y - r_y
    #move backward
    if(error < 0):
        while(abs(error) > satisf_inaccuracy):
            motor.setMotorModel(-1000,-1000,-1000,-1000)
            r_y = getLocation(robot_tag).getY()
            error = p_y - r_y



def turn(p_location: Point, r_location: Point) -> None:
    r_y = r_location.getY()
    p_y = p_location.getY()
    #turn right 90 degrees
    if(r_y - p_y > 0):
        motor.setMotorModel(100, 2000, -2000, 100)
    #turn left 90 degrees 
    if(r_y - p_y < 0):
        motor.setMotorModel(-2000, 100, 100, 2000)



def movement(p_location: Point) -> None:
    if(getStatus(person_tag) == status.IDLE):
        pass
        #think what it can do while waiting
    
    if(getStatus(person_tag) == status.DUTY):
        r_location = getLocation(robot_tag)
        move_x(p_location, r_location)
        turn(p_location, r_location)
        move_y(p_location, r_location)



def approaching_person(tag_id):
    if(is_button_pressed == True):
        status = 2 # robot on duty for approaching a person

        # first move is to move forward
        motor.setMotorModel(1000, 1000, 1000, 1000)
    else:
        print("Robot on idle state")
        


def main():
    pass