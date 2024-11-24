"""
Creates, destroys, and prints user interface elements to the console.
"""

import os

class ConsoleUI:
    """
    Creates, destroys, and prints user interface objects to the console.
 
    Attributes:
        header (str): Text that will be displayed in the user interface's Header section (this should not change during runtime).
        title (str): Text that will be displayed in the user interface's Title section.
        body (str): Text that will be displayed in the user interface's Body section.
        
    Todo:
        * Write more descriptive class description.
        * Create Options menu functionality
    """
    
    UI_WIDTH = 150
    """int: Determines how wide (in characters) the console user interface is allowed to be."""

    HEADER_TEXT = 'Python Movie Database Manager'
    """str: The text to be displayed in the Header section of user interface."""
    
    def __init__(self, title, body):
        """
        Initializes new ConsoleUI object.

        Args:
            title (str, optional): Text to be displayed in the Title section of the user interface. Defaults to STARTUP_TITLE.
            body (str, optional): Text to be displayed in the Body section of the user interface. Defaults to STARTUP_BODY.
        """
        self.header = ConsoleUI.HEADER_TEXT
        self.title = title
        self.body = body
        
    def clear_screen(self):
        """Clears the console/terminal of all output."""
        # Check to see what operating system is being used and use appropriate clear command.
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
            
    def print_screen(self):
        """Prints out each section (Header, Title, Body, and Options menu) of the user interface to the console to create a screen for the user."""
        self.clear_screen()
        
        # Print Header section
        print('=' * ConsoleUI.UI_WIDTH)
        print(f'|{self.header:^{ConsoleUI.UI_WIDTH - 2}}|')
        print('=' * ConsoleUI.UI_WIDTH, '\n')
        
        # Print Title section
        print(f'{self.title:^{ConsoleUI.UI_WIDTH}}')
        print('-' * ConsoleUI.UI_WIDTH, '\n')
        
        # Print Body section
        print(f'{self.body}\n')
        
    def update_screen(self, new_title = None, new_body = None):
        """
        Changes title and body attributes to supplied strings (if supplied) and redraws the screen.
        
        Note: If you need to change the body text only, call this function with object_name.update_screen(new_body='New string here').
        
        Args:
            new_title (str, optional): _Description_: Text to change the object's title attribute to. Defaults to None (Null).
            new_body (str, optional): _Description_: Text to change the object's body attribute to. Defaults to None (Null).
        """
        if new_title is not None:
            self.title = new_title
        
        if new_body is not None:  
            self.body = new_body
        
        self.print_screen()
    
    # These fuctions are for collecting user data.
    # TODO: Have user input be validated by these functions, rather than main.py to keep main.py tidy and readable.
    # TODO: Expand docstrings for each function.
    def prompt_options_menu(self, *available_options):
        """
        Constructs an options menu from the arguments passed through to this function.
        
        Args:
            available_options (tuple): _Description_: Tuple containing options to print out to console.
            
        Returns:
            selected_option (int): _Description_: Tuple containing options to print out to console.
        """
        print('Available Options:')
        
        for option in available_options:
            print(f'   {available_options.index(option) + 1}: {option}')
            
        print(f'\nPlease enter your choice (1 - {len(available_options)}):', end=' ')

    def prompt_yes_or_no(self, question):
        """
        Constructs a yes-or-no prompt for the user to answer then collects the user's input.

        Args:
            question (str): _Description_: Question to ask the user.

        Returns:
            Returns True if the user answers "Yes", returns False if the user enters "No"
        """
        user_selection = input(f'{question} (Yes or No): ')
        
        if user_selection == 'Yes' or user_selection == 'yes' or user_selection == 'Y' or user_selection == 'y':
            return True
        elif user_selection == 'No' or user_selection == 'no' or user_selection == 'N' or user_selection == 'n':
            return False
        else:
            # TODO: Implement actual input validating and reprompt user.
            print('Not valid. Returning False.')
            self.prompt_enter_to_continue()
            return False
    
    def prompt_ask_for_string(self):
        """Prompts the user to enter a string."""
        #TODO: Implement this
        pass
    
    def prompt_ask_for_number(self):
        """Prompts the user to enter a number."""
        #TODO: Implement this
        pass
    
    def prompt_enter_to_continue(self):
        """Halts application and prompts the user to press their Enter key to continue."""
        input('Press Enter to continue...')

# If this file is launched as as script, print an error message alerting the user to open the correct file.
if __name__ == '__main__':
    print('\nError: File launched as script!\nThe program does not launch from this file!\nPlease execute \'main.py\' in order to launch the Python Movie Database Manager.\n')