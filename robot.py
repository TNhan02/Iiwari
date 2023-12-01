#this is the 2nd python script to add robot's algorithm
import time
import settings
from botVector import *
from person_stream import *
from button_press import *
from Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi.Code.Server.Motor import *
from Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi.Code.Server.Light import *
#from Iiwari.Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi.Code.Server.Light import *
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

person_x = 25
person_y = 25
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
def getStatus():
    if(settings.is_button_pressed == True):
        status = 2
        return status
    return status


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


def check_approach(accept_distance: float) -> bool:
    #change function
    r_location = getLocation()
    r_x = r_location.getX()
    r_y = r_location.getY()

    #change function
    p_location = getLocation()
    p_x = p_location.getX()
    p_y = p_location.getY()

    value = math.sqrt((p_x - r_x)**2 + (p_y - r_y)**2)
    if(value > accept_distance):
        return False
    else:
        return True
    

def rotate(angle: float) -> None:
    rotate_angle = 180-angle
    rotation_time = rotate_angle* (0.88/90)
    motor.setMotorModel(2000,2000,-2000,-2000)
    time.sleep(rotation_time)
    motor.destroy()

#Final version of the movement algorithm

def movement() -> None:
    status = RobotStatus.IDLE.value
    while True:
        match (status):
            case RobotStatus.IDLE.value:
                if(settings.is_button_pressed):
                    status = RobotStatus.DUTY.value
                    break
                else:
                    time.sleep(2)
                continue
            
            case RobotStatus.DUTY.value:
                #change to appropriate function
                r_locationInitial = getLocation(robot_tag)
                motor.setMotorModel(1000,1000,1000,1000)
                time.sleep(1)
                motor.destroy()
                #change to appropriate function
                p_location = getLocation(person_tag)
                r_locationCurrent = getLocation(robot_tag)

                r_vector = Vector(r_locationCurrent, r_locationInitial)
                r_p_vector = Vector(p_location, r_locationCurrent)
                angle = angleBetweenVectors(r_vector, r_p_vector)
                #calibration is required 
                rotate(angle)

                while(not check_approach(5)):
                    motor.setMotorModel(1000,1000,1000,1000)
                motor.destroy()
                status = RobotStatus.IDLE.value
                break


def approaching_person(tag_id):
    if(settings.is_button_pressed == True):
        status = 2 # robot on duty for approaching a person

        # first move is to move forward
        motor.setMotorModel(1000, 1000, 1000, 1000)
    else:
        print("Robot on idle state")
        


def main():
    #test values
    p_location = Point(0, person_y)
    r_location = Point()

    turn(p_location, r_location)


if __name__ == '__main__':
    main()