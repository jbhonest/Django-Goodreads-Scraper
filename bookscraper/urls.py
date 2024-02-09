from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import book_list, BookViewSet

book_router = DefaultRouter()
book_router.register('', BookViewSet)

urlpatterns = [
    path('', book_list, name='book_list'),
    path('api/', include(book_router.urls)),
]
