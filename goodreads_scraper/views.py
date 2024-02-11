from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Book, Group
from .serializers import BookSerializer, GroupSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('author',)
    search_fields = ('title', 'author')


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    search_fields = ('title',)


def book_list(request):
    books = Book.objects.all()
    return render(request, 'goodreads_scraper/books_list.html', {'books': books})


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'goodreads_scraper/groups_list.html', {'groups': groups})
