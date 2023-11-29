# Name: Akshat Gaur
# Student ID: 2176685
# Date : 10/03/2023
# I Akshat Gaur have not given or received any unauthorized assistance on this assignment.
# Youtube Link : https://youtu.be/whxc80PawlY

def goldbach_conjecture():
    '''
    Runs a nested loop to find number pairs that sum upto the current number
    Calls check_prime to check whether the numbers found are prime or not and displays the result
    '''
    limit = 100                                 # Testing Goldbach's Conjecture till 100
    for n in range(4, limit + 1, 2):            # for loop running from 4 to 100 with a step of 2
        for primeNum1 in range(2, n // 2 + 1):  # iterates through potential values of the first prime in the range from 2 up to half of the current even number
            primeNum2 = n - primeNum1                             # second prime will be the remaining part
            if check_prime(primeNum1) and check_prime(primeNum2): # checking if the numbers are prime by calling the check_prime function
                print(f"{n} = {primeNum1} + {primeNum2}")         # displaying the result
                break

def check_prime(num):
    '''
    To check if a given number is prime or not
    Returns true or false accordingly
    '''
    if num <= 1:                    # 1 or below not prime
        return False
    else:
        for i in range(2,num//2):      # Runs a loop from 2 to num
            if(num % i) == 0:       # Checks if the number has a factor
                return False        # Not prime if there is a factor                                 
    return True                     # Prime if there is no factor

goldbach_conjecture()