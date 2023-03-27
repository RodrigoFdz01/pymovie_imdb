from PyMovieDb import IMDB
imdb = IMDB()
#res = imdb.search('Shazam', year=2019) # ok
res = imdb.person_by_name("Christian Bale") 
for data in res:
    print(data)


# Fetch Movie by name
# res2 = imdb.get_by_name("The Dark Knight")  ## esto esta ok
#print(res2)