# Name : AKSHAT GAUR
# Date : 10/26/2023
# I Akshat Gaur have not given or received any unauthorized assistance on this assignment.
# Youtube Link : https://youtu.be/6Wy6tDzSuoU

def is_palindrome(date):
    """
    Checks if a given string is Palindrome or not.
    Returns true or false accordingly.
    """
    date = date.replace('/', '')                                    # Replaces / to ensure checking of just numbers
    return date == date[::-1]                                       # Checks if the string is equal to it's reverse or not

def main():
    """
    Runs nested loop through years months and days.
    Calls is_palindrome function to check for palindrome.
    Opens a file and writes the entire list obtained on it.
    """
    palindrome_dates = []                                           # Empty palindrome list

    for year in range(2001, 2100):                                  # Runs from 2001 to 2091
        if(year % 10 < 3):
            for month in range(2,3):                                # Runs only through the second month(21 st Century years)
                for day in range(1, 29):                            # Second month will only have 28 days
                    date_str = f'{day:02d}/{month:02d}/{year:04d}'  # Storing the days month and year as DD/MM/YYYY in date_str
                    if is_palindrome(date_str):                     # Calls is_palindrome
                        palindrome_dates.append(date_str)           # Appends date_str if is_palindrome returns true
    
    f = open("palindrome.txt", "w")                                 # Opens a file to write
    f.write("The palindrome dates of 21st Century are:\n")          
    for p in palindrome_dates:                                      # Runs a loop through the list 
        f.write(p + "\n")                                           # Writes each value of the list in the file
    f.close

main()                                                              # To start the program








