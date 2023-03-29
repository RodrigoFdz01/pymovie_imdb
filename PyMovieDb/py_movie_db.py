from PyMovieDb import IMDB
imdb = IMDB()
#print(dir(imdb))

# movie and year
#res = imdb.search('Shazam', year=2019) # ok

# Fetch  by actor name
#res = imdb.person_by_name('Christian Bale')  
actor_by_id = imdb.person_by_id("nm3822770")
#print(res)
#sprint(actor_by_id)


# Fetch Movie by movie name
movie_name = imdb.get_by_name("The Dark Knight")  ## esto esta ok
print(movie_name[0][0])

# Fetch Movie by popluar movies
popular = imdb.popular_movies(genre=None) # list of 50 movies
#print(popular)


