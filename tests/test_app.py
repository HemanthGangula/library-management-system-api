import unittest
import json
from app import create_app
from models import Book, Member

class LibraryManagementSystemAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        
        # Obtain authentication token
        response = self.client.post('/auth/login', json={
            'username': 'admin',
            'password': 'password1234'
        })
        # Ensure the login was successful before proceeding
        self.assertEqual(response.status_code, 200, "Failed to log in during setup.")
        self.token = json.loads(response.data).get('token')
        self.headers = {
            'Authorization': self.token
        }

    def tearDown(self):
        # Logout after tests
        response = self.client.post('/auth/logout', json={'token': self.token})
        self.assertEqual(response.status_code, 200, "Failed to log out during teardown.")

    def test_login_logout(self):
        # Test successful login
        response = self.client.post('/auth/login', json={
            'username': 'admin',
            'password': 'password1234'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', json.loads(response.data))

        # Test logout
        token = json.loads(response.data).get('token')
        response = self.client.post('/auth/logout', json={'token': token})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['message'], 'Logged out successfully.')

    def test_add_book(self):
        response = self.client.post('/books/', headers=self.headers, json={
            'title': '1984',
            'author': 'George Orwell'
        })
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['title'], '1984')
        self.assertEqual(data['author'], 'George Orwell')

    def test_get_books(self):
        # Add a book first
        self.client.post('/books/', headers=self.headers, json={
            'title': 'To Kill a Mockingbird',
            'author': 'Harper Lee'
        })
        response = self.client.get('/books/', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertGreaterEqual(len(data['books']), 1)

    def test_update_book(self):
        # Add a book first
        add_response = self.client.post('/books/', headers=self.headers, json={
            'title': 'The Great Gatsby',
            'author': 'F. Scott Fitzgerald'
        })
        self.assertEqual(add_response.status_code, 201)
        book_id = json.loads(add_response.data)['id']
        
        # Update the book
        response = self.client.put(f'/books/{book_id}', headers=self.headers, json={
            'title': 'The Great Gatsby',
            'author': 'Francis Scott Fitzgerald'
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['author'], 'Francis Scott Fitzgerald')

    def test_delete_book(self):
        # Add a book first
        add_response = self.client.post('/books/', headers=self.headers, json={
            'title': 'Moby Dick',
            'author': 'Herman Melville'
        })
        self.assertEqual(add_response.status_code, 201)
        book_id = json.loads(add_response.data)['id']
        
        # Delete the book
        response = self.client.delete(f'/books/{book_id}', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['message'], 'Book deleted')

    def test_add_member(self):
        response = self.client.post('/members/', headers=self.headers, json={
            'name': 'John Doe',
            'email': 'john.doe@example.com'
        })
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'John Doe')
        self.assertEqual(data['email'], 'john.doe@example.com')

    def test_get_members(self):
        # Add a member first
        self.client.post('/members/', headers=self.headers, json={
            'name': 'Jane Smith',
            'email': 'jane.smith@example.com'
        })
        response = self.client.get('/members/', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertGreaterEqual(len(data), 1)

    def test_update_member(self):
        # Add a member first
        add_response = self.client.post('/members/', headers=self.headers, json={
            'name': 'Alice Johnson',
            'email': 'alice.johnson@example.com'
        })
        self.assertEqual(add_response.status_code, 201)
        member_id = json.loads(add_response.data)['id']
        
        # Update the member
        response = self.client.put(f'/members/{member_id}', headers=self.headers, json={
            'name': 'Alice J.',
            'email': 'alice.j@example.com'
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Alice J.')
        self.assertEqual(data['email'], 'alice.j@example.com')

    def test_delete_member(self):
        # Add a member first
        add_response = self.client.post('/members/', headers=self.headers, json={
            'name': 'Bob Brown',
            'email': 'bob.brown@example.com'
        })
        self.assertEqual(add_response.status_code, 201)
        member_id = json.loads(add_response.data)['id']
        
        # Delete the member
        response = self.client.delete(f'/members/{member_id}', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['message'], 'Member deleted')

    def test_protected_route_without_token(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.data)['message'], 'Token is missing.')

    def test_invalid_token(self):
        invalid_headers = {
            'Authorization': 'invalidtoken123'
        }
        response = self.client.get('/books/', headers=invalid_headers)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.data)['message'], 'Invalid or expired token.')

if __name__ == '__main__':
    unittest.main()
    