from django.http import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Category_Movie, Movie


# CATEGORY TESTS
class CategoryMovieTests(APITestCase):
    def setUp(self):
        Category_Movie.objects.create(name='Action')
        Category_Movie.objects.create(name='Comedy')
        Category_Movie.objects.create(name='Terror')

    def test_get_method_categories_success(self):
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        queryset = Category_Movie.objects.all()
        self.assertEqual(queryset.count(), 3)

    def test_post_method_category_success(self):
        url = reverse('category-list')
        data = {'name': 'Thriller'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        queryset = Category_Movie.objects.all()
        self.assertEqual(queryset.count(), 4)

    def test_post_method_category_fail(self):
        url = reverse('category-list')
        # "name" changed for "name_changed" to fail post method
        data = {'name_changed': 'Thriller'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        queryset = Category_Movie.objects.all()
        self.assertEqual(queryset.count(), 3)

    def test_put_method_category_success(self):
        queryset = Category_Movie.objects.get(name='Action')
        id_category = queryset.id
        url = f'/api/categories/{id_category}/'
        data = {'name': 'Drama'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        queryset = Category_Movie.objects.get(pk=id_category)
        self.assertEqual(queryset.name, data['name'])

    def test_patch_method_category_success(self):
        queryset = Category_Movie.objects.get(name='Action')
        id_movie = queryset.id
        url = f'/api/categories/{id_movie}/'
        data = {'name': 'Drama'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        queryset = Category_Movie.objects.get(pk=id_movie)
        self.assertEqual(queryset.name, data['name'])

    def test_delete_method_category_success(self):
        queryset = Category_Movie.objects.get(name='Action')
        id_movie = queryset.id
        url = f'/api/categories/{id_movie}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        queryset = Category_Movie.objects.all()
        self.assertEqual(queryset.count(), 2)


# MOVIE TESTS
class MovieTest(APITestCase):
    def setUp(self):
        Category_Movie.objects.create(name='Action')
        Category_Movie.objects.create(name='Comedy')

        Movie.objects.create(
            title = 'Title 1',
            description = 'Description 1',
            category = Category_Movie.objects.get(name='Action'),
            rating = 6.7,
            num_ratings = 21,
            director = 'Director 1',
            release_date = '2021-05-28',
            cover_page = 'https://m.media-amazon.com/images/M/MV5B.jpg'
        )
        Movie.objects.create(
            title = 'Title 2',
            description = 'Description 2',
            category = Category_Movie.objects.get(name='Comedy'),
            rating = 8.5,
            num_ratings = 35,
            director = 'Director 2',
            release_date = '1993-03-22',
            cover_page = 'https://m.media-amazon.com/images/M/MDH8.jpg'
        )

    def test_put_method_movie_success(self):
        queryset = Movie.objects.first()
        id_movie = queryset.id
        url = f'/api/movies/{id_movie}/'
        data = {
            'title': 'Title modified',
            'category': Category_Movie.objects.get(name='Comedy').id,
            'release_date': '2021-05-28'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        queryset = Movie.objects.get(pk=id_movie)
        self.assertEqual(queryset.title, data['title'])
