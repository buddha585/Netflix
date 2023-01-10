from rest_framework.response import Response
from rest_framework.decorators import api_view
from movie_club.models import Movie, Director, Review
from movie_club.serializers import MovieSerializer, DirectorSerializer, ReviewSerializer, MovieReviewSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        
        serializer = MovieSerializer(movies, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        rating = request.data.get('rating')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id, rating=rating)
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
            title = request.data.get('title')
            description = request.data.get('description')
            duration = request.data.get('duration')
            director_id = request.data.get('director_id')
            rating = request.data.get('rating')
            return Response(data={'message': 'data received!!!!',
                                  'movie': MovieSerializer(movie).data})
            
         
        
        

@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        name = request.data.get('name')
        age = request.data.get('age')
        rating = request.data.get('rating')
        director = Director.objects.create(name=name, age=age, rating=rating)
        director.save()
        return Response(data={'message': 'Director added',
                        'director': DirectorSerializer(director).data})

@api_view(['GET', 'DELETE', 'PUT'])
def directors_detail_view(request,**kwargs):
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
            name = request.data.get('name')
            age = request.data.get('age')
            rating = request.data.get('rating')
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
        text = request.data.get('text')
        movie = request.data.get('movie')
        stars = request.data.get('stars')
        review = Review.objects.create(text=text, movie=movie, stars=stars)
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
            text = request.data.get('text')
            movie = request.data.get('movie')
            stars = request.data.get('stars')
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
    
