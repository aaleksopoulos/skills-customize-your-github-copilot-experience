# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a complete RESTful API using the FastAPI framework. You'll create endpoints for managing resources, implement data validation, handle errors gracefully, and explore advanced features. This assignment teaches you how to structure modern Python web APIs.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI project with the provided starter code and extend it to create your first custom endpoints. You'll learn the basics of routing, HTTP methods, and request/response handling.

#### Requirements
Completed program should:

- Import FastAPI and run the application using Uvicorn
- Create a GET endpoint that returns a welcome message
- Create a POST endpoint that accepts JSON data and returns it with a timestamp
- Test both endpoints using the interactive API documentation at `/docs`

### 🛠️ Implement CRUD Operations for a Resource

#### Description
Build a complete CRUD (Create, Read, Update, Delete) API for managing a collection of items. Use an in-memory list or database to store data, and implement all four HTTP methods.

#### Requirements
Completed program should:

- Implement GET /items to retrieve all items
- Implement GET /items/{item_id} to retrieve a specific item
- Implement POST /items to create a new item
- Implement PUT /items/{item_id} to update an existing item
- Implement DELETE /items/{item_id} to delete an item
- Use appropriate HTTP status codes (200, 201, 404, etc.)

### 🛠️ Add Data Validation and Error Handling

#### Description
Enhance your API with Pydantic models for data validation and implement proper error handling. This ensures your API rejects invalid data and returns meaningful error messages.

#### Requirements
Completed program should:

- Define Pydantic models for request/response data
- Validate all incoming data automatically
- Return a 422 status code with clear error details for invalid data
- Implement a 404 response when an item is not found
- Return a 500 error with a generic message for unexpected errors

### 🛠️ Add Authentication and Advanced Features (Stretch Goal)

#### Description
Implement basic authentication to control access to your API and add filtering/pagination capabilities. This prepares you for real-world API security.

#### Requirements
Completed program should:

- Implement a simple API key authentication system
- Protect at least the DELETE endpoint with authentication
- Add optional query parameters for filtering items (e.g., by status or category)
- Implement pagination with limit and offset parameters
- Document all new endpoints in the OpenAPI schema
