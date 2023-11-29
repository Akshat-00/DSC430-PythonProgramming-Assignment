# Name: Akshat Gaur
# Student ID: 2176685
# Date :10/03/2023
# I Akshat Gaur have not given or received any unauthorized assistance on this assignment.
# Youtube Link : https://youtu.be/JrXKcHuJGgI

def main():
    '''
    Calls get_input to get input from the user
    Calls number_determination to check which category does the number lie
    Prints the result accordingly
    '''
    while True:
        try:                   # exception to catch Value error
            num = get_input()  # calling the get_input function
            if num <= 0:       # checking if the user has entered a negative number or 0
                print("Please enter a positive integer.")
                continue
            result = number_determination(num)         # calls the number_determination function
            print(f"{num} is a {result}.")             # displaying the result
        except ValueError:
            print("Exiting the program")
            break                                      # if the user has entered a non integer

def get_input():
    '''
    Asks the user to input a positive integer or quit.
    Returns the integer to main function
    '''
    num = int(input("Enter a positive integer (or any non-integer to exit): "))
    return num

def number_determination(num):
    '''
    Calls the check_happy function to check if the number is happy or not
    Calls the check_prime function to check if the number is prime or not
    Returns the appropriate string accordingly
    '''
    if check_happy(num):                # calls check_happy function
        if check_prime(num):            # calls check_prime function
            return "Happy Prime"        # If both the functions return true
        else:
            return "Happy Non-Prime"    # If only check_happy returns true
    else:
        if check_prime(num):
            return "Sad Prime"          # If only check_prime returns true 
        else:
            return "Sad Non-Prime"      # If none of the functions return true
        
def check_happy(num):
    '''
    To check if a given number is happy or not
    Keeps adding sum of squares of the digits till the sum = 1(True) 
    or The list has a duplicate sum value(False)
    '''
    lst=[]                          # initializing an empty list
    while num !=1:                  # will run the loop till num = 1
        sum = 0                     # initializing sum to 0
        lst.append(num)             # Appending num to list
        while num > 0:             
            rem = num%10
            sum = sum + (rem**2)    # sum of squares calculation
            num = num//10
        num = sum                   # assigning the sum of squares to num
        if(num in lst):             # checking if the sum is already present in the list or not(checking if the sequence repeats)
            return False            # Returns false i.e. not a happy number
    return True                     # Returns true i.e. a happy number
  
def check_prime(num):
    '''
    To check if a given number is prime or not
    Returns true or false accordingly
    '''
    if num <= 1:                    # 1 or below not prime
        return False
    else:
        for i in range(2,num):      # Runs a loop from 2 to num
            if(num % i) == 0:       # Checks if the number has a factor
                return False        # Not prime if there is a factor                                 
    return True                     # Prime if there is no factor
        
main()