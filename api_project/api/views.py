from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class BookList(generics.ListAPIView):
    pass
class BookViewSet(viewsets.ModelViewSet):
    """A viewset for managing books. Requires"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated to access this viewset


"""
Authentication & Permissions Setup:
- TokenAuthentication is enabled via REST_FRAMEWORK settings.
- Obtain a token by sending POST to /auth/token/ with username & password.
- Include the token in request headers as: Authorization: Token <your_token>.
- Default permission is IsAuthenticated, meaning only logged-in users with a valid token can access API endpoints.
"""

