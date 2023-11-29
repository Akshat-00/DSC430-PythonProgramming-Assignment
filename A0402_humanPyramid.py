# Name: Akshat Gaur
# Student ID: 2176685
# Date :10/12/2023
# I Akshat Gaur have not given or received any unauthorized assistance on this assignment.
# Youtube Link : https://youtu.be/SPWV1oS8YKE

def humanPyramid(row, column):
    '''
    This function takes as input the row and column number of a person in a human pyramid
    Calculates the total weight on that persons back
    Returns the total weight
    '''
    if row < 0 or column < 0 or column > row:                   # No person exists at that position
        return 0
    if row == 0 and column == 0:                                # For top most person
        return 0
    elif row > 0 and column == 0:                               # For leftmost person in any row (except the top row)
        return (128 + humanPyramid(row - 1, column)) / 2        # Half of right parent and accumulated weight on it
    elif row > 0 and column == row:                             # For rightmost person in any row (except the top row)
        return (128 + humanPyramid(row - 1, column - 1)) / 2    # Half of left parent and accumulated weight on it
    else:                                                       # Every person other than rightmost or leftmost
        # Half of left parent,half of right parent and the accumulated weight on them
        return (128 + 128 + humanPyramid(row - 1, column - 1) + humanPyramid(row - 1, column)) / 2
   
row = int(input("Enter the row number: "))                      # Ask the user to enter row number
column = int(input("Enter the column number: "))                # Ask the user to enter column number
total_weight = humanPyramid(row, column)                        # Call recursive function with rows and columns as parameters
print("Total weight on the person\'s back at position ({}, {}) is {}".format(row, column, total_weight))