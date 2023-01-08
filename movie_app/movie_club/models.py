from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=40)
    age = models.CharField(max_length=2, default=18)
    rating = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.name
    
    @property
    def movie_count(self):
        return self.movies.all().count()

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=7)
    director= models.ForeignKey(Director, on_delete=models.CASCADE, blank=True,
                                related_name='movies')
    rating = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.title
     
    @property 
    def review_count(self):
        return self.reviews.all().count()
    
rate = (
    (1, '⭐'),
    (2, '⭐⭐'),
    (3, '⭐⭐⭐'),
    (4, '⭐⭐⭐⭐'),
    (5, '⭐⭐⭐⭐⭐')
)
class Review(models.Model):
    text = models.TextField(max_length=425)    
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name ='reviews')
    stars = models.IntegerField(default=1, choices=rate)
    
    def  __str__(self):
        return self.text
