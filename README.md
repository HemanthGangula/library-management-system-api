
# Library Management System API

A Flask-based Library Management System API supporting CRUD operations for books and members, built with a focus on correctness, clean code, and functionality. Includes features like search, pagination, and token-based authentication.

## Features

- **CRUD Operations**: Manage books and members with Create, Read, Update, and Delete functionalities.
- **Search Functionality**: Search books by title or author.
- **Pagination**: Navigate through large datasets efficiently.
- **Token-Based Authentication**: Secure API endpoints with authentication tokens.
- **Unit Testing**: Comprehensive tests to ensure API reliability and correctness.

## Built With

- [Flask](https://flask.palletsprojects.com/) - A lightweight WSGI web application framework.
- [Python](https://www.python.org/) - Programming language used.
- [Unittest](https://docs.python.org/3/library/unittest.html) - Python's built-in testing framework.

## Quick Start

1. Clone and install:
```bash
git clone https://github.com/HemanthGangula/library-management-system-api
```
activate the virtual environment
```bash
python3 -m venv venv
```
activate the environment
``` bash
source venv/bin/activate
```
Installing the requirements that are mention in the requirements.txt
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python3 app.py
```

## API Documentation

For detailed API documentation including all endpoints, authentication, request/response formats, and examples, please visit: xyz.com

## Testing

```bash
source venv/bin/activate
python3 -m unittest discover tests
```


