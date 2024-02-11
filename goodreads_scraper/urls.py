from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import book_list, group_list, BookViewSet, GroupViewSet

book_router = DefaultRouter()
book_router.register('', BookViewSet)

group_router = DefaultRouter()
group_router.register('', GroupViewSet)

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('groups/', group_list, name='group_list'),
    path('api/books/', include(book_router.urls)),
    path('api/groups/', include(group_router.urls)),
]
