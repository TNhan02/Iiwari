import botVector

filtered_value = 0.0

def exponential_filter(incoming_value):
    global filtered_value
    if(incoming_value != None):
        filtered_value = 0.5 * incoming_value + (1 - 0.5) * filtered_value

    return filtered_value

class Collector():
    personLocation: botVector.Point = botVector.Point()
    robotLocation: botVector.Point = botVector.Point()
    initialRobotLocation: botVector.Point = None

    def __init__(self) -> None:
        self.personLocation = botVector.Point()
        self.robotLocation = botVector.Point()
        self.initialRobotLocation = botVector.Point()

    def addPersonLocation(self, personLocation: botVector.Point):
        self.personLocation = personLocation

    def addRobotLocation(self, robotLocation: botVector.Point):
        if(self.initialRobotLocation==botVector.Point(0,0)):
            self.initialRobotLocation = robotLocation
        self.robotLocation = robotLocation
    
    def clearInitialLocation(self):
        self.initialRobotLocation = None

    
    def clear(self):
        self.personLocation = None
        self.robotLocation = None
        self.initialRobotLocation = None 



    def getPersonLocation(self):
        print("Person: {}, {}".format(self.personLocation.getX(), self.personLocation.getY()))
        return botVector.Point(self.personLocation.getX(), self.personLocation.getY())
    
    def getRobotLocation(self):
        print("Robot: {}, {}".format(self.robotLocation.getX(), self.robotLocation.getY()))
        return botVector.Point(self.robotLocation.getX(), self.robotLocation.getY())
    
    def getInitRobotLocation(self):
        print("Initial robot: {}, {}".format(self.initialRobotLocation.getX(), self.initialRobotLocation.getY()))
        return botVector.Point(self.initialRobotLocation.getX(), self.initialRobotLocation.getY())
    

global collector, is_button_pressed
collector = Collector()
is_button_pressed = False