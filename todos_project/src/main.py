from fastapi import FastAPI, HTTPException  # Import FastAPI framework and HTTP error handling
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
from pydantic import BaseModel, Field  # For request validation
from typing import Optional  # Allow optional fields in models
import uuid  # Used to generate unique IDs
import json  # Used for file I/O
import os  # Used for file path operations

# Create FastAPI instance
app = FastAPI()

# Set file path to JSON file storing todos
FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "todos.json")
FILE_PATH = os.path.abspath(FILE_PATH)  # Convert to absolute path

# Enable CORS to allow frontend or external tools like Postman to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"]  # Allow all headers
)

# Define data model using Pydantic for validation
class Todo(BaseModel):
    title: str  # Title is required
    description: str  # Description is required
    doneStatus: bool = False  # Default status is False
    id: Optional[str] = Field(default=None)  # ID is optional; generated if not provided

# Load todos from file
def load_todos():
    if not os.path.exists(FILE_PATH):  # If file doesn't exist, return empty list
        return []
    with open(FILE_PATH, "r") as f:  # Open file in read mode
        return json.load(f)  # Return loaded list

# Save todos to file
def save_todos(todos):
    print("Saving todos:", todos)  # Debug print for visibility
    with open(FILE_PATH, "w") as f:  # Open file in write mode
        json.dump(todos, f, indent=4)  # Save todos as pretty JSON

# Home route to verify API is running
@app.get("/")
def read_root():
    return {"message": "✅ API is running!"}  # Health check

# Get all todos
@app.get("/todos")
def get_all_todos():
    return load_todos()  # Return list of todos

# Get a single todo by ID
@app.get("/todo/{todo_id}")
def get_todo(todo_id: str):
    todos = load_todos()  # Load all todos
    for todo in todos:
        if todo["id"] == todo_id:  # Match by ID
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")  # If not found

# Add a new todo
@app.post("/add_todo")
def add_todo(todo: Todo):
    todos = load_todos()
    # Check for duplicate todo by title and description
    for existing in todos:
        if existing["title"] == todo.title and existing["description"] == todo.description:
            raise HTTPException(status_code=400, detail="Todo with the same title and description already exists.")
    todo.id = todo.id or uuid.uuid4().hex  # Generate ID if not provided
    todos.append(todo.dict())  # Add to list as dict
    save_todos(todos)  # Save to file
    return {"message": "Todo added successfully", "todo": todo}  # Return response

# Update existing todo
@app.put("/update_todo/{todo_id}")
def update_todo(todo_id: str, updated: Todo):
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:  # Match by ID
            # Update fields
            todo["title"] = updated.title
            todo["description"] = updated.description
            todo["doneStatus"] = updated.doneStatus
            save_todos(todos)  # Save updated list
            return {"message": "Todo updated", "todo": todo}
    raise HTTPException(status_code=404, detail="Todo not found")  # If not found

# Delete a todo
@app.delete("/remove_todo/{todo_id}")
def delete_todo(todo_id: str):
    todos = load_todos()
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:  # Match by ID
            removed = todos.pop(i)  # Remove from list
            save_todos(todos)  # Save changes
            return {"message": "Todo deleted", "todo": removed}  # Return removed item
    raise HTTPException(status_code=404, detail="Todo not found")  # If not found

