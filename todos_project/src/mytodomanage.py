# Copyright (c) 2025 Shashank
# You may not copy, modify, distribute, or use this code for any purpose without express written permission from the author.

import json
import uuid
import os
import logging

FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "todos.json")
FILE_PATH = os.path.abspath(FILE_PATH)

LOG_FILE = "todo_manager.log"

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_todos():
    """Load todos from the JSON file"""
    if not os.path.exists(FILE_PATH):
        logging.warning("Todo file not found. Creating a new one.")
        return []
    with open(FILE_PATH, "r") as f:
        todos = json.load(f)
    logging.info("Todos loaded successfully.")
    return todos

def save_todos(todos):
    """Save todos back to the JSON file"""
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    with open(FILE_PATH, "w") as f:
        json.dump(todos, f, indent=4)
    logging.info("Todos saved successfully.")

def display_todos(todos, message=" Current Todos:"):
    """Display todos to the console"""
    print(f"\n{message}")
    print(json.dumps(todos, indent=4))

def add_todo(todos):
    """Add a new Todo to the list"""
    print("Adding a Todo...")
    title = input("Enter title: ")
    description = input("Enter description: ")
    new_todo = {
        "id": uuid.uuid4().hex,  # Automatically generate a new ID
        "title": title,
        "description": description,
        "doneStatus": False  # Default value is False
    }
    todos.append(new_todo)
    display_todos(todos, " Updated Todos after addition:")
    save_todos(todos)
    print("Todos have been saved.")
    logging.info(f"Added new todo: {new_todo['id']}")

def get_todo(todos):
    """Get a specific todo by its ID"""
    print(" Viewing a Todo...")
    while True:
        id_to_view = input("Enter ID of the todo to view: ").strip()
        for todo in todos:
            if todo["id"] == id_to_view:
                print(json.dumps(todo, indent=4))
                logging.info(f"Viewed todo: {id_to_view}")
                return
        print(" Invalid ID. Kindly enter a valid one.")

def update_todo(todos):
    """Update an existing todo by ID"""
    print("Updating a Todo...")
    while True:
        id_to_update = input("Enter ID of the todo to update: ").strip()
        for todo in todos:
            if todo["id"] == id_to_update:
                title = input("Enter new title: ")
                description = input("Enter new description: ")
                status_input = input("Enter new status (True/False): ").strip().lower()

                # Convert input to boolean
                done_status = status_input == "true"

                todo["title"] = title
                todo["description"] = description
                todo["doneStatus"] = done_status

                display_todos(todos, " Updated Todos after update:")
                save_todos(todos)
                print(" Todos have been saved.")
                logging.info(f"Updated todo: {id_to_update}")
                return
        print(" Invalid ID. Kindly enter a valid one.")


def remove_todo(todos):
    """Remove a todo from the list by ID"""
    print("Removing a Todo...")
    while True:
        id_to_remove = input("Enter ID of the todo to remove: ").strip()
        for i, todo in enumerate(todos):
            if todo["id"] == id_to_remove:
                removed = todos.pop(i)
                display_todos(todos, " Updated Todos after removal:")
                save_todos(todos)
                print(" Todos have been saved.")
                logging.info(f"Removed todo: {id_to_remove}")
                return
        print(" Invalid ID. Kindly enter a valid one.")

if __name__ == "__main__":
    """Main execution for adding, viewing, updating, and removing todos"""
    print("=== TODO MANAGER EXECUTION ===")
    print("1️Loading Todos...\n")
    todos = load_todos()
    display_todos(todos)

    add_todo(todos)
    get_todo(todos)
    update_todo(todos)
    remove_todo(todos)

    # Final save and display
    save_todos(todos)
    display_todos(todos, "\n Final Todos after all operations:")

