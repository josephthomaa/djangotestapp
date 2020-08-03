from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=300)
    genres = models.TextField()


class User(models.Model):
    name = models.CharField(max_length=100)


class UserRatings(models.Model):
    userId = models.ForeignKey(User, related_name='user', on_delete=models.DO_NOTHING)
    movieId = models.ForeignKey(Movie, related_name='movie', on_delete=models.DO_NOTHING)
    rating = models.FloatField()
