# Name : AKSHAT GAUR
# Date : 9/17/2023
# I Akshat Gaur have not given or received any unauthorized assistance on this assignment.
# Youtube Link : https://youtu.be/ypLcxbyydzM

def py_file_check():
    """
    Returns boolean true or false depending on whether the assignment is submitted as a single uncompressed .py file.
    """
    fileSubmission = int(input("Is the assignment submitted as a single uncompressed .py file? (1.Yes/2.No): ")) # type conversion to int
    return fileSubmission == 1

def student_name_date_check():
    """
    Returns boolean true or false depending on whether the assignment includes the student's name and date.
    """
    studentInfo = int(input("Does the assignment include the student's name and date? (1.Yes/2.No): ")) # type conversion to int
    return studentInfo == 1

def honor_statement_check():
    """
    Returns boolean true or false depending on whether the assignment includes the honor statement.
    """
    honorStatement = int(input("Does the assignment include the honor statement? (1.Yes/2.No): ")) # type conversion to int
    return honorStatement == 1

def youtube_link_check():
    """
    Returns boolean true or false depending on whether the assignment includes a link to a 3-minute YouTube video.
    """
    youtubeLink = int(input("Does the assignment include a link to an unlisted 3-minute YouTube video and answers all the assigned questions? (1.Yes/2.No) ")) # type conversion to int
    return youtubeLink == 1

def evaluation():
    """
    Evaluates the correctness, elegance, hygiene of the code and quality of disscusion in the video.
    Returns integer marks out of 40 after total evaluation.
    """
    correctness = int(input("Out of 10 points, how would you evaluate the correctness of the code? (0-10): "))
    elegance = int(input("Out of 10 points, how would you evaluate the elegance of the code (algorithm efficiency)? (0-10): "))
    hygiene = int(input("Out of 10 points, how would you evaluate the code hygiene (whitespaces, docstrings)? (0-10): "))
    quality = int(input("Out of 10 points, how would you evaluate the quality of the discussion in youtube video? (0-10): "))

    # using min function incase the user enters a value more than 10
    totalEvaluation = min(correctness, 10) + min(elegance, 10) + min(hygiene, 10) + min(quality, 10) 
    return totalEvaluation # sum of all the points returned
    
def calculate_late_penalty():
    """
    Calculates the late submission penalty.
    Returns float penalty based on the number of hours the assignment was late.
    """
    penalty = 0.0 # assigning initial penalty value
    lateCheck = int(input("Was the assignment late? (1.Yes/2.No)"))
    if(lateCheck == 1): # only if the assignment was submitted late
        hours = int(input("How many hours late is the assignment? "))
        hours = min(hours,100) # max marks lost will be 100%
        penalty = hours * 0.01 # for each hour 1% is deducted
    return penalty # returning penalty value based on whether or not the assignment was late

def compute_grade():
    """
    Calculates the final grade for an assignment based on specified criteria.
    Returns float final grade for the assignment, ranging from 0 to 40.
    """
    grade = 0                         # initial grade value
    if not py_file_check():           # using helper function
        return 0                      # if file is incorrect, the grade is 0
    if not student_name_date_check(): # using another helper function
        return 0                      # if name and date not present, the grade is 0
    if not honor_statement_check():   # using another helper function
        return 0                      # if honor statement not present, the grade is 0
    if not youtube_link_check():      # using another helper function
        return 0                      # if unlisted youtube link is not present, the grade is 0
    
    grade = evaluation()                                   # calling the evaluation function to get the marks out of 40
    finalGrade = grade -(calculate_late_penalty() * grade) # subtracting the late penalty marks(if any) and computing final grade
    return finalGrade                                      # returns finalgrade obtained

finalGrade = compute_grade()                                     # calling the compute_grade function to get the final grade
print(f"The final grade for the assignment is: {finalGrade}")    # Printing the final grade of the student
