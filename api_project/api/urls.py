from django.db import router
from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router =DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    #Route for the BookList view(ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),
    #Include the router for BookViewSet(all CRUD ooperations)
    path('',include(router.urls)),#This includes all routes registered with the router
    path('auth/token/', obtain_auth_token,name='api_token_auth'),  # Token authentication endpoint
]