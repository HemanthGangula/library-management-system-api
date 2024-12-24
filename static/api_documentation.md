# Library Management System API Documentation

Welcome to the **Library Management System API** documentation. This guide provides a comprehensive overview of all available API endpoints, including their purposes, request methods, URLs, required headers, request bodies, and example `curl` commands. Whether you're a beginner or an experienced developer, this documentation will help you understand and interact with the API effortlessly.

## Table of Contents

1. [Introduction](#introduction)
2. [Authentication](#authentication)
    - [1.1 Login](#11-login)
    - [1.2 Logout](#12-logout)
3. [Books Management](#books-management)
    - [2.1 Add a New Book](#21-add-a-new-book)
    - [2.2 Get All Books](#22-get-all-books)
    - [2.3 Get a Specific Book](#23-get-a-specific-book)
    - [2.4 Update a Book](#24-update-a-book)
    - [2.5 Delete a Book](#25-delete-a-book)
4. [Members Management](#members-management)
    - [3.1 Add a New Member](#31-add-a-new-member)
    - [3.2 Get All Members](#32-get-all-members)
    - [3.3 Get a Specific Member](#33-get-a-specific-member)
    - [3.4 Update a Member](#34-update-a-member)
    - [3.5 Delete a Member](#35-delete-a-member)
5. [Error Handling](#error-handling)
6. [Authentication Flow](#authentication-flow)
7. [Getting Started](#getting-started)
8. [Project Structure](#project-structure)
9. [Environment Variables](#environment-variables)
10. [Testing](#testing)
11. [Contributing](#contributing)
12. [License](#license)
13. [Contact](#contact)


## Introduction

The **Library Management System API** is a Flask-based backend service designed to manage a library's resources efficiently. It supports CRUD (Create, Read, Update, Delete) operations for books and members, incorporates token-based authentication for security, and provides a minimal frontend interface to demonstrate its functionalities. This API is built with a focus on correctness, clean code, and scalability, making it an excellent project for both learning and practical applications.


## Authentication

Authentication is a crucial aspect of the Library Management System API, ensuring that only authorized users can access and manipulate the library's resources. The API employs token-based authentication to secure its endpoints.

### 1.1 Login

- **Purpose:** Authenticate a user and obtain an authentication token.
- **Method:** `POST`
- **URL:** `http://localhost:5000/auth/login`
- **Headers:**
  - `Content-Type: application/json`
- **Request Body:** *(JSON)*

  ```json
  {
    "username": "admin",
    "password": "password1234"
  }
  ```

- **Example `curl` Command:**

  ```bash
  curl -X POST http://localhost:5000/auth/login \
       -H "Content-Type: application/json" \
       -d '{"username": "admin", "password": "password1234"}'
  ```

- **Expected Response:**
  - **Status Code:** `200 OK`
  - **Body:** *(JSON)*

    ```json
    {
      "token": "your-authentication-token"
    }
    ```

- **Description:**
  - Users provide their `username` and `password` to authenticate.
  - Upon successful authentication, the server responds with a unique `token` that must be included in subsequent requests to access protected endpoints.

### 1.2 Logout

- **Purpose:** Invalidate an existing authentication token.
- **Method:** `POST`
- **URL:** `http://localhost:5000/auth/logout`
- **Headers:**
  - `Content-Type: application/json`
- **Request Body:** *(JSON)*

  ```json
  {
    "token": "your-authentication-token"
  }
  ```

- **Example `curl` Command:**

  ```bash
  curl -X POST http://localhost:5000/auth/logout \
       -H "Content-Type: application/json" \
       -d '{"token": "your-authentication-token"}'
  ```

- **Expected Response:**
  - **Status Code:** `200 OK`
  - **Body:** *(JSON)*

    ```json
    {
      "message": "Logged out successfully."
    }
    ```

- **Description:**
  - Users send their current `token` to invalidate it.
  - This ensures that the token can no longer be used to access protected endpoints, enhancing security.


## Books Management

The Books Management section allows users to perform CRUD operations on the library's book collection. All endpoints in this section require authentication via the `Authorization` header containing the token.

- **Header:** `Authorization: your-authentication-token`

### 2.1 Add a New Book

- **Purpose:** Create a new book entry in the library.
- **Method:** `POST`
- **URL:** `http://localhost:5000/books/`
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: your-authentication-token`
- **Request Body:** *(JSON)*

  ```json
  {
    "title": "1984",
    "author": "George Orwell"
  }
  ```

- **Example `curl` Command:**

  ```bash
  curl -X POST http://localhost:5000/books/ \
       -H "Content-Type: application/json" \
       -H "Authorization: your-authentication-token" \
       -d '{"title": "1984", "author": "George Orwell"}'
  ```

- **Expected Response:**
  - **Status Code:** `201 Created`
  - **Body:** *(JSON)*

    ```json
    {
      "id": 1,
      "title": "1984",
      "author": "George Orwell"
    }
    ```

- **Description:**
  - Adds a new book to the library with the specified `title` and `author`.
  - The server assigns a unique `id` to the newly created book.

### 2.2 Get All Books

- **Purpose:** Retrieve a list of all books in the library.
- **Method:** `GET`
- **URL:** `http://localhost:5000/books/`
- **Headers:**
  - `Authorization: your-authentication-token`

- **Example `curl` Command:**

  ```bash
  curl -X GET http://localhost:5000/books/ \
       -H "Authorization: your-authentication-token"
  ```

- **Expected Response:**
  - **Status Code:** `200 OK`
  - **Body:** *(JSON)*

    ```json
    {
      "total": 1,
      "page": 1,
      "per_page": 10,
      "books": [
        {
          "id": 1,
          "title": "1984",
          "author": "George Orwell"
        }
      ]
    }
    ```

- **Description:**
  - Retrieves a paginated list of all books.
  - Supports pagination through query parameters (not shown in this example).

### 2.3 Get a Specific Book

- **Purpose:** Retrieve details of a specific book by its ID.
- **Method:** `GET`
- **URL:** `http://localhost:5000/books/{id}` *(Replace `{id}` with the desired book ID)*
- **Headers:**
  - `Authorization: your-authentication-token`

- **Example `curl` Command:**

  ```bash
  curl -X GET http://localhost:5000/books/1 \
       -H "Authorization: your-authentication-token"
  ```

- **Expected Response:**
  - **Status Code:** `200 OK`
  - **Body:** *(JSON)*

    ```json
    {
      "id": 1,
      "title": "1984",
      "author": "George Orwell"
    }
    ```

- **Description:**
  - Retrieves detailed information about the book with the specified `id`.

### 2.4 Update a Book

- **Purpose:** Update the details of an existing book.
- **Method:** `PUT`
- **URL:** `http://localhost:5000/books/{id}` *(Replace `{id}` with the desired book ID)*
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: your-authentication-token`
- **Request Body:** *(JSON)*

  ```json
  {
    "title": "Nineteen Eighty-Four",
    "author": "George Orwell"
  }
  ```

- **Example `curl` Command:**

  ```bash
  curl -X PUT http://localhost:5000/books/1 \
       -H "Content-Type: application/json" \
       -H "Authorization: your-authentication-token" \
       -d '{"title": "Nineteen Eighty-Four", "author": "George Orwell"}'
  ```

- **Expected Response:**
  - **Status Code:** `200 OK`
  - **Body:** *(JSON)*

    ```json
    {
      "id": 1,
      "title": "Nineteen Eighty-Four",
      "author": "George Orwell"
    }
    ```

- **Description:**
  - Updates the `title` and/or `author` of the book with the specified `id`.
  - Returns the updated book details upon success.

### 2.5 Delete a Book

- **Purpose:** Remove a book from the library.
- **Method:** `DELETE`
- **URL:** `http://localhost:5000/books/{id}` *(Replace `{id}` with the desired book ID)*
- **Headers:**
  - `Authorization: your-authentication-token`

- **Example `curl` Command:**

  ```bash
  curl -X DELETE http://localhost:5000/books/1 \
       -H "Authorization: your-authentication-token"
  ```

- **Expected Response:**
  - **Status Code:** `200 OK`
  - **Body:** *(JSON)*

    ```json
    {
      "message": "Book deleted"
    }
    ```

- **Description:**
  - Deletes the book with the specified `id` from the library.
  - Confirms deletion with a success message.


## Members Management

The Members Management section allows users to perform CRUD operations on the library's member database. All endpoints in this section require authentication via the `Authorization` header containing the token.

- **Header:** `Authorization: your-authentication-token`

### 3.1 Add a New Member

- **Purpose:** Register a new member in the library system.
- **Method:** `POST`
- **URL:** `http://localhost:5000/members/`
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: your-authentication-token`
- **Request Body:** *(JSON)*

  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

- **Example `curl` Command:**

  ```bash
  curl -X POST http://localhost:5000/members/ \
       -H "Content-Type: application/json" \
       -H "Authorization: your-authentication-token" \
       -d '{"name": "John Doe", "email": "john.doe@example.com"}'
  ```

- **Expected Response:**
  - **Status Code:** `201 Created`
  - **Body:** *(JSON)*

    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Description:**
  - Adds a new member to the library with the specified `name` and `email`.
  - The server assigns a unique `id` to the newly created member.

### 3.2 Get All Members

- **Purpose:** Retrieve a list of all library members.
- **Method:** `GET`
- **URL:** `http://localhost:5000/members/`
- **Headers:**
  - `Authorization: your-authentication-token`

- **Example `curl` Command:**

  ```bash
  curl -X GET http://localhost:5000/members/ \
       -H "Authorization: your-authentication-token"
  ```

- **Expected Response:**
  - **Status Code:** `200 OK`
  - **Body:** *(JSON)*

    ```json
    {
      "total": 1,
      "members": [
        {
          "id": 1,
          "name": "John Doe",
          "email": "john.doe@example.com"
        }
      ]
    }
    ```

- **Description:**
  - Retrieves a list of all members registered in the library.
  - Supports pagination through query parameters (not shown in this example).

### 3.3 Get a Specific Member

- **Purpose:** Retrieve details of a specific member by their ID.
- **Method:** `GET`
- **URL:** `http://localhost:5000/members/{id}` *(Replace `{id}` with the desired member ID)*
- **Headers:**
  - `Authorization: your-authentication-token`

- **Example `curl` Command:**

  ```bash
  curl -X GET http://localhost:5000/members/1 \
       -H "Authorization: your-authentication-token"
  ```

- **Expected Response:**
  - **Status Code:** `200 OK`
  - **Body:** *(JSON)*

    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Description:**
  - Retrieves detailed information about the member with the specified `id`.

### 3.4 Update a Member

- **Purpose:** Update the details of an existing library member.
- **Method:** `PUT`
- **URL:** `http://localhost:5000/members/{id}` *(Replace `{id}` with the desired member ID)*
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: your-authentication-token`
- **Request Body:** *(JSON)*

  ```json
  {
    "name": "Johnathan Doe",
    "email": "johnathan.doe@example.com"
  }
  ```

- **Example `curl` Command:**

  ```bash
  curl -X PUT http://localhost:5000/members/1 \
       -H "Content-Type: application/json" \
       -H "Authorization: your-authentication-token" \
       -d '{"name": "Johnathan Doe", "email": "johnathan.doe@example.com"}'
  ```

- **Expected Response:**
  - **Status Code:** `200 OK`
  - **Body:** *(JSON)*

    ```json
    {
      "id": 1,
      "name": "Johnathan Doe",
      "email": "johnathan.doe@example.com"
    }
    ```

- **Description:**
  - Updates the `name` and/or `email` of the member with the specified `id`.
  - Returns the updated member details upon success.

### 3.5 Delete a Member

- **Purpose:** Remove a member from the library system.
- **Method:** `DELETE`
- **URL:** `http://localhost:5000/members/{id}` *(Replace `{id}` with the desired member ID)*
- **Headers:**
  - `Authorization: your-authentication-token`

- **Example `curl` Command:**

  ```bash
  curl -X DELETE http://localhost:5000/members/1 \
       -H "Authorization: your-authentication-token"
  ```

- **Expected Response:**
  - **Status Code:** `200 OK`
  - **Body:** *(JSON)*

    ```json
    {
      "message": "Member deleted"
    }
    ```

- **Description:**
  - Deletes the member with the specified `id` from the library system.
  - Confirms deletion with a success message.


## Error Handling

The API uses standard HTTP status codes to indicate the success or failure of an API request. Below are common error responses you might encounter along with their meanings.

### 4.1 Unauthorized Access

- **Status Code:** `401 Unauthorized`
- **Condition:** Missing or invalid authentication token.
- **Response:** *(JSON)*

  ```json
  {
    "message": "Token is missing."
  }
  ```

  or

  ```json
  {
    "message": "Invalid or expired token."
  }
  ```

### 4.2 Not Found

- **Status Code:** `404 Not Found`
- **Condition:** Requested resource does not exist.
- **Response:** *(JSON)*

  ```json
  {
    "message": "Resource not found."
  }
  ```

### 4.3 Bad Request

- **Status Code:** `400 Bad Request`
- **Condition:** Invalid request data or parameters.
- **Response:** *(JSON)*

  ```json
  {
    "message": "Invalid request data."
  }
  ```

### 4.4 Internal Server Error

- **Status Code:** `500 Internal Server Error`
- **Condition:** An unexpected error occurred on the server.
- **Response:** *(JSON)*

  ```json
  {
    "message": "An unexpected error occurred."
  }
  ```

---

## Authentication Flow

Understanding the authentication flow is essential for interacting securely with the API. Below is a step-by-step guide to the authentication process.

1. **Login:**
   - **Action:** Send a `POST` request to `/auth/login` with valid `username` and `password`.
   - **Result:** Receive an authentication `token` in the response.
   
2. **Authenticated Requests:**
   - **Action:** Include the received `token` in the `Authorization` header for all protected endpoints (e.g., `/books/`, `/members/`).
   - **Header Format:** `Authorization: your-authentication-token`
   - **Result:** Access granted to perform CRUD operations on books and members.
   
3. **Logout:**
   - **Action:** Send a `POST` request to `/auth/logout` with the current `token`.
   - **Result:** Token is invalidated, and protected endpoints can no longer be accessed with it.
   
4. **Token Validation:**
   - **Action:** For each protected request, the server validates the `token`.
   - **Result:** Valid tokens allow access; invalid or missing tokens result in `401 Unauthorized` errors.


### Test Coverage

The 

test_app.py

 file contains unit tests for:

- Authentication endpoints
- Book management endpoints
- Member management endpoints
- Error handling scenarios
- Token validation
- Database operations

Each test ensures that:
- Endpoints return correct status codes
- Response data matches expected format
- Error handling works as intended
- Authentication flow functions properly
