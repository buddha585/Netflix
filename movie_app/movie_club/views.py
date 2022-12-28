from rest_framework.response import Response
from rest_framework.decorators import api_view
from movie_club.models import Movie, Director, Review
from movie_club.serializers import MovieSerializer, DirectorSerializer, ReviewSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        
        serializer = MovieSerializer(movies, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movies_detail_view(request, **kwargs):
    if request.method == 'GET':
        movie = Movie.objects.get(id=kwargs['id'])
        serializer = MovieSerializer(movie, many=False)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def directors_detail_view(request,**kwargs):
    if request.method == 'GET':
        director = Director.objects.get(id=kwargs['id'])
        serializer = DirectorSerializer(director, many=False)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def reviews_detail_view(request, **kwargs):
    if request.method == 'GET':
        review = Review.objects.get(id=kwargs['id'])
        serializer = ReviewSerializer(review, many=False)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
