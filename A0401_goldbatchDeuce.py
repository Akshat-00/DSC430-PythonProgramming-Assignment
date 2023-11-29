# Name: Akshat Gaur
# Student ID: 2176685
# Date :10/12/2023
# I Akshat Gaur have not given or received any unauthorized assistance on this assignment.
# Youtube Link : https://youtu.be/m0azZJOZ8Vw


import random                                       # importing random package

def generate_random_list(length):
    """
    Parameter : length for the list
    Responsible for calculating random list of integers using randint
    Returns the list
    """
    randomList=[]                                   # Initializing an empty list
    for i in range (length):                    
        randomList.append(random.randint(0,100))    # Appending random integers between 0 and 100 in the list
    return randomList

def find_pair(sortedList, targetSum):
    """
    Parameters : Sorted list and the target sum
    Responsible for finding pairs of numbers whose sum is the desired sum
    Calls binary search function to search num 2
    Returns both numbers if num 2 is found else returns None
    """
    for i in range (0,len(sortedList)):                           # Runs through the sorted list. Complexity:(O(n))
        n2 = targetSum - sortedList[i]                            # Initializing n2 as the difference of target sum and the current num
        result = binarySearch(sortedList,0,len(sortedList)-1,n2)  # Calling binarySearch function to search number 2 . Complexity:(O(n))
        if(result == False):
            continue                                              # If the result of binarySearch is false, continue the loop
        else:                                                     # If the result of binarySearch is true
            n1=sortedList[i]                                      # Storing the current num as n1       
            return n1,n2                                          # Returns the pair
    return None,None

def binarySearch(list, start, end, x):
    """
    Parameters : list,start(starting point),end(ending point),element to be searched
    Applies binary search on the list
    Returns true or false on whether the element is found or not
    """
    while start <= end:                         # runs till the start is less than or equal to end
 
        mid = start + (end - start) // 2        # Finding the middle element between left and right
         
        if list[mid] == x:                      # Check if x(desired element) is present at mid position
            return True
 
        elif list[mid] < x:                     # If element at mid is less than x
            start = mid + 1                     # Moving the start index after mid (Ignoring left half)
 
        else:                                   # If element at mid is more than x
            end = mid - 1                       # Moving the end index before mid (Ignoring right half)
 
    return False                                # If the element is not present at all

def main():
    """
    Takes the length of the list and target sum from the user.
    Calls the generate_random_list function to generate random numbers and store in a list
    Sorts the list using inbuilt function sort and displays the sorted list
    Calls the find_pair function to find the pairs whose sum is equivalent to the target sum
    Displays the final output 
    """
    length = int(input("Enter the length of the list: "))           # User input for length of list
    randomList = generate_random_list(length)                       # To generate random numbers list and store in randomList
    randomList.sort()                                               # Sort the list in O(n*log(n)) time
    print("The generated random sorted list is : ", randomList)     # Displaying sorted list

    targetSum = int(input("Enter the target sum: "))  # User input for target sum
    pair1,pair2 = find_pair(randomList, targetSum)    # Calling findpair to to find the pairs whose sum is equivalent to the target sum

    if pair1:                                                       # If the pairs are found
        print(f"Pair found: {pair1} + {pair2} = {targetSum}") 
    else:                                                           # If the pairs are not found
        print("No pair found for the given sum.")


main()                                                              # Calling the main function to start the program