import fresh_tomatoes 
import media


toy_story = media.Movie("Toy Story","Toy Story is about the 'secret life of toys' when people are not around.","http://www.pixartalk.com/wp-content/uploads/2009/06/tstheatrical.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

fault_stars = media.Movie("Fault in our stars","Life is what happens to us when we are busy making other plans.","https://nesmedia2017.files.wordpress.com/2016/08/tfios-poster.jpg","https://www.youtube.com/watch?v=9ItBvH5J6ss")

dead_silence = media.Movie("Dead Silence","Its amazing how loud things are when everything is dead silent.","https://www.tribute.ca/tribute_objects/images/movies/dead_silence/poster_lg.jpg","https://www.youtube.com/watch?v=8b_HVtHmK30")

two_states = media.Movie("Two States","Love story of people belonging from two different states","http://4.bp.blogspot.com/-FRnkbQbPRus/U1Igh3UQpPI/AAAAAAAABaI/6PvCtLYrOi0/s1600/2States_image.jpg","https://www.youtube.com/watch?v=CGyAaR2aWcA")

despicableme = media.Movie("Despicable me","A funny, sweet, self-contained story about a guy named Gru who renounces villainy and embraces fatherhood.","https://image.tmdb.org/t/p/original/qY04idV5FsgCSHBdFmSkgnT9nne.jpg","https://www.youtube.com/watch?v=sUkZFetWYY0")

movies = [toy_story, fault_stars, dead_silence, two_states, despicableme]
fresh_tomatoes.open_movies_page(movies)
