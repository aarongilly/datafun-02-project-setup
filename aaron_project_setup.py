"""
Module: aaron_project_setup

Purpose: Provide functions to script project folders (and domonstrate basic Python coding skills).

Description: This module provides functions for creating a series of project folders.

Author: Aaron Gillespie
Drived from Work By: Denise Case
"""

#####################################
# Import Modules at the Top
#####################################

# Import moduldes from standand library
import pathlib
from time import sleep

# Import local modules
import utils_aaron

#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    # Some bonus error handling
    if not isinstance(start_year, int) or not isinstance(end_year, int):
        print("You passsed a non-integer to the create_folders_for_range function. Returning nothing") # logging a warning, I'll wade do real exceptions someday soon
        return None
    
    # In case range was passed in backwards
    if start_year > end_year:
        temp = start_year
        start_year = end_year
        end_year = temp

    # Handle the happy case
    for i in range(start_year, end_year + 1):
        data_path.joinpath(str(i)).mkdir(exist_ok=True) # assuming I'm supposed to make the folders inside the `data` directory as part of this assignment
  
#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, to_lowercase=False, remove_spaces=False) -> None:
    '''
    Create folders from a list of strings.
    
    Arguments:
    folder_list -- A list of strings containing names of folders to be created
    to_lowercase -- whether or not the file names should be force to lowercase
    remove_spaces -- whether or not the file names should have spaces replaced with underscores
    '''

    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_from_list folder_list={folder_list}, to_lowercase={to_lowercase}, remove_spaces={remove_spaces}")

    if to_lowercase:
        folder_list = [name.lower() for name in folder_list]
    
    if remove_spaces:
        folder_list = [name.replace(" ","_") for name in folder_list]

    for name in folder_list:
        data_path.joinpath(str(name)).mkdir(exist_ok=True) # assuming I'm supposed to make the folders inside the `data` directory as part of this assignment
  
#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    '''
    Create folders from a list of strings with a supplied prefix.
    
    Arguments:
    folder_list -- A list of strings containing names of folders to be created
    prefix -- the desired prefix 
    '''

    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_prefixed_folders folder_list={folder_list}, prefix={prefix}")

    # Creating a new list concatenating the passed-in list with the passed-in prefix.
    modified_list = [prefix + name for name in folder_list]
    # Passings this to the function I already wrote
    create_folders_from_list(modified_list) # DRY

#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
    '''
    Creates folders at a pace according to the supplied duration in seconds.

    Arguments:
    duration_seconds -- Number of seconds to wait between folder creation
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_periodically duration_seconds={duration_seconds}")

    number_of_folders_to_create = 3

    i = 1
    while i <= number_of_folders_to_create:
        data_path.joinpath(f"Periodic Folder {str(i)}").mkdir(exist_ok=True) # assuming I'm supposed to make the folders inside the `data` directory as part of this assignment
        i += 1
        sleep(duration_seconds)

  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    print(f"Byline: {utils_aaron.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)
    # Doing some bonus error handling stuff.
    create_folders_for_range("Strings","Should Fail")
    create_folders_for_range(start_year=2018, end_year=2013) #flipped around in func

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'myprefix-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 2  # duration in seconds
    create_folders_periodically(duration_secs)

    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    # Uncomment this line after you've added your custom logic
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

#TODO: Run this as a script to test that all functions work as intended.