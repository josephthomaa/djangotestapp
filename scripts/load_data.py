import csv
import os
from testapi.models import Movie, UserRatings

# movie_path = '/home/one/Desktop/djangotestapp/movies.csv'
# def run():
#     with open(movie_path) as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             print(row['title'])
#             movie = Movie(id=row['id'], title=row['title'], genres=row['genres'])
#             movie.save()
    

ratings_path = '/home/one/Desktop/djangotestapp/ratings.csv'


def run():
    with open(ratings_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['userId'])
            ratings = UserRatings(userId_id=row['userId'], movieId_id=row['movieId'],
                                rating=row['rating'])
            ratings.save()
