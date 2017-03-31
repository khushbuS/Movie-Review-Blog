import webbrowser

class Movie():
    '''This class provides a way to store movies information.'''
    #constructor 
    def __init__(self,movie_title,movie_storyline,poster_img,trailer):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_img
        self.trailer_youtube_url=trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
