import webbrowser


class Movie():
    # Paramater required to construct object are 4 of the following text variables movie title,storyline, poster image link and trailer website link

    def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)


__author__ = 'style'
