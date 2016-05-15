# Movie Trailer Class Movie
# By Or Grunebaum
# Modified from Python Course

import webbrowser

class Movie():
    """ This class provides a way to store movie related information """
    
    
    def __init__(self, movie_title, poster_image, trailer_youtube):
    """ initialize movies to store relevant movie information we need for
        website.
        
        inputs Required: 
        Movie Title : string 
        Movie Poster : URL to a movie poster
        Movie Trailer : Youtube UR of Trailer
    """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

   ers
    def show_trailer(self):
    """show_trailer() opens the trailer in a new browser window. """
        webbrowser.open(self.trailer_youtube_url)

