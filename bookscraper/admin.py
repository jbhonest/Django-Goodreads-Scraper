from django.contrib import admin
from .models import Book, Group


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'average_rating')
    list_filter = ('author',)
    search_fields = ('title', 'author')
    ordering = ('id',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'members')
    search_fields = ('title',)
    ordering = ('id',)
