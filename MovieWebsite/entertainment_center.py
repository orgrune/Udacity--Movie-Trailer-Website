# Movie Trailer Main File
# By Or Grunebaum
# Modified from Python Course
import fresh_tomatoes
import media

# enable api by setting key for movie database
from tmdb3 import set_key, set_cache
set_key('')
set_cache('null')

# import movie module from the movie database
from tmdb3 import Movie
# add all my favourite movies
list_movies = list()
list_movies.extend([Movie(862),Movie(1542),Movie(671),Movie(83542),Movie(957),
                    Movie(10156),Movie(8005),Movie(658), Movie(10671),
                    Movie(813),Movie(86838),Movie(640),Movie(98),
                    Movie(616),Movie(1669)])

# create movies list to store information needed for the movie trailer website
# (using the Fresh Tomatoes Script) provided by udacity
movies = list()

# loop through the list of movies selected, and add them to movies list to be 
# displayed. Specifically we are adding the title, poster, and youtube url. 
for number in range(len(list_movies)):
    movies.append(media.Movie(list_movies[number].title,
                        list_movies[number].poster.geturl(),
                        list_movies[number].youtube_trailers[0].geturl()))

#send to movie page 
fresh_tomatoes.open_movies_page(movies)

