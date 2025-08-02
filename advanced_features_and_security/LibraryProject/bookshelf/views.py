from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import permission_required, login_required
from .models import Book
from .forms import ExampleForm

from django.db.models import Q  # Import Q for complex lookups

@permission_required('bookshelf.view_book', raise_exception=True)
@login_required
def book_list(request):
    query = request.GET.get('q')  # Get the search term from query parameters
    if query:
        # Safe ORM filtering using Q objects
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    else:
        books = Book.objects.all()
        
    return render(request, "relationship_app/book_list.html", {'books': books, 'query': query})


@permission_required('relationship_app.can_add_book',raise_exception=True) 
def add_book(request):
    if request .method == 'POST':
        title =request.POST.get('title')
        author_id=request.POST.get('author_id')
        publication_year = request.POST.get('publication_year')
        if title and author_id and publication_year:
            book = Book(title=title, author_id=author_id, publication_year=publication_year)
            book.save()
            return redirect('list_books')
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request,book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author_id = request.POST.get('author_id')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('list_books')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request,book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
