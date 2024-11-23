class Movie:
    def __init__(self, title, genre, year, runtime, score):
        self.title = title
        self.genre = genre
        self.year = year
        self.runtime = runtime
        self.score = score
        
    def add_movie(self):
        pass
    
    def update_movie(self):
        pass
    
    def remove_movie(self):
        pass

# TODO: Everything here.

# If this file is launched as as script, print an error message alerting the user to open the correct file.
if __name__ == '__main__':
    print('\nError: File launched as script!\nThe program does not launch from this file!\nPlease execute \'main.py\' in order to launch the Python Movie Database Manager.\n')