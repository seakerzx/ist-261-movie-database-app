"""
Program executes here.
"""

import user_interface
import movies

if __name__ == '__main__':
    close_program = False
    user_selection = -1
    
    console_interface = user_interface.ConsoleUI('Title', 'Body')
    
    # Main program loop starts here.
    while close_program == False:
        
        console_interface.update_screen('Main Menu', 'Welcome to the Python Movie Database Manager!')
        console_interface.prompt_options_menu('Add a Movie', 'Update a Movie', 'Search for Movies', 'Import Data from CSV', 'Export Data to CSV', 'Exit Application')

        # TODO: Add try-except to make sure user input is acceptable
        # TODO: Collecting the user input should probably be a function of the ConsoleUI class, look into implementing it there.
        user_selection = int(input())
        
        # TODO: Finish each branch
        # Add a Movie Branch
        if user_selection == 1:
            console_interface.update_screen('Add a Movie', 'Sorry! This feature has not be implemented yet! You will be returned to the main menu.')
            console_interface.prompt_enter_to_continue()
            
        # Update a Movie Branch
        elif user_selection == 2:
            console_interface.update_screen('Update a Movie', 'Sorry! This feature has not be implemented yet! You will be returned to the main menu.')
            console_interface.prompt_enter_to_continue()
            
        # Search for Movies Branch
        elif user_selection == 3:
            console_interface.update_screen('Search for a Movie', 'Sorry! This feature has not be implemented yet! You will be returned to the main menu.')
            console_interface.prompt_enter_to_continue()
            
        # Import Data from CSV Branch
        elif user_selection == 4:
            console_interface.update_screen('Import Data from CSV', 'Sorry! This feature has not be implemented yet! You will be returned to the main menu.')
            console_interface.prompt_enter_to_continue()
            
        # Export Data to CSV Branch
        elif user_selection == 5:
            console_interface.update_screen('Export Data to CSV', 'Sorry! This feature has not be implemented yet! You will be returned to the main menu.')
            console_interface.prompt_enter_to_continue()
            
        # Exit Application Branch
        elif user_selection == 6:
            # TODO: Add a prompt asking the user if they would like to save their data to an external CSV file before quitting the application.
            console_interface.update_screen('Exiting Application...', 'You are about to close the application.')
            close_program = console_interface.prompt_yes_or_no('Are you sure you want to quit?')
            
        # User has entered an invalid option (either it is not an integer or it is not a valid integer.)
        else:
            console_interface.update_screen('Error: Invalid Option!', 'You have entered an invalid option.')
            console_interface.prompt_enter_to_continue()
    
       
    console_interface.update_screen('Good Bye!', 'Thank you for using the Python Movie Database Manager! \nThe application has now been closed.')
