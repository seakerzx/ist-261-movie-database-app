import csv

class Movie:
    """Represents a movie with basic attributes and related operations."""

    def __init__(self, title, genre, year, runtime, score, director):
        """
        Initializes a Movie instance with given attributes.

        Args:
            title (str): The title of the movie.
            genre (str): The genre of the movie.
            year (int): The release year of the movie.
            runtime (int): The runtime of the movie in minutes.
            score (float): The score of the movie out of 10.
            director (str): The director of the movie.
        """
        self.title = title
        self.genre = genre
        self.year = year
        self.runtime = runtime
        self.score = score
        self.director = director

    def update_movie(self, field, new_value):
        """
        Updates a specific field of the movie with a new value.

        Args:
            field (str): The name of the field to update (e.g., 'title', 'genre').
            new_value: The new value for the field.

        Raises:
            ValueError: If the new value is invalid for the given field.
        """
        if field == 'title':
            self.title = new_value
        elif field == 'genre':
            self.genre = new_value
        elif field == 'year':
            self.year = int(new_value)
        elif field == 'runtime':
            self.runtime = int(new_value)
        elif field == 'score':
            self.score = float(new_value)
        elif field == 'director':
            self.director = new_value
        else:
            raise ValueError(f"Invalid field: {field}")

    @classmethod
    def create_movie_from_input(cls, console_ui):
        """
        Prompts the user to input movie details and returns a Movie instance.

        Args:
            console_ui: An instance of ConsoleUI to interact with the user.

        Returns:
            Movie: A new Movie instance if input is valid, otherwise None.
        """
        console_ui.update_screen('Add a Movie', 'Please enter the movie details:')

        title = input('Title: ')
        genre = input('Genre: ')
        year = input('Year: ')
        runtime = input('Runtime (minutes): ')
        score = input('Score (out of 10): ')
        director = input('Director: ')

        try:
            year = int(year)
            runtime = int(runtime)
            score = float(score)
            return cls(title, genre, year, runtime, score, director)
        except ValueError:
            console_ui.update_screen('Error', 'Invalid input for numeric fields.')
            console_ui.prompt_enter_to_continue()
            return None

    @staticmethod
    def import_from_csv(file_path):
        """
        Imports movies from a CSV file and returns a list of Movie objects.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            list: A list of Movie instances.
        """
        movies_list = []
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        movies_list.append(Movie(
                            title=row['Title'],
                            genre=row['Genre'],
                            year=int(row['Year']),
                            runtime=int(row['Runtime']),
                            score=float(row['Score']),
                            director=row['Director']
                        ))
                    except ValueError as ve:
                        print(f"Skipping invalid row: {row}, Error: {ve}")
            print(f"Successfully imported {len(movies_list)} movies from '{file_path}'.")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")
        except KeyError as ke:
            print(f"Error: Missing column in CSV: {ke}")
        return movies_list

    @staticmethod
    def export_to_csv(file_path, movies_list):
        """
        Exports a list of Movie objects to a CSV file.

        Args:
            file_path (str): The path to the CSV file.
            movies_list (list): A list of Movie instances to export.
        """
        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['Title', 'Genre', 'Year', 'Runtime', 'Score', 'Director'])
                writer.writeheader()
                for movie in movies_list:
                    writer.writerow({
                        'Title': movie.title,
                        'Genre': movie.genre,
                        'Year': movie.year,
                        'Runtime': movie.runtime,
                        'Score': movie.score,
                        'Director': movie.director
                    })
            print(f"Successfully exported {len(movies_list)} movies to '{file_path}'.")
        except IOError as e:
            print(f"Error writing to file '{file_path}': {e}")

if __name__ == '__main__':
    print('\nError: File launched as script!\nThe program does not launch from this file!\nPlease execute \"main.py\" in order to launch the Python Movie Database Manager.\n')