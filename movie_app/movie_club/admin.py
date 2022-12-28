from django.contrib import admin
from movie_club.models import Movie, Director, Review
# Register your models here.

admin.site.register(Director),
admin.site.register(Movie),
admin.site.register(Review)
