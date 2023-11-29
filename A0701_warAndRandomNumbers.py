# Name: Akshat Gaur
# Student ID: 2176685
# Date : 11/03/2023
# I Akshat Gaur have not given or received any unauthorized assistance on this assignment.
# Youtube Link : https://youtu.be/KaNkrcoM2CE

from statistics import mean

class WarAndPeacePseudoRandomNumberGenerator:
    def __init__(self,seed=1000,step = 100):

        self.seed = seed
        self.step = step
        self.fileName = "war-and-peace.txt"
        with open(self.fileName, 'r') as file:  # Opening the file for reading
            self.content = file.read()          # Storing the file in content
        self.content_length = len(self.content) # Calculating the length of the file
        self.content_pos = 0                    # Setting the cursor value to
        
    def readCharacters(self):
        """
        Reads character 1 & 2 based on seed value and step
        Returns char 1 & 2
        """
        char1 = self.content[self.seed]          # Read char 1 at the seed position in the content
        self.content_pos = (self.content_pos + self.seed) % self.content_length  # Update position based on the seed and content length
        char2 = self.content[self.content_pos]   # Read char 2 at the updated position in the content
        self.content_pos = (self.content_pos + self.step) % self.content_length  # Update position again based on the step and content length
        return char1, char2
    

    def generateList(self):
        """
        Compares if char 2 is an empty string
        Compares both the characters and appends the result in binary list accoringly
        Returns binary list after finding all 32 pairs
        """
        binarylist = []
        pairs_generated = 0
        while pairs_generated < 32:                         # Generating 32 proper pairs
            char1, char2 = self.readCharacters()
            if char1 == char2:
                self.step += 100                            # Increase the step by 100 places
                char2 = self.content[self.content_pos]      # Read char2 again with the updated step
                self.content_pos = (self.content_pos + self.step) % self.content_length 
                continue
            if ord(char1) > ord(char2):                     # If ascii value of char1 is more
                binarylist.append(1)
            else:                                           # If ascii value of char2 is more
                binarylist.append(0)                       

            pairs_generated += 1                            # Increment pair once found
            self.step += 100                                # Incrementing step and seed to read the next pair
            self.seed = (self.seed + self.step) % self.content_length
        return binarylist

    def random(self):
        """
        Multiplies each value of binary list with a probablity value which keeps on decreasing
        Decreasing happens by multiplying the denominator by 2 
        Returns all the added value as one random number
        """
        randomNumber = 0.0
        probDenom= 2
        binaryList = self.generateList()
        for i in range (len(binaryList)):
            randomNumber = randomNumber + binaryList[i] * (1/probDenom)    # Multiplying the binary with probablity and computing
            probDenom = probDenom * 2
        return randomNumber
    
    def closeFile(self):
        """
        Closing the file opened
        """
        pass 
    
def main():
    """
    Calls WarWarAndPeacePseudoRandomNumberGenerator class
    Calls random fn to generate 10000 numbers from the text file
    Calculates the mean, max, min from the list of generated random numbers
    """
    randomNumberList = []
    n = 10000
    prng2 = WarAndPeacePseudoRandomNumberGenerator(12345)   # Creates a new instance of class and assigns it to prng2 with seed
    random = prng2.random()                                 # Random number generation
    prng2.closeFile()                                       # Closing the file

    prng = WarAndPeacePseudoRandomNumberGenerator()         # Creates a new instance of class and assigns it to prng without seed
    for i in range(n):                                      # Generating 10000 random numbers
        r = prng.random()                                   # Calls the random function of the class
        randomNumberList.append(r)                          # Appending the random number obtained to the list
    prng.closeFile()                                        # Calling the close file function of the class

    mean_value = mean(randomNumberList)                     
    minimum = min(randomNumberList)
    maximum = max(randomNumberList)

    print("Random numbers generated with seed 12345: {}".format(random))
    print("\nAfter generating",n ,"random numbers")
    print("\nMean: {} ".format(mean_value))
    print("\nMinimum: {} ".format(minimum))
    print("\nMaximum: {} ".format(maximum))
    print("\nList of first 5 random numbers",randomNumberList[:5],"\n") # Displaying first 10 numbers out of 10000

if __name__ == '__main__':
    main()


