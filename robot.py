#this is the 2nd python script to add robot's algorithm
import time
from settings import person_location, is_button_pressed, robot_location
import run_streams
from botVector import *
from person_stream import *
from Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi.Code.Server.Motor import *
from Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi.Code.Server.Light import *
from Iiwari.Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi.Code.Server.Light import *
from enum import Enum

# this class is used for setting the robot's status when an event occurs
class RobotStatus(Enum):
    IDLE = 1
    DUTY = 2
    LOST = 3

# initialize robot's components
motor = Motor()
status = RobotStatus(1)

# check if robot is near to the person or not
# accept distance is the radius of the area marking the robot has arrived
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
    

def rotate(angle: float, r_locationCurrent: Point, p_location: Point) -> None:
    rotate_angle = 0
    if(r_locationCurrent.getX() >= p_location.getX()):
        rotate_angle = 180-angle
    else:
        rotate_angle = angle
    rotation_time = rotate_angle* (0.88/90)
    if(r_locationCurrent.getY >= p_location.getY()):
        motor.setMotorModel(2000,2000,-2000,-2000)
    else:
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
                p_location = person_location
                r_locationCurrent = robot_location
                p_location = settings.collector.getPersonLocation()
                r_locationCurrent = settings.collector.getRobotLocation()

                r_vector = Vector(r_locationCurrent, r_locationInitial)
                r_p_vector = Vector(p_location, r_locationCurrent)
                angle = angleBetweenVectors(r_vector, r_p_vector)
                #calibration is required 
                rotate(angle, r_locationCurrent, p_location)

                while(not check_approach(2)):
                    motor.setMotorModel(1000,1000,1000,1000)

                motor.destroy()
                status = RobotStatus.IDLE.value
                break