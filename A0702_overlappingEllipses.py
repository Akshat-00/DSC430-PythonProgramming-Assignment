# Name: Akshat Gaur
# Student ID: 2176685
# Date : 11/03/2023
# I Akshat Gaur have not given or received any unauthorized assistance on this assignment.
# Youtube Link : https://youtu.be/IZMlQ1bOiWA

import math
import warAndRandomNumbers as randomNum

class Point:
    """
    Class to initialize x and y point of a coordinate
    """
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
class Ellipse(Point):
    """
    Class to initialize two points and the width of the ellipse
    """
    def __init__(self, p1, p2, width=4):
        self.p1 = p1
        self.p2 = p2
        self.width = width

class EllipseOverlapCalculator(randomNum.WarAndPeacePseudoRandomNumberGenerator):
    """
    Subclass extending WarAndPeacePseudoRandomGenerator
    """
    def __init__(self, seed=1000, l=0, r=0, t=0, b=0):
        super().__init__(seed)
        self.l = l
        self.r = r
        self.t = t
        self.b = b

    def generateRandomPoints(self, numPoints):
        """
        Generate random points with the help of random function from War and Peace and store it in a list
        Returns list of tuples
        """
        random_points = []

        for i in range(numPoints):
            x = self.random() * (self.r - self.l) + self.l      # X coordinate generation
            y = self.random() * (self.b - self.t) + self.t      # Y coordinate generation
            random_points.append((x, y))

        return random_points

    def isInsideEllipse(self, x, y, fp1, fp2, w):
        """
        Checks if a point(x,y) is present inside an ellipse
        Returns True or False based on comparing the distance and width
        """
        d1 = math.sqrt((x - fp1.x) ** 2 + (y - fp1.y) ** 2)     # Euclidean's algo to calculate distance b/w two points
        d2 = math.sqrt((x - fp2.x) ** 2 + (y - fp2.y) ** 2)

        return d1+d2 <= w                                       # Comparing with width

def computeOverlapOfEllipses(e1, e2):
    """
    Creates a box surrounding the ellipses.
    Checks if the random numbers generated is present in both the ellipses(i.e. overlapping)
    Computes the overlap area 
    Returns the area
    """
    # All four corners of the box
    l = min(e1.p1.x, e1.p2.x, e2.p1.x, e2.p2.x) - e1.width / 2
    r = max(e1.p1.x, e1.p2.x, e2.p1.x, e2.p2.x) + e1.width / 2
    t = min(e1.p1.y, e1.p2.y, e2.p1.y, e2.p2.y) - e1.width / 2
    b = max(e1.p1.y, e1.p2.y, e2.p1.y, e2.p2.y) + e1.width / 2

    random_gen = EllipseOverlapCalculator(seed=1000, l=l, r=r, t=t, b=b) # Creating a new instance of a class EllipseOverlapCalculator
    randomPointList = random_gen.generateRandomPoints(10000)             # Generating 10000 points
    length = len(randomPointList)

    overlapPointCount = 0
    for point in randomPointList:
        # If the random numbers generated is present in both the ellipses(i.e. overlapping)
        if (random_gen.isInsideEllipse(point[0], point[1], e1.p1, e1.p2, e1.width) 
        and random_gen.isInsideEllipse(point[0], point[1], e2.p1, e2.p2, e2.width)):
            overlapPointCount +=1
            
    boxArea = (r - l) * (b - t)                                         # Area of the box surrounding the ellipse
    overlapArea = (overlapPointCount / length) * boxArea                # Area of overlapping parts of the ellipse

    return overlapArea

def main():
    """
    Prints the result based on different scenarios
    Assigns the focal points, width of the ellipse
    """
    print("Case 1: Simple case for two overlapping circles\n")
    p1 = Point(0, 0)
    p2 = Point(0, 0)
    e1 = Ellipse(p1, p2, 2)  
    e2 = Ellipse(p1, p2, 2)
    overlap = computeOverlapOfEllipses(e1, e2)
    print("Overlapping area for two circles at the origin(approx): ", overlap)

    print("\n\nCase 2: Case for two overlapping ellipses\n")
    p1 = Point(2, 2)
    p2 = Point(2, 6)
    e1 = Ellipse(p1, p2, 5)
    p3 = Point(4, 4)
    p4 = Point(4, 9)
    e2 = Ellipse(p3, p4, 10)
    overlap = computeOverlapOfEllipses(e1, e2)
    print("Overlapping Area for Ellipses(approx):", overlap)

    print("\n\nCase 3: Case for two non-overlapping ellipses\n")
    p1 = Point(2, 0)
    p2 = Point(2, 5)
    e1 = Ellipse(p1, p2, 4)
    p3 = Point(8, 2)
    p4 = Point(8, 7)
    e2 = Ellipse(p3, p4, 3)
    overlap = computeOverlapOfEllipses(e1, e2)
    print("Overlapping Area:", overlap)

if __name__ == '__main__':
    main()