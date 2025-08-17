"""
Serializers for Author and Book, demonstrating:

1) A simple ModelSerializer for Book (serializes all fields).
2) A nested Author serializer that includes the author's related books using the
   BookSerializer with `many=True`.
3) Custom field-level validation on Book.publication_year to ensure it is not
   in the future.

Notes on nested serialization:
- Because Book.author uses `related_name='books'`, we can expose an author's
  books by declaring `books = BookSerializer(many=True, read_only=True)`.
- `read_only=True` means nested data is provided only on output. If you want to
  support creating/updating nested books from an Author payload, you'd override
  AuthorSerializer.create/update and handle nested write logic explicitly.
"""

from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'published_year', 'author']
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Published year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']