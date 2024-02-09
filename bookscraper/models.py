# bookscraper/models.py
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    author = models.CharField(max_length=255, null=False, blank=False)
    average_rating = models.FloatField(null=False, blank=False)
    cover_image_url = models.URLField(null=False, blank=False)

    def __str__(self):
        return self.title
