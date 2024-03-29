from django.contrib import admin
from .models import Book, Group


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'average_rating')
    list_display_links = ('id', 'title')
    list_filter = ('author',)
    search_fields = ('title', 'author')
    ordering = ('id',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'members')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)
