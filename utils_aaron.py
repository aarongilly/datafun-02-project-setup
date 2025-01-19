"""
Module: utils_aaron

Purpose: Reusable Module for My Analytics Projects

Description: This module implements some basic functionality demsontrating the completion of the 
the first "Engage" assigment. In theory this sort of module would be reusable. Thus far I doubt
anything in here is particularly worth reusing yet, although syntax references are always nice.

Author: Aaron Gillespie, derived from:
Original Author: Denise Case
"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
is_strong_in_python: bool = False
#has_international_clients: bool = True

# declare an integer variable 
years_old: int = 36
#years_in_operation: int = 10

# declare a floating point variable
current_weight_lbs: float = 224.5
#average_client_satisfaction: float = 4.7

# declare a list of strings
skills_in_work: list = ["Python","3D Printing & Design", "Microcontroller stuff"]
#skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

# declare a list of numbers so we can illustrate statistics skills
prev_three_days_spend: list = [0.0, 30.34, 12.58]
#client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

# Calculate basic statistics using built-in Python functions and the statistics module
min_score: float = min(prev_three_days_spend)  
max_score: float = max(prev_three_days_spend)  
mean_score: float = statistics.mean(prev_three_days_spend)  
stdev_score: float = statistics.stdev(prev_three_days_spend)

# Use a Python formatted string (f-string) to show information
byline: str = f"""
---------------------------------------------------------
Aaron Analytics: The More Fun AA
---------------------------------------------------------
Is Strong with Python:      {is_strong_in_python}
Years in Operation:         {years_old}
Skills In Development:      {skills_in_work}
Previous 3 Days Spend:      {prev_three_days_spend}
Minimum Money Spent:        {min_score}
Maximum Money Spent:        {max_score}
Mean Money Spent:           {mean_score:.2f}
Standard Deviation of Money Spent: {stdev_score:.2f}
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.
