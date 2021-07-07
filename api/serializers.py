from .models import Movie, Category_Movie
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class CategoryMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_Movie
        fields = '__all__'