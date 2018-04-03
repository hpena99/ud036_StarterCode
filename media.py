import webbrowser
# Move class with properties useful for website displaying movie
# information and link to youtube trailer


class Movie():
    # constructor to intialize object properties for the movie's title,
    #  the movie's storyline, and image of the movie's original poster or
    #  box art, and the url to the movie's original trailer video found on
    #  youtube.
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # method plays trailer in browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
