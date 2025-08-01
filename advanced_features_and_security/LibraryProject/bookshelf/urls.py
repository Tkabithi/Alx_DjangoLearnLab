from django.urls import path
from . import views  # Import your views

app_name = 'bookshelf'  # Optional namespace

urlpatterns = [
    path('', views.book_list, name='list_books'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]