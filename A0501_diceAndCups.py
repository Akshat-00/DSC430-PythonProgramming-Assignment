# Name: Akshat Gaur
# Student ID: 2176685
# Date : 10/19/2023
# I Akshat Gaur have not given or received any unauthorized assistance on this assignment.
# Youtube Link : https://youtu.be/Tt47PTzoqWE

import random

def main():
    """
    Creates a new instance of all the classes and does a test run.
    """
    sixside = SixSidedDie()                             # Creates a new instance of class SixSidedDie and assigns it to sixside
    sixside.roll()                                      # Calls the roll function of the class
    print("\nRolling a Six Sided Die:")
    print(f"Face value: {sixside.getFaceValue()}")      # Calls getFaceValue to get the generated face value
    print(sixside)
 
    tenside = TenSidedDie()                             # Creates a new instance of class TenSidedDie and assigns it to tenside
    tenside.roll()                                      # Calls the roll function of the class
    print("\nRolling a Ten Sided DIe:")
    print(f"Face value: {tenside.getFaceValue()}")      # Calls getFaceValue from the SixSidedDie class 
    print(tenside)

    twentyside = TwentySidedDie()                       # Creates a new instance of class TwentySidedDie and assigns it to twentyside                      
    twentyside.roll()                                   # Calls the roll function of the class
    print("\nRolling a Twenty Sided Die:")
    print(f"Face value: {twentyside.getFaceValue()}")   # Calls getFaceValue from the SixSidedDie class
    print(twentyside)

    cup = Cup(2, 3, 3)                                  # Creates a new instance of class Cup and assigns it to cup                           
    cup.roll()                                          # Calls roll function of Cup class
    print("\nRolling a Cup:")
    print(f"Sum of face values: {cup.getSum()}")        # Calls the getSum function to get the total number
    print(cup)

class SixSidedDie():                           
    """
    Six-sided dice class. Parent / Superclass
    Includes __init__(), roll(), getFaceValue() and __repr__() methods
    """
    def __init__(self):                             # Called when new instance of class is created                      
        self.face_value = None                      # Initial face value assigned to None

    def roll(self):
        self.face_value = random.randint(1, 6)      # Computing face value by generating random number between 1 & 6

    def getFaceValue(self):                         # Getter function to return the current value on the die
        return self.face_value

    def __repr__(self):                             # Returns the representation of the object as a string
        return f'SixSidedDie({self.face_value})'

class TenSidedDie(SixSidedDie):
    """
    Ten-sided dice class. Child / Subclass. Extends SixSidedDie.
    Includes roll() and __repr__() methods which will overlap the parent class functions
    """
    def roll(self):                                 
        self.face_value = random.randint(1, 10)     # Computing face value by generating random number between 1 & 10

    def __repr__(self):
        return f'TenSidedDie({self.face_value})'    # Returns the representation of the object as a string

class TwentySidedDie(SixSidedDie):
    """
    Twenty-sided dice class. Child / Subclass. Extends SixSidedDie.
    Includes roll() and __repr__() methods which will overlap the parent class methods
    """
    def roll(self):                                 # Computing face value by generating random number between 1 & 20
        self.face_value = random.randint(1, 20)

    def __repr__(self):                             
        return f'TwentySidedDie({self.face_value})' # Returns the representation of the object as a string

class Cup():
    """
    A Class is a separate class that manages and interacts with multiple dice objects.
    Includes __init__(), roll(), getSum() & __repr__()
    """
    # Called when new instance of class is created, By default, the cup will contain one of each type of die.
    def __init__(self, six_sided = 1, ten_sided = 1, twenty_sided = 1): 

        self.dice = []                            # Creating an empty list
        for i in range(six_sided):                # Iterates the number of six sided dice in the cup
            self.dice.append(SixSidedDie())       # New instance of SixSidedDie is created using SixSidedDie(), and added to the dice list.
        for i in range(ten_sided):                # Iterates the number of ten sided dice in the cup
            self.dice.append(TenSidedDie())       # New instance of TenSidedDie is created using TenSidedDie(), and added to the dice list.
        for i in range(twenty_sided):             # Iterates the number of twenty sided dice in the cup
            self.dice.append(TwentySidedDie())    # New instance of TwentySidedDie is created using TwentySidedDie(), and added to the dice list.

    def roll(self):
        for die in self.dice:                                   # Iterates through the dice list
            die.roll()                                          # Calls roll function for each die

    def getSum(self):                                           # Funtion to get the total number from all dice
        return sum(die.getFaceValue() for die in self.dice)     # Calls getFaceValue function for each die and returns the sum

    def __repr__(self):                                         # Returns the representation of the object as a string                                 
        return f'Cup({", ".join(map(repr, self.dice))})'        # This part joins the string representations of each die in the cup.
    
if __name__=="__main__":
    main()
