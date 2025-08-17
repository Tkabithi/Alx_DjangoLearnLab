from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# ListBooksView:    GET all books
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# BookDetailView:   GET single book by ID   
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#CreateBookView:   POST a new book
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save()

# UpdateBookView:   PUT/PATCH update an existing book 
class UpdateView(generics.UpdateAPIView):
    queryset = Book.object.all()
    serializer_class =BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_update(self, serializer):
        serializer.save()

 #   DeleteBookView:   DELETE an existing book
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]