# bookscraper/models.py
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    average_rating = models.FloatField()
    cover_image_url = models.URLField()

    def __str__(self):
        return self.title
