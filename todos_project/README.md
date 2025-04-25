shashankhb-MWt-project/
├── frontend/
│   └── index.html       # Basic HTML file for the frontend (not fully implemented)
├── src/
│   ├── todomanage.py    # Core functions for managing todos
│   ├── main.py          # FastAPI backend (API routes for todo operations)
│   └── todo-manager.log # Log file for application logs
├── tests/
│   └── test_mymodule.py # Unit tests for the core functions
└── data/
    └── todos.json       # JSON file storing todos


Setup and Installation
Prerequisites

    Python 3.x: Ensure you have Python 3.x installed. You can verify this by running:

python3 --version

Virtual Environment: It is recommended to set up a virtual environment to manage dependencies.

    To create a virtual environment:

python3 -m venv .venv

Activate the virtual environment:

    On Linux/Mac:

source .venv/bin/activate

On Windows:

        .venv\Scripts\activate

Install Dependencies: If you have a requirements.txt file (or similar), install the dependencies:

pip install -r requirements.txt

If no dependencies are listed yet, you can manually install FastAPI and Uvicorn (for the backend API):

    pip install fastapi uvicorn

Running the Application

    CLI Tool: The project includes a command-line tool (src/todomanage.py) that allows you to manage your todos. You can use it to interact with the todo list via the terminal.

    Example commands:

        To add a todo:

python src/todomanage.py add "New Task" "Description of the task"

To view all todos:

python src/todomanage.py view

To update a todo:

    python src/todomanage.py update <todo_id> "Updated Task" "Updated Description"

FastAPI Backend: The backend API allows you to interact with the todo list using HTTP requests. The main API file is src/main.py.

    To run the FastAPI server:

        uvicorn src.main:app --reload

    This will start the server at http://127.0.0.1:8000.

        Endpoints available:

            GET /todos: Get all todos.

            GET /todos/{id}: Get a specific todo by ID.

            POST /todos: Add a new todo.

            PUT /todos/{id}: Update an existing todo.

            DELETE /todos/{id}: Delete a todo by ID.

Accessing the Todo List

Your todo list is stored in a JSON file (data/todos.json), where each todo is represented as a JSON object with fields like id, title, description, and doneStatus.

The file is updated whenever you add, update, or delete todos via the CLI or API.
Functionality
Core Functions in todomanage.py

This file contains all the core functions that manage the todo list. They are used by both the CLI and FastAPI backend.

    add_todo(new_id, new_todo, done_status): Adds a new todo to the list with the given ID, title, description, and done status.

    update_todo(todo_id, updated_todo, updated_description): Updates an existing todo based on its ID.

    remove_todo(todo_id): Removes a todo from the list by its ID.

    get_todo(todo_id): Retrieves a specific todo by its ID.

    load_todos(): Loads the todo list from the JSON file.

    save_todos(todos): Saves the updated todo list to the JSON file.

FastAPI Endpoints in main.py

This file contains the API routes for the backend:

    GET /todos: Returns a list of all todos.

    GET /todos/{id}: Retrieves a specific todo by its ID.

    POST /todos: Adds a new todo.

    PUT /todos/{id}: Updates an existing todo.

    DELETE /todos/{id}: Deletes a todo by its ID.

Testing

Unit tests are written for the core functions using Python's unittest framework and are located in the tests folder.

    To run the tests:

    python -m unittest discover tests

Contributing

Feel free to fork the repository and make contributions. If you have any suggestions or improvements, please create an issue or submit a pull request.
License

This project is licensed under the @shashank License - see the LICENSE file for details.

