"""
Program executes here.
"""

import console_ui

title_text = 'Welcome to the Python Movie Database Manager!'
"""String: Contains the text used for the user interface's title."""

body_text = 'To start off you can choose to import data from an external CSV file or go straight to the main menu.'
"""String: Contains the text used for the user interface's body."""

console_ui.create_screen(title_text, body_text)