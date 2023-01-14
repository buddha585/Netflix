from rest_framework.response import Response
from rest_framework.decorators import api_view
from movie_club.models import Movie, Director, Review
from movie_club.serializers import MovieSerializer, DirectorSerializer, ReviewSerializer, MovieReviewSerializer,\
MovieValidaterSerializer, DirectorValidaterSerializer, ReviewValidaterSerializer
from rest_framework import status


# Create your views here.

@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = MovieValidaterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')
        rating = serializer.validated_data.get('rating')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id,
                                     rating=rating)
        movie.save()
        return Response(data={'message': 'data received',
                              'movie': MovieSerializer(movie).data})


@api_view(['GET', 'PUT', 'DELETE'])
def movies_detail_view(request, **kwargs):
    try:
        movie = Movie.objects.get(id=kwargs['id'])
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Movie not found'})
    if request.method == 'GET':
        serializer = MovieSerializer(movie, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = MovieValidaterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration')
        movie.director_id = serializer.validated_data.get('director_id')
        movie.rating = serializer.validated_data.get('rating')
        movie.save()
        return Response(data={'message': 'data received!!!!',
                              'movie': MovieSerializer(movie).data})


@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = DirectorValidaterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors':serializer.errors},
                                 status=status.HTTP_400_BAD_REQUEST)
        name = serializer.validated_data.get('name')
        age = serializer.validated_data.get('age')
        rating = serializer.validated_data.get('rating')
        director = Director.objects.create(name=name, age=age, rating=rating)
        director.save()
        return Response(data={'message': 'Director added',
                              'director': DirectorSerializer(director).data})


@api_view(['GET', 'DELETE', 'PUT'])
def directors_detail_view(request, **kwargs):
    try:
        director = Director.objects.get(id=kwargs['id'])
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Director not found'})
    if request.method == 'GET':
        serializer = DirectorSerializer(director, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = DirectorValidaterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get('name')
        age = serializer.validated_data.get('age')
        rating = serializer.validated_data.get('rating')
        director = Director.objects.create(name=name, age=age, rating=rating)
        director.save()
        return Response(data={'message': 'data received',
                              'director': DirectorSerializer(director).data})


@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ReviewValidaterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_data.get('movie_id')
        stars = serializer.validated_data.get('stars')
        review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        review.save()
        return Response(data={'message': 'data received!',
                              'review': ReviewSerializer(review).data})


@api_view(['GET', 'DELETE', 'PUT'])
def reviews_detail_view(request, **kwargs):
    try:
        review = Review.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Review not found'})
    if request.method == 'GET':
        serializer = ReviewSerializer(review, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = ReviewValidaterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_datata.get('movie')
        stars = serializer.validated_data.get('stars')
        review = Review.objects.create(text=text, movie=movie, stars=stars)
        review.save()
        return Response(data={'message': 'data received!',
                              'review': ReviewSerializer(review).data})


@api_view(['GET'])
def movies_reviews_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieReviewSerializer(movie, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
