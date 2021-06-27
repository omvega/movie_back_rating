from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class ModelBaseApp(models.Model):
    crated_by = models.CharField(max_length=150, blank=True, null=True)
    updated_by = models.CharField(max_length=150, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Category_Movie(ModelBaseApp):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return f'{ self.name }'

    class Meta:
        verbose_name_plural = 'Categories'

class Movie(ModelBaseApp):
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category_Movie, on_delete=models.CASCADE, related_name="movie_category")
    rating = models.FloatField(default=0.0, validators=[MinValueValidator(0.9), MaxValueValidator(58)])
    director = models.CharField(max_length=255, blank=True, null=True, default='Unknown')
    release_date = models.DateField()
    cover_page = models.CharField(max_length=255, blank=True, null=True)

    def __str(self):
        return f'{ self.title }'

    class Meta:
        verbose_name_plural = 'Movies'
