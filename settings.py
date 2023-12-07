import botVector

filtered_value = 0.0
is_button_pressed

def init():
    global is_button_pressed
    is_button_pressed = False

def exponential_filter(incoming_value):
    global filtered_value
    if(incoming_value != None):
        filtered_value = 0.5 * incoming_value + (1 - 0.5) * filtered_value

    return filtered_value

class Collector():
    def __init__(self) -> None:
        self.personLocation = botVector.Point()
        self.robotLocation = botVector.Point()
        self.initialRobotLocation = None

    def addPersonLocation(self, personLocation: botVector.Point):
        self.personLocation = personLocation

    def addRobotLocation(self, robotLocation: botVector.Point):
        if(self.initialRobotLocation==None):
            self.initialRobotLocation = robotLocation
        self.robotLocation = robotLocation
    
    def clearInitialLocation(self):
        self.initialRobotLocation = None

    
    def clear(self):
        self.personLocation = None
        self.robotLocation = None
        self.initialRobotLocation = None 



    def getPersonLocation(self):
        return botVector.Point(self.personLocation.getX(), self.personLocation.getY())
    
    def getRobotLocation(self):
        return botVector.Point(self.robotLocation.getX(), self.robotLocation.getY())
    
    def getInitRobotLocation(self):
        return botVector.Point(self.initialRobotLocation.getX(), self.initialRobotLocation.getY())
    

global collector, is_button_pressed
collector = Collector()
is_button_pressed = False