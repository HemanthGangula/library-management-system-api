from flask import Blueprint, request, jsonify
from typing import List, Optional
from models import Book
from utils.auth_decorator import token_required

bp = Blueprint('books', __name__, url_prefix='/books')

# In-memory storage for books
books: List[Book] = []

@bp.route('/', methods=['GET'])
@token_required
def get_books() -> jsonify:
    title: Optional[str] = request.args.get('title')
    author: Optional[str] = request.args.get('author')
    page: int = int(request.args.get('page', 1))
    per_page: int = int(request.args.get('per_page', 10))
    
    filtered_books: List[dict] = [
        book.__dict__ for book in books
        if (title.lower() in book.title.lower() if title else True) and
           (author.lower() in book.author.lower() if author else True)
    ]
    
    total: int = len(filtered_books)
    start: int = (page - 1) * per_page
    end: int = start + per_page
    paginated_books: List[dict] = filtered_books[start:end]
    
    return jsonify({
        'total': total,
        'page': page,
        'per_page': per_page,
        'books': paginated_books
    }), 200

@bp.route('/', methods=['POST'])
@token_required
def add_book() -> jsonify:
    data = request.get_json()
    if not data.get('title') or not data.get('author'):
        return jsonify({'message': 'Title and author are required.'}), 400
    book = Book(
        id=len(books) + 1,
        title=data.get('title'),
        author=data.get('author')
    )
    books.append(book)
    return jsonify(book.__dict__), 201

@bp.route('/<int:book_id>', methods=['GET'])
@token_required
def get_book(book_id: int) -> jsonify:
    book: Optional[Book] = next((b for b in books if b.id == book_id), None)
    if book:
        return jsonify(book.__dict__), 200
    return jsonify({'message': 'Book not found'}), 404

@bp.route('/<int:book_id>', methods=['PUT'])
@token_required
def update_book(book_id: int) -> jsonify:
    data = request.get_json()
    book: Optional[Book] = next((b for b in books if b.id == book_id), None)
    if book:
        book.title = data.get('title', book.title)
        book.author = data.get('author', book.author)
        return jsonify(book.__dict__), 200
    return jsonify({'message': 'Book not found'}), 404

@bp.route('/<int:book_id>', methods=['DELETE'])
@token_required
def delete_book(book_id: int) -> jsonify:
    global books
    books = [b for b in books if b.id != book_id]
    return jsonify({'message': 'Book deleted'}), 200