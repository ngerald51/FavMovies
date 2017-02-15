import Movie
import fresh_tomatoes

# Initializing the list of my favourite movies

superman = Movie.Movie("Superman", "Man of Steel",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI5OTYzNjI0Ml5BMl5BanBnXkFtZTcwMzM1NDA1OQ@@._V1_.jpg",
                       "https://www.youtube.com/watch?v=EBatxZ90wag")
Wolverine = Movie.Movie("LOGAN", "LOGAN",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUwNjU5NjgxOF5BMl5BanBnXkFtZTgwMDM5NjY5MDI@._V1_.jpg",
                        "https://www.youtube.com/watch?v=XaE_9pfybL4")
Batman = Movie.Movie("Dark Knight", "Dark Knight",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY")

movies = [Wolverine, superman, Batman]
fresh_tomatoes.open_Movies_page(movies)



__author__ = 'style'
