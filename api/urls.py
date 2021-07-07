from django.urls import path, include

from rest_framework import routers
from .views import CategoryMovieViewset, MovieViewset

router = routers.DefaultRouter()

router.register('movies', MovieViewset, basename='movie')
# router.register('movie/print_movie', MovieViewset.print_movie.as_view, basename='MovieView')
router.register('categories', CategoryMovieViewset, basename='category')

urlpatterns = [
    path('api/', include(router.urls)),
]