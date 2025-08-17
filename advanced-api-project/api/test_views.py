from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Author, Book

class BookAPITest(APITestCase):
    """
    Comprehensive test suite for Book API endpoints.
    Tests cover CRUD operations, authentication requirements, search, and ordering.
    Uses Django's login system for authentication testing as required by ALX.
    """

    def setUp(self):
        """
        Initialize test data that will be used across all test cases.
        Runs before each test method execution.
        """
        # Create test user with credentials for authentication tests
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'  # Plaintext password for test login
        )
        
        # Create test author and book as sample data
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter and the Sorcerer's Stone",
            author=self.author,
            publication_year=1997
        )
        
        # Define API endpoints
        self.list_create_url = '/api/books/'  # List and create endpoint
        self.detail_url = f'/api/books/{self.book.pk}/'  # Detail view endpoint

    def test_list_books_unauthenticated(self):
        """
        Verify unauthenticated users can access the book listing.
        Should return HTTP 200 and all books.
        """
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should see our test book

    def test_retrieve_book_unauthenticated(self):
        """
        Verify unauthenticated users can view individual book details.
        Should return HTTP 200 with correct book data.
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_create_book_authenticated(self):
        """
        Verify authenticated users can create new books.
        Uses Django's login() instead of force_authenticate() for proper auth testing.
        """
        new_book_data = {
            'title': 'The Hobbit',
            'author': self.author.pk,
            'publication_year': 1937
        }
        
        # Authenticate using Django's login system (required by ALX)
        login_success = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(login_success)  # Verify login worked
        
        response = self.client.post(self.list_create_url, new_book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Original + new book
        
        self.client.logout()  # Clean up authentication

    def test_create_book_unauthenticated_fails(self):
        """
        Verify unauthenticated users cannot create books.
        Should return HTTP 403 Forbidden.
        """
        new_book_data = {
            'title': 'The Hobbit',
            'author': self.author.pk,
            'publication_year': 1937
        }
        
        response = self.client.post(self.list_create_url, new_book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Book.objects.count(), 1)  # No new book created

    def test_update_book_authenticated(self):
        """
        Verify authenticated users can update existing books.
        Uses the non-standard update endpoint with PUT method.
        """
        updated_data = {
            'pk': self.book.pk,
            'title': 'Harry Potter and the Philosopher\'s Stone',
            'author': self.author.pk,
            'publication_year': 1997
        }
        
        # Authenticate properly with login()
        self.client.login(username='testuser', password='testpassword')
        
        response = self.client.put('/api/books/update/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify the book was actually updated
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, updated_data['title'])
        
        self.client.logout()

    def test_delete_book_authenticated(self):
        """
        Verify authenticated users can delete books.
        Uses the non-standard delete endpoint with DELETE method.
        """
        delete_data = {'pk': self.book.pk}
        
        # Authenticate with login() as required
        self.client.login(username='testuser', password='testpassword')
        
        response = self.client.delete('/api/books/delete/', delete_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  # Book should be deleted
        
        self.client.logout()

    def test_search_books_by_title(self):
        """
        Verify the search functionality filters books by title.
        """
        response = self.client.get(self.list_create_url, {'search': 'Harry'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book.title)

    def test_search_books_by_author_name(self):
        """
        Verify the search functionality filters books by author name.
        """
        response = self.client.get(self.list_create_url, {'search': 'Rowling'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        """
        Verify the ordering functionality works by publication year.
        """
        # Add a second book for ordering tests
        Book.objects.create(
            title="Fantastic Beasts and Where to Find Them",
            author=self.author,
            publication_year=2001
        )
        
        # Test descending order
        response = self.client.get(self.list_create_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify order is correct
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, [
            "Fantastic Beasts and Where to Find Them",
            "Harry Potter and the Sorcerer's Stone"
        ])