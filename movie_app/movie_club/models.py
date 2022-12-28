from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=40)
    age = models.CharField(max_length=2, default=18)
    rating = models.IntegerField(default=0)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=7)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

class Review(models.Model):
    text = models.TextField(max_length=425)    
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)

