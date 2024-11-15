"""
Creates, destroys, and prints user interface elements to the console.
"""

import os

# Module Variables
UI_WIDTH = 135
""""Int: Constant used to determine how wide (in terms of characters) UI elements are allowed to be."""

HEADER_TEXT = 'Python Movie Database Manager'
"""String: Constant used to determine text to be printed in the UI's header section."""

# Module Functions
def clear_screen():
    """
    Clears screen of all text.
    """
    # Check to see what operating system is being used and use appropriate clear command.
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def create_screen(title_text, body_text):
    """
    Creates screen with UI elements.
    
    Args:
        title_text (str): String containing text to be used for the UI's title.
        body_text (str): String containing text to be used for the UI's body.
    """
    clear_screen()
    print_header()
    print_body(title_text, body_text)

def print_header():
    """"
    Constructs UI header and prints it to console.
    """
    print('=' * UI_WIDTH)
    print(f'|{HEADER_TEXT:^{UI_WIDTH - 2}}|')
    print('=' * UI_WIDTH, '\n')
    
def print_body(title_text, body_text):
    """
    Constructs UI title and body and print it to console.
    
    Args:
        title_text (str): String containing text to be used for the UI's title.
        body_text (str): String containing text to be used for the UI's body.
    """
    print(f'{title_text:^{UI_WIDTH}}')
    print('-' * UI_WIDTH, '\n')
    print(f'{body_text}\n')