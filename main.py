"""
Program executes here.
"""

import user_interface
import movies

if __name__ == '__main__':
    console_interface = user_interface.ConsoleUI()
    console_interface.print_screen()
    
    console_interface.print_options_menu('Go to Main Menu', 'Import Data from CSV', 'Exit Application')