from bookshelf.models import Book

Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949) 

book

<Book: 1984 by George Orwell (1949)>


#Retreive
from bookshelf.models import Book

book = Book.objects.get(title="1984")

print(book.title) print(book.author) print(book.publication_year)


from bookshelf.models import Book


#Update title
book = Book.objects.get(title="1984") book.title = "Nineteen Eighty-Four" book.save()

Verify
print(book.title)

Output:
Nineteen Eighty-Four

from bookshelf.models import Book

Delete book
book = Book.objects.get(title="Nineteen Eighty-Four") book.delete()

Confirm deletion
Book.objects.all()

Output:
<QuerySet []>

