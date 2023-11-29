# Name: Akshat Gaur
# Student ID: 2176685
# Date : 9/24/2023
# I Akshat Gaur have not given or received any unauthorized assistance on this assignment.
# Youtube Link : https://youtu.be/da0wz3iP82g

def main():
    '''
    Responsible for controlling the entire program.
    Calls greet,get_input,stem_leaf_design and print_stem_leaf_plot to perform various functions.
    '''
    greet()                         # calling greet function
    while True:                     # runs till user enters q for quitting
        choice = get_input()        # calling the getInput function
        if choice in ['1','2','3']: # if user has entered a correct file number between 1,2,3
            stemLeafDesign=stem_leaf_design(choice) # calling stem_leaf_design function with choice as the parameter
        elif choice == 'q':         # if user has entered q to quit
            break                   # break to exit
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 'q' to quit.") # if user has entered anything other than 1,2,3 or quit
            continue                                                       # skips and continues the loop
        
        print_stem_leaf_plot(stemLeafDesign) # calls the print_stem_leaf_plot function

def greet():
    '''
    Greets the user.
    '''
    print("\nHello User.")
    print("This is a Stem and Leaf plotting program.")

def get_input():
    '''
    Asks the user to input a file number or quit.
    Returns the choice to main function
    '''
    choice = input("\nEnter 1, 2, or 3 to choose a file (or 'q' to quit): ") # asking the user to choose a file or quit
    return choice

def stem_leaf_design(choice):
    '''
    Calls the read_file function to attain a list of data values
    Converts each value to a key value pair(stem leaf) and stores it in a dictionary
    Returns the dictionary to main
    '''
    fileName = f"StemAndLeaf{choice}.txt" # assigning the filename to their corresponding txt file and storing the name
    stemLeafDesignDict = {}                   # creating an empty dictionary
    data = read_file(fileName)            # calling the read_file function with filename as the parameter

    for value in data:                    # iterating through the list
        stem = str(value // 10)           # stem stores the quotient
        leaf = str(value % 10)            # leaf stores the remainder
        
        if stem not in stemLeafDesignDict:    # checking if stem(key) already exists in the dictionary
            stemLeafDesignDict[stem] = []     # adding the stem(key) to the dictionary if key is not present

        stemLeafDesignDict[stem].append(leaf) # appending the leaf(value) to the list of values for the corresponding stem(key)
    return stemLeafDesignDict

def read_file(fileName):
    '''
    Reads the file corresponding to the fileName parameter.
    Stores the values of the file in a list.
    Returns the list of values to stem_leaf_design
    '''
    dataList = []                              # creating an empty list
    try:                                       # try block for exceptional handling
        file = open(fileName,'r')              # opens the particular file in reading mode
        for line in file:                      # to itererate through each line of the file
            value = int(line.strip())          # removing whitespaces and storing each line as an integer in value
            dataList.append(value)             # appending the value obtained into dataList
        file.close()                           # closes the file after the desired operation is done
    except FileNotFoundError:                  # except block to catch a file not found exception
        print(f"File '{fileName}' not found.") # prints the statement to handle the exception
    return dataList                 

def print_stem_leaf_plot(stemLeafDesign):
    '''
    Takes a dictionary as the parameter
    Sorts the stems and leaf and combines them(string converted) to store each pair in the list using join
    Prints each pair in a seperate line.

    '''
    print("\nThe stem and leaf plot for the chosen file is: \n")

    sorted_stems = sorted(stemLeafDesign.keys(),key=int)     # sorting the stems(keys) in the dictionary using sorted
# iteration through every key in the sorted dictionary(line 86)
    stem_and_leaf_lines = [
        f"{stem}| {' '.join(map(str,sorted(stemLeafDesign[stem])))}" # conversion of sorted leaves to string using map & joining them with strings using join
        for stem in sorted_stems # iterates through every key in the dictionary
    ]
    for i in stem_and_leaf_lines:                    # iterates through the list storing stem leaf pair
        print(i)                                     # prints the stem-and-leaf plot

main() # Calling the main function to start the program