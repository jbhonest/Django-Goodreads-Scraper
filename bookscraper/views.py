from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('author',)
    search_fields = ('title', 'author')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookscraper/books_list.html', {'books': books})
