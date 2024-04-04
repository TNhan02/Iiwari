import botVector

filtered_x = 0.0
filtered_y = 0.0

def exponential_filter(incoming_value, coordinate):
    global filtered_x, filtered_y
    if coordinate == 'x':
        if(incoming_value != None):
            filtered_x = 0.7 * incoming_value + (1 - 0.7) * filtered_x
        return filtered_x
    elif coordinate == 'y':
        if(incoming_value != None):
            filtered_y = 0.7 * incoming_value + (1 - 0.7) * filtered_y
        return filtered_y
    

class Collector():
    initialPersonLocation : botVector.Point = botVector.Point()
    personLocation: botVector.Point = botVector.Point()
    robotLocation: botVector.Point = botVector.Point()
    initialRobotLocation: botVector.Point = None

    def __init__(self) -> None:
        self.initialPersonLocation = botVector.Point()
        self.personLocation = botVector.Point()
        self.robotLocation = botVector.Point()
        self.initialRobotLocation = botVector.Point()

    def addPersonLocation(self, personLocation: botVector.Point):
        if(self.initialPersonLocation == botVector.Point(0,0)):
            self.initialPersonLocation = personLocation
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

    def getInitPersonLocation(self):
        print("Initial Person: {}, {}".format(self.initialPersonLocation.getX(), self.initialPersonLocation.getY()))
        return botVector.Point(self.personLocation.getX(), self.personLocation.getY())

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