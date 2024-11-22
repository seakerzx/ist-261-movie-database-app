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
    """int: Determines how wide (in characters) the user interface is allowed to be."""

    HEADER_TEXT = 'Python Movie Database Manager'
    """str: The text to be displayed in the Header section of user interface."""
    
    STARTUP_TITLE = 'Welcome to the Python Movie Database Manager!'
    """str: The default text for the Title section to be used if no string is supplied when initializing a new ConsoleUI object."""
    
    STARTUP_BODY = 'To start, you can choose to import data from an external CSV file or go straight to the main menu from the Options menu below.'
    """str: The default text for the Body section to be used if no string is supplied when initializing a new ConsoleUI object."""
    
    def __init__(self, title=STARTUP_TITLE, body=STARTUP_BODY):
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
        """
        Clears the console/terminal of all output.
        """
        # Check to see what operating system is being used and use appropriate clear command.
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
            
    def print_screen(self):
        """
        Prints out each section (Header, Title, Body, and Options menu) of the user interface to the console to create a screen for the user.
        """
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
    
    # Look into expanding the options menu into its own class with input handling and exception handling in the future.
    def print_options_menu(self, *available_options):
        """
        Prints out an options menu with the supplied options.
        
        Args:
            available_options (tuple): _Description_: Tuple containing options to print out to console.
        """
        print('Available Options:')
        
        for option in available_options:
            print(f'    {available_options.index(option) + 1}: {option}')
            
        print('\nPlease enter your choice:', end=' ')