from django.urls import path
from movie_club.views import movies_view, directors_view, reviews_view, movies_detail_view, directors_detail_view, reviews_detail_view

urlpatterns = [
    path('movies/', movies_view),
    path('movies/<int:id>/', movies_detail_view),
    path('directors/', directors_view),
    path('directors/<int:id>/', directors_detail_view),
    path('reviews/', reviews_view),
    path('reviews/<int:id>/', reviews_detail_view)
    
]

