# Name: Akshat Gaur
# Student ID: 2176685
# Date : 11/21/2023
# I Akshat Gaur have not given or received any unauthorized assistance on this assignment.
# Youtube Link : https://youtu.be/6rRpeleaL18

import math

class Planet:
    """
    Initializes radius and year length
    Calculates position of a planet on a certain day
    """

    def __init__(self,radius,year):
        self.radius = radius
        self.year = year
    def position(self,day):
        """
        Calculates angle on a specific day
        Returns x and y coordinates on that day using trignometry
        """
        angle = 2 * math.pi * day / self.year           # Calculate the angle in radians

        x = self.radius * math.cos(angle)               # Calculate x coordinate using trigonometry
        y = self.radius * math.sin(angle)               # Calculate y coordinate using trigonometry

        return x, y

def distance(planet1,planet2,day):
    """
    Calls the position function to get the coordinates of the required planets
    Calculates distance using Euclideans Distance
    Returns distance
    """
    x1, y1 = planet1.position(day)                      # Get position of the planet 1 on the given day
    x2, y2 = planet2.position(day)                      # Get position of the planet 2 on the given day

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)   # Computing Euclidean's distance

    return distance

def main():
    """
    Calls various functions to calculate position and distance
    """
    # Creating instances of all planets
    mercury = Planet(3.5, 88)
    venus = Planet(6.7, 225)
    earth = Planet(9.3, 365)
    mars = Planet(14.2, 687)
    jupiter = Planet( 48.4, 4333)
    saturn = Planet(88.9, 10759)
    uranus = Planet(179, 30687)
    neptune = Planet(288, 60190)

    # Case 1: Calculating position of mercury on various days
    days = [0,22,365,440,33,50]
    for d in days:
        pos = mercury.position(d)
        pos3 = earth.position(d)
        print(f"\nPosition of Mercury after {d} days: {pos}")
        print(f"Position of Earth after {d} days: {pos3}")

    # Case 2: Calculating distance between two planets
    p1= "Earth"
    p2= "Mars"
    day = 732
    dist = distance(earth,mars,day)
    print(f"\nDistance between {p1} and {p2} on day {day} : {dist}\n")

if __name__ == "__main__":
    main()
