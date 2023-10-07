# Write a function that takes a movie dictionary from the above list and 
# return true if imdb rating is greater than 5. Additionally, you can also 
# alter the function to return whether the movie has low, medium or high rating

# Write a function that accepts the entire list of movies and a category and 
# returns the average score for that category.

# Write a function that accepts the movie list and a category and returns all 
# the movies belonging to that category. Your function should be able to throw 
# an error if that category does not exist

# List of movies dictionaries:
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def rating_more_than_5(movies, movie_name):
    for movie in movies:
        if movie['name'] == movie_name:
            return (movie['imdb'] > 5)

print("Movie Name: What is the name")
print("Rating above 5?", rating_more_than_5(movies, "What is the name"))
print()
print("Movie Name: Exam")
print("Rating above 5?", rating_more_than_5(movies, "Exam"))
print("---")
print()

def rating_category(movies, movie_name):
    for movie in movies:
        if movie['name'] == movie_name:
            if movie['imdb'] <= 10/3:
                return "Low"
            elif movie['imdb'] > 10/3 and movie['imdb'] <= 2 * 10/3:
                return "Medium"
            else:
                return "High"
            
print("Movie Name: What is the name")
print("Rating category : ", rating_category(movies, "What is the name"))
print()
print("Movie Name: Exam")
print("Rating category : ", rating_category(movies, "Exam"))
print()
print("Movie Name: AlphaJet")
print("Rating category : ", rating_category(movies, "AlphaJet"))
print("---")
print()

def average_of_category(movies, category):
    sum_of_ratings = 0
    number_of_movies = 0
    for movie in movies:
        if movie['category'] == category:
            sum_of_ratings += movie['imdb']
            number_of_movies += 1
    return sum_of_ratings/number_of_movies

print("Category: War")
print("Average Rating : ", average_of_category(movies, "War"))
print()
print("Category: Thriller")
print("Average Rating : ", average_of_category(movies, "Thriller"))
print("---")
print()

def get_movies_from_category(movies, category):
    movie_names = []
    for i in range(len(movies)):
        movie = movies[i]
        if movie['category'] == category:
            movie_names.append(movie['name'])
        if i == len(movies) - 1 and len(movie_names) == 0:
            raise Exception("Invalid Category!")
    return movie_names

print("Category: War")
print("Movies : ", get_movies_from_category(movies, "War"))
print()
print("Category: Romance")
print("Movies : ", get_movies_from_category(movies, "Romance"))
print()

try:
    print("Category: Mystery")
    print("Movies : ", get_movies_from_category(movies, "Mystery"))
    print()
except Exception as e:
    print(e)