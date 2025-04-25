from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
import uuid
import json
import os

# FastAPI instance
app = FastAPI()

# File path for storing todos
FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "todos.json")
FILE_PATH = os.path.abspath(FILE_PATH)

# Enable CORS (for frontend or Postman use)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Define the data model
class Todo(BaseModel):
    title: str
    description: str
    doneStatus: bool = False
    id: Optional[str] = Field(default=None)

# Load todos from JSON file
def load_todos():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)

# Save todos to JSON file
def save_todos(todos):
    with open(FILE_PATH, "w") as f:
        json.dump(todos, f, indent=4)

# Home route
@app.get("/")
def read_root():
    return {"message": "✅ API is running!"}

# 1️⃣ Get all todos
@app.get("/todos")
def get_all_todos():
    return load_todos()

# 2️⃣ Get one todo by ID
@app.get("/todo/{todo_id}")
def get_todo(todo_id: str):
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# 3️⃣ Add a new todo
@app.post("/add_todo")
def add_todo(todo: Todo):
    todos = load_todos()
    for existing in todos:
        if existing["title"] == todo.title and existing["description"] == todo.description:
            raise HTTPException(status_code=400, detail="Todo with the same title and description already exists.")
    todo.id = todo.id or uuid.uuid4().hex
    todos.append(todo.dict())
    save_todos(todos)
    return {"message": "Todo added successfully", "todo": todo}

# 4️⃣ Update an existing todo
@app.put("/update_todo/{todo_id}")
def update_todo(todo_id: str, updated: Todo):
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["title"] = updated.title
            todo["description"] = updated.description
            todo["doneStatus"] = updated.doneStatus
            save_todos(todos)
            return {"message": "Todo updated", "todo": todo}
    raise HTTPException(status_code=404, detail="Todo not found")

# 5️⃣ Delete a todo
@app.delete("/remove_todo/{todo_id}")
def delete_todo(todo_id: str):
    todos = load_todos()
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            removed = todos.pop(i)
            save_todos(todos)
            return {"message": "Todo deleted", "todo": removed}
    raise HTTPException(status_code=404, detail="Todo not found")
