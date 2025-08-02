from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import permission_required, login_required
from .models import Book

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
