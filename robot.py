#this is the 2nd python script to add robot's algorithm
import time
import settings
import run_streams
from botVector import *
from person_stream import *
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
status = RobotStatus(1)

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
    #change function of robot
    r_location = settings.collector.getRobotLocation()
    r_x = r_location.getX()
    r_y = r_location.getY()

    #change function of person
    p_location = settings.collector.getPersonLocation()
    p_x = p_location.getX()
    p_y = p_location.getY()

    value = math.sqrt((p_x - r_x)**2 + (p_y - r_y)**2)
    if(value > accept_distance):
        return False
    else:
        return True
    

def rotate(angle: float, robot_y: float, person_y: float) -> None:
    rotate_angle = 180-angle
    rotation_time = rotate_angle* (0.88/90)
    if(robot_y < person_y):
        motor.setMotorModel(2000,2000,-2000,-2000)
    elif(robot_y > person_y):
        motor.setMotorModel(-2000,-2000,2000,2000)
    time.sleep(rotation_time)
    motor.setMotorModel(0,0,0,0)

#Final version of the movement algorithm

def movement() -> None:
    status = RobotStatus.IDLE
    
    while True:
        match (status):
            case RobotStatus.IDLE:
                if(settings.is_button_pressed):
                    status = RobotStatus.DUTY
                    continue
                else:
                    time.sleep(2)
                continue
            
            case RobotStatus.DUTY:
                #change to appropriate function
                motor.setMotorModel(1000, 1000, 1000, 1000)
                time.sleep(2)
                motor.setMotorModel(0,0,0,0)
                r_locationInitial = settings.collector.getInitRobotLocation()
                motor.setMotorModel(1000,1000,1000,1000)
                time.sleep(3)
                motor.setMotorModel(0,0,0,0)
                #change to appropriate function
                p_location = settings.collector.getPersonLocation()
                r_locationCurrent = settings.collector.getRobotLocation()

                r_vector = Vector(r_locationCurrent, r_locationInitial)
                r_p_vector = Vector(p_location, r_locationCurrent)
                angle = angleBetweenVectors(r_vector, r_p_vector)
                #calibration is required 
                rotate(angle, r_locationCurrent.getY(), p_location.getY())

                while(not check_approach(2)):
                    motor.setMotorModel(1000,1000,1000,1000)
                    time.sleep(1)
                motor.setMotorModel(0,0,0,0)
                status = RobotStatus.IDLE
                continue
    """
    time.sleep(3)
    motor.setMotorModel(1000,1000,1000,1000)
    time.sleep(2)
    motor.setMotorModel(0,0,0,0)
    time.sleep(5)
    r_locationInitial = settings.collector.getInitRobotLocation()
    p_location = settings.collector.getPersonLocation()
    motor.setMotorModel(-1000,-1000,-1000,-1000)
    time.sleep(2)
    motor.setMotorModel(0,0,0,0)

    #robot location initially
    print('Robot 1st location: [X:{}, Y:{}]'.format(r_locationInitial.getX(), r_locationInitial.getY()))
    #person location initially
    print('Person: [X:{}, Y:{}]'.format(p_location.getX(), p_location.getY()))
    time.sleep(10)
    r_locationCurrent = settings.collector.getRobotLocation()
    print('Robot 2nd location: [X: {}, Y:{}]'.format(r_locationCurrent.getX(), r_locationCurrent.getY()))
    
    r_vector = Vector(r_locationCurrent, r_locationInitial)
    r_p_vector = Vector(p_location, r_locationCurrent)
    angle = angleBetweenVectors(r_vector, r_p_vector)
    #calibration is required 
    rotate(angle, r_locationCurrent.getY(), p_location.getY())
    rotate(angle, r_locationCurrent.getY(), p_location.getY())

    while(not check_approach(10)):
        motor.setMotorModel(1000,1000,1000,1000)
        time.sleep(0.3)
    motor.setMotorModel(0,0,0,0)
    """

def main():
    movement()


if __name__ == '_main_':
    main()