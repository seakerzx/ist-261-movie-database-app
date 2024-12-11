import os

class ConsoleUI:
    """
    Manages console interactions, including screen display and user input prompts.

    Attributes:
        header (str): Text displayed in the Header section of the user interface.
        title (str): Text displayed in the Title section of the user interface.
        body (str): Text displayed in the Body section of the user interface.
    """

    UI_WIDTH = 150
    HEADER_TEXT = 'Python Movie Database Manager'

    def __init__(self, title, body):
        self.header = self.HEADER_TEXT
        self.title = title
        self.body = body

    def clear_screen(self):
        """Clears the console output."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_screen(self):
        """Displays the header, title, and body in a formatted console screen."""
        self.clear_screen()
        print('=' * self.UI_WIDTH)
        print(f'|{self.header:^{self.UI_WIDTH - 2}}|')
        print('=' * self.UI_WIDTH, '\n')
        print(f'{self.title:^{self.UI_WIDTH}}')
        print('-' * self.UI_WIDTH, '\n')
        print(f'{self.body}\n')

    def update_screen(self, new_title=None, new_body=None):
        """Updates the title and body, then refreshes the screen."""
        if new_title:
            self.title = new_title
        if new_body:
            self.body = new_body
        self.print_screen()

    def prompt_options_menu(self, *options):
        """
        Displays a menu of options and prompts for user selection.

        Args:
            options (tuple): List of options to display.

        Returns:
            int: The selected option number.
        """
        print('Available Options:')
        for i, option in enumerate(options, start=1):
            print(f'   {i}: {option}')

        while True:
            try:
                choice = int(input(f'\nPlease enter your choice (1-{len(options)}): '))
                if 1 <= choice <= len(options):
                    return choice
                else:
                    raise ValueError
            except ValueError:
                print(f'Invalid input. Enter a number between 1 and {len(options)}.')

    def prompt_yes_or_no(self, question):
        """
        Prompts a yes-or-no question and returns a boolean response.

        Args:
            question (str): The yes-or-no question to display.

        Returns:
            bool: True for 'Yes', False for 'No'.
        """
        while True:
            response = input(f'{question} (Yes/No): ').strip().lower()
            if response in ['yes', 'y']:
                return True
            elif response in ['no', 'n']:
                return False
            print('Invalid input. Please enter Yes or No.')

    def prompt_ask_for_string(self, question):
        """
        Prompts the user for a string response.

        Args:
            question (str): The question to display.

        Returns:
            str: User's response as a string.
        """
        return input(f'{question}: ').strip()

    def prompt_ask_for_number(self, question, get_float=False):
        """
        Prompts the user to enter a number, returning it as an integer or float.

        Args:
            question (str): The question to display.
            get_float (bool): If True, returns a float. Otherwise, returns an integer.

        Returns:
            int or float: User's response as a number.
        """
        while True:
            try:
                return float(input(f'{question}: ')) if get_float else int(input(f'{question}: '))
            except ValueError:
                print('Invalid input. Please enter a valid number.')

    def prompt_enter_to_continue(self):
        """Pauses execution until the user presses Enter."""
        input('Press Enter to continue...')

# If this file is launched as a script, print an error message.
if __name__ == '__main__':
    print('\nError: File launched as script!\nThe program does not launch from this file!\nPlease execute \'main.py\' to run the Python Movie Database Manager.\n')