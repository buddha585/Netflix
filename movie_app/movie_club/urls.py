from django.urls import path
from movie_club.views import movies_view, directors_view, reviews_view, movies_detail_view,\
directors_detail_view, reviews_detail_view, movies_reviews_view
urlpatterns = [
    path('api/v1/movies/', movies_view),
    path('api/v1/movies/<int:id>/', movies_detail_view),
    path('api/v1/directors/', directors_view),
    path('api/v1/directors/<int:id>/', directors_detail_view),
    path('api/v1/movies/reviews/', movies_reviews_view),
    path('api/v1/reviews/', reviews_view),
    path('api/v1/reviews/<int:id>/', reviews_detail_view)
    
]

