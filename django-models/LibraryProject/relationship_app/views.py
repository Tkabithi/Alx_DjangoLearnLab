from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Added Library import here

# Function-based view that lists all books
def list_books(request):
    """Function-based view to list all books"""
    books = Book.objects.all()
    return render(
        request, 
        'relationship_app/list_books.html',
        {'books': books}
    )

# Class-based view that shows library details
class LibraryDetailView(DetailView):
    """Class-based view to show library details"""
    model = Library  # This requires the Library import
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'