from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookscraper/books_list.html', {'books': books})
