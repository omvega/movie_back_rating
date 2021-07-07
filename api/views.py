from .models import Movie, Category_Movie

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import MovieSerializer, CategoryMovieSerializer


class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(
        methods=['post'], detail=True,
        url_path='rating-movie', url_name='rating_movie')
    def rating_movie(self, request, pk=None):
        movie = self.get_object()
        num_ratings = movie.num_ratings + 1
        form_data = {
            'rating':
                (movie.rating + float(request.POST['rating'])) / num_ratings,
            'num_ratings': num_ratings
        }

        serializer = MovieSerializer(movie, data=form_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryMovieViewset(viewsets.ModelViewSet):
    queryset = Category_Movie.objects.all()
    serializer_class = CategoryMovieSerializer
