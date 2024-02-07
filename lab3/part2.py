#1 

def is_high_score(movie):
    return movie["imdb"] > 5.5

movies = [ { "name": "Usual Suspects", "imdb": 7.0, "category": "Thriller" },
{ "name": "Hitman", "imdb": 6.3, "category": "Action" }, 
{ "name": "Dark Knight", "imdb": 9.0, "category": "Adventure" }, 
{ "name": "The Help", "imdb": 8.0, "category": "Drama" },
{ "name": "The Choice", "imdb": 6.2, "category": "Romance" },
{ "name": "Colonia", "imdb": 7.4, "category": "Romance" }, 
{ "name": "Love", "imdb": 6.0, "category": "Romance" }, 
{ "name": "Bride Wars", "imdb": 5.4, "category": "Romance" },
{ "name": "AlphaJet", "imdb": 3.2, "category": "War" },
{ "name": "Ringing Crime", "imdb": 4.0, "category": "Crime" },
{ "name": "Joking muck", "imdb": 7.2, "category": "Comedy" }, 
{ "name": "What is the name", "imdb": 9.2, "category": "Suspense" },
{ "name": "Detective", "imdb": 7.0, "category": "Suspense" },
{ "name": "Exam", "imdb": 4.2, "category": "Thriller" }, 
{ "name": "We Two", "imdb": 7.2, "category": "Romance" } ]
print(is_high_score(movies)) 

#2

def get_high_score_movies(movies):
    q = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            q.append(movie)
    return q
movies = [ { "name": "Usual Suspects", "imdb": 7.0, "category": "Thriller" },
{ "name": "Hitman", "imdb": 6.3, "category": "Action" }, 
{ "name": "Dark Knight", "imdb": 9.0, "category": "Adventure" }, 
{ "name": "The Help", "imdb": 8.0, "category": "Drama" },
{ "name": "The Choice", "imdb": 6.2, "category": "Romance" },
{ "name": "Colonia", "imdb": 7.4, "category": "Romance" }, 
{ "name": "Love", "imdb": 6.0, "category": "Romance" }, 
{ "name": "Bride Wars", "imdb": 5.4, "category": "Romance" },
{ "name": "AlphaJet", "imdb": 3.2, "category": "War" },
{ "name": "Ringing Crime", "imdb": 4.0, "category": "Crime" },
{ "name": "Joking muck", "imdb": 7.2, "category": "Comedy" }, 
{ "name": "What is the name", "imdb": 9.2, "category": "Suspense" },
{ "name": "Detective", "imdb": 7.0, "category": "Suspense" },
{ "name": "Exam", "imdb": 4.2, "category": "Thriller" }, 
{ "name": "We Two", "imdb": 7.2, "category": "Romance" } ]
q = get_high_score_movies(movies)
print("Movies with IMDB score above 5.5:", q)

#3
def get_movies_by_category(category, movies):
    category_movies = [movie for movie in movies if movie["category"] == category]
    return category_movies

movies = [ { "name": "Usual Suspects", "imdb": 7.0, "category": "Thriller" },
{ "name": "Hitman", "imdb": 6.3, "category": "Action" }, 
{ "name": "Dark Knight", "imdb": 9.0, "category": "Adventure" }, 
{ "name": "The Help", "imdb": 8.0, "category": "Drama" },
{ "name": "The Choice", "imdb": 6.2, "category": "Romance" },
{ "name": "Colonia", "imdb": 7.4, "category": "Romance" }, 
{ "name": "Love", "imdb": 6.0, "category": "Romance" }, 
{ "name": "Bride Wars", "imdb": 5.4, "category": "Romance" },
{ "name": "AlphaJet", "imdb": 3.2, "category": "War" },
{ "name": "Ringing Crime", "imdb": 4.0, "category": "Crime" },
{ "name": "Joking muck", "imdb": 7.2, "category": "Comedy" }, 
{ "name": "What is the name", "imdb": 9.2, "category": "Suspense" },
{ "name": "Detective", "imdb": 7.0, "category": "Suspense" },
{ "name": "Exam", "imdb": 4.2, "category": "Thriller" }, 
{ "name": "We Two", "imdb": 7.2, "category": "Romance" } ]

category_name = input()
adventure_movies = get_movies_by_category(category_name, movies)
print(f"Movies under the category '{category_name}':", adventure_movies)

#4
def average_imdb_score(movies):
    n = sum(movie["imdb"] for movie in movies)
    a = n / len(movies)
    return a

movies = [ { "name": "Usual Suspects", "imdb": 7.0, "category": "Thriller" },
{ "name": "Hitman", "imdb": 6.3, "category": "Action" }, 
{ "name": "Dark Knight", "imdb": 9.0, "category": "Adventure" }, 
{ "name": "The Help", "imdb": 8.0, "category": "Drama" },
{ "name": "The Choice", "imdb": 6.2, "category": "Romance" },
{ "name": "Colonia", "imdb": 7.4, "category": "Romance" }, 
{ "name": "Love", "imdb": 6.0, "category": "Romance" }, 
{ "name": "Bride Wars", "imdb": 5.4, "category": "Romance" },
{ "name": "AlphaJet", "imdb": 3.2, "category": "War" },
{ "name": "Ringing Crime", "imdb": 4.0, "category": "Crime" },
{ "name": "Joking muck", "imdb": 7.2, "category": "Comedy" }, 
{ "name": "What is the name", "imdb": 9.2, "category": "Suspense" },
{ "name": "Detective", "imdb": 7.0, "category": "Suspense" },
{ "name": "Exam", "imdb": 4.2, "category": "Thriller" }, 
{ "name": "We Two", "imdb": 7.2, "category": "Romance" } ]
avg = average_imdb_score(movies)
print("Average IMDB score of the movies:", avg)

#5
def average_imdb_score_by_category(category, movies):
    c = [movie for movie in movies if movie["category"] == category]
    if not c:
        return None  # Return None if no movies in the specified category
    n = sum(movie["imdb"] for movie in c)
    a = n / len(c)
    return a

movies = [ { "name": "Usual Suspects", "imdb": 7.0, "category": "Thriller" },
{ "name": "Hitman", "imdb": 6.3, "category": "Action" }, 
{ "name": "Dark Knight", "imdb": 9.0, "category": "Adventure" }, 
{ "name": "The Help", "imdb": 8.0, "category": "Drama" },
{ "name": "The Choice", "imdb": 6.2, "category": "Romance" },
{ "name": "Colonia", "imdb": 7.4, "category": "Romance" }, 
{ "name": "Love", "imdb": 6.0, "category": "Romance" }, 
{ "name": "Bride Wars", "imdb": 5.4, "category": "Romance" },
{ "name": "AlphaJet", "imdb": 3.2, "category": "War" },
{ "name": "Ringing Crime", "imdb": 4.0, "category": "Crime" },
{ "name": "Joking muck", "imdb": 7.2, "category": "Comedy" }, 
{ "name": "What is the name", "imdb": 9.2, "category": "Suspense" },
{ "name": "Detective", "imdb": 7.0, "category": "Suspense" },
{ "name": "Exam", "imdb": 4.2, "category": "Thriller" }, 
{ "name": "We Two", "imdb": 7.2, "category": "Romance" } ]
cN = input()
avg = average_imdb_score_by_category(cN, movies)
if avg is not None:
    print(f"Average score of '{cN}' movies:", avg)
else:
    print(f"No movies found in the category '{cN}'")
