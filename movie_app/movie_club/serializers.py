from rest_framework import serializers
from movie_club.models import Movie, Director, Review

class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = ('id', 'name', 'age', 'movie_count', 'rating')

    def get_movie_count(self, director):
        return director.movie_count

class DirectorValidaterSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=18)
    age = serializers.CharField(max_length=2)
    rating = serializers.IntegerField(max_value=10)

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    review_count = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ('director', 'id', 'title', 'description', 'duration', 'rating', 'reviews', 'review_count')

    def get_review_count(self, movie):
        return movie.review_count

class MovieValidaterSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=100)
    description = serializers.CharField(required=False, default='No text')
    duration = serializers.CharField()
    director_id = serializers.IntegerField(min_value=1)
    rating = serializers.IntegerField()

    def validate_director_id(self, director_id):
        try:
            directors = Director.objects.filter(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director not found')
        return director_id

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'movie', 'text', 'stars')

class ReviewValidaterSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=8, max_length=150)
    movie_id = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField()

    def validate_director_id(self, movie_id):
        try:
            directors = Movie.objects.filter(id=movie_id_id)
        except Movie.DoesNotExist:
            raise ValidationError('Review not found')
        return movie_id

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
