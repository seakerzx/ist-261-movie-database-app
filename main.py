import os
import user_interface
import movies

def main():
    close_program = False
    console_interface = user_interface.ConsoleUI('Main Menu', 'Welcome to the Python Movie Database Manager!')
    movie_list = []

    while not close_program:
        console_interface.update_screen('Main Menu', 'Welcome to the Python Movie Database Manager!')
        user_selection = console_interface.prompt_options_menu(
            'Add a Movie', 'Update a Movie', 'Search for Movies',
            'Import Data from CSV', 'Export Data to CSV', 'Exit Application'
        )

        if user_selection == 1:
            # Add a Movie
            new_movie = movies.Movie.create_movie_from_input(console_interface)
            if new_movie:
                movie_list.append(new_movie)
                console_interface.update_screen('Success', f'Movie "{new_movie.title}" added successfully!')
            console_interface.prompt_enter_to_continue()

        elif user_selection == 2:
            # Update a Movie
            if not movie_list:
                console_interface.update_screen('Error', 'No movies available to update.')
                console_interface.prompt_enter_to_continue()
                continue

            console_interface.update_screen('Update a Movie', 'Available movies (sorted alphabetically):')
            sorted_movies = sorted(movie_list, key=lambda movie: movie.title.lower())
            for i, movie in enumerate(sorted_movies, start=1):
                print(f"{i}. {movie.title}")

            print("\nEnter the title of the movie to update:")
            search_title = input().strip()
            matching_movies = [movie for movie in movie_list if movie.title.lower() == search_title.lower()]

            if not matching_movies:
                console_interface.update_screen('Not Found', f'No movie found with the title "{search_title}".')
            else:
                movie_to_update = matching_movies[0]
                console_interface.update_screen('Movie Found', f'Current details:\n{movie_to_update.display_details()}')
                console_interface.prompt_enter_to_continue()

                console_interface.update_screen('Update Options', 'What would you like to update?')
                console_interface.prompt_options_menu('Title', 'Genre', 'Year', 'Runtime', 'Score', 'Director', 'Cancel Update')

                try:
                    update_choice = int(input())
                except ValueError:
                    console_interface.update_screen('Error', 'Invalid input. Returning to the main menu.')
                    console_interface.prompt_enter_to_continue()
                    continue

                if update_choice in range(1, 7):
                    new_value = input('Enter the new value: ').strip()
                    try:
                        movie_to_update.update_movie(update_choice, new_value)
                        console_interface.update_screen('Success', f'Movie updated successfully:\n{movie_to_update.display_details()}')
                    except ValueError as e:
                        console_interface.update_screen('Error', str(e))
                elif update_choice == 7:
                    console_interface.update_screen('Cancelled', 'Movie update cancelled.')
                else:
                    console_interface.update_screen('Error', 'Invalid option. Returning to the main menu.')

            console_interface.prompt_enter_to_continue()

        elif user_selection == 3:
            # Search for Movies
            console_interface.update_screen('Search for Movies', 'Feature not yet implemented!')
            console_interface.prompt_enter_to_continue()

        elif user_selection == 4:
            # Import Data from CSV
            file_path = input('Enter the CSV file path: ').strip()
            if not os.path.isfile(file_path):
                console_interface.update_screen('File Not Found', f'The file "{file_path}" does not exist.')
                create_file = console_interface.prompt_yes_or_no('Would you like to create a new CSV file?')
                if create_file:
                    movies.Movie.export_to_csv(file_path, movie_list)
                    console_interface.update_screen('File Created', f'Empty CSV file created at "{file_path}".')
                else:
                    console_interface.update_screen('Returning to Main Menu', 'No file created.')
            else:
                imported_movies = movies.Movie.import_from_csv(file_path)
                if imported_movies:
                    movie_list.extend(imported_movies)
                    console_interface.update_screen('Success', f'{len(imported_movies)} movies imported successfully!')
                else:
                    console_interface.update_screen('No Movies Imported', 'No valid movies found in the file.')
            console_interface.prompt_enter_to_continue()

        elif user_selection == 5:
            # Export Data to CSV
            if not movie_list:
                console_interface.update_screen('Error', 'No movies to export.')
            else:
                file_path = input('Enter the CSV file path to save: ').strip()
                movies.Movie.export_to_csv(file_path, movie_list)
                console_interface.update_screen('Success', f'Movies exported successfully to "{file_path}".')
            console_interface.prompt_enter_to_continue()

        elif user_selection == 6:
            # Exit Application
            close_program = console_interface.prompt_yes_or_no('Are you sure you want to quit?')

        else:
            console_interface.update_screen('Error', 'Invalid selection. Please choose a valid option.')
            console_interface.prompt_enter_to_continue()

    console_interface.update_screen('Goodbye!', 'Thank you for using the Python Movie Database Manager!')

if __name__ == '__main__':
    main()