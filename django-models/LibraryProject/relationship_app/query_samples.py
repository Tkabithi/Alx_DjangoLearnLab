from .models import Author, Book, Library, Librarian    

def get_books_by_author(author_name):
    """
    Retrieve all books written by a specific author.
    """
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
    except Author.DoesNotExist:
        return [Book.objects.none()]
    
def get_books_in_library(library_name):
    """
    Retrieve all books available in a specific library.
    """
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []
    
def get_librarian_for_library(library_name):
    """
    Retrieve the librarian responsible for a specific library.
    """
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return None

