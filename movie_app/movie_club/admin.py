from django.contrib import admin
from movie_club.models import Movie, Director, Review
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'rating')
    list_display_links = ("rating",)
    search_fields = ('title', 'description')
    
admin.site.register(Director),
admin.site.register(Movie, MovieAdmin),
admin.site.register(Review)
