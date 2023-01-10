from rest_framework import serializers
from movie_club.models import Movie, Director, Review

        
class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = ('id', 'name', 'age', 'movie_count', 'rating')
    
    def get_movie_count(self, director):
        return director.movie_count

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    review_count = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ('director', 'id', 'title', 'description', 'duration', 'rating', 'reviews', 'review_count' )

    def get_review_count(self, movie):
        return movie.review_count
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text'.split()      
         
class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_reviews(self, movie):
        return [i.stars for i in movie.reviews.all()]
    
    def get_rating(self, movie):
        return movie.rating

