# Module Name: Entertainment Center - application startup

import fresh_tomatoes
import media

# New Movie objects
toy_story = media.Movie("Toy Story",
                        "Boy and Toys",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                    "Marines on a planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

movies = [toy_story,avatar]

fresh_tomatoes.open_movies_page(movies) #Build and page with listed movies
