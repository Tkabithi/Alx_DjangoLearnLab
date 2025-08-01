from .models import Author, Book, Library, Librarian    

def get_books_by_author(author_name):
    """
    Retrieve all books written by a specific author.
    """
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return [Book.objects.none()]
   
  
        
def get_all_books_in_library(library_name):
    """
    Retrieve all books available in a specific library.
    """
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return [library.books.none()]
    
    
def get_librarian_for_library(library_name):
    """
    Retrieve the librarian responsible for a specific library.
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return library.librarian
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return None

