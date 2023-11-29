# Name : AKSHAT GAUR
# Date : 9/17/2023
# I Akshat Gaur have not given or received any unauthorized assistance on this assignment.
# Youtube Link : https://youtu.be/ypLcxbyydzM

def coprime_test_loop():
    """
    Continuously prompt the user to input pairs of numbers and check if they are coprime.
    The loop continues until the user enters 0 to exit the program.
    Prints whether the numbers are coprime or not
    """
    while True: # loop runs until user enters 0

        a = int(input("Enter 0 if you wish to exit or \nEnter the First number: ")) # taking the first number or 0 to exit
        if a == 0: # Checking if the user has entered 0 to exit
            print("Exiting Program Thankyou.")
            break # Causes the loop to break
        b = int(input("Enter the Second Number: ")) #taking the second number
        
        if coprime(a, b): # Calling coprime function and passing the two numbers a,b as parameters
            print(f"{a} and {b} are coprime.")
        else:
            print(f"{a} and {b} are not coprime.")


def coprime(a, b):
    """
    Check if two numbers a and b are coprime (i.e., their greatest common divisor is 1).
    Arguments:
        a (int): The first number.
        b (int): The second number.
    Returns boolean true if the number are coprime, otherwise false
    """
    while b: # Runs until b becomes 0
        tmp = b
        b = a % b # storing the remainder in b
        a = tmp # storing b's previous value
    return a == 1 # Final value of a is gcd and is compared with 1 to return true or false
    
coprime_test_loop() # Run coprime_test_loop