"""
FastAPI REST API Starter Code
Students will extend this basic template to complete the assignment tasks.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI(
    title="Item Management API",
    description="A simple REST API for managing items",
    version="1.0.0"
)

# Pydantic model for request/response validation
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    status: str = "active"

# In-memory data storage
items_db = []

# TODO: Task 1 - Add a GET endpoint that returns a welcome message

# TODO: Task 1 - Add a POST endpoint that accepts JSON and returns it with a timestamp

# TODO: Task 2 - Implement CRUD operations (GET all, GET one, POST, PUT, DELETE)

# TODO: Task 3 - Add error handling for 404 and 422 responses

# TODO: Task 4 - Add authentication middleware for protected endpoints

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
