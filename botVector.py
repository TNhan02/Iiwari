import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def getX(self):
        return self.x
    
    def getX(self):
        return self.y
    


class Vector():
    def __init__(self, finalPoint: Point, initialPoint: Point):
        self.x = finalPoint.getX() - initialPoint.getX()
        self.y = finalPoint.getX() - initialPoint.getX()


    def getX(self):
        return self.x


    def getY(self):
        return self.y
    

    def countMagnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    

def scalarProduct(vector1: Vector, vector2: Vector) -> float:
    return (vector1.getX() * vector2.getX()) + (vector1.getY() * vector2.getY())


def moduleProduct(vector1: Vector, vector2: Vector) -> float:
    return vector1.countMagnitude() * vector2.countMagnitude()


def angleBetweenVectors(vector1: Vector, vector2: Vector):

    """
    Returns a magnitude of an angle between 2 vectors.
    The result is in radians from 0 to pi.
    """

    cos_a = scalarProduct(vector1, vector2) / moduleProduct(vector1, vector2)
    return math.acos(cos_a*180/math.pi)

    