# shashankhb-moolya-test-project
learning period - MWT - 3months
1st project-todo list

# 📝 Todo Manager (Command-Line Tool)

A simple command-line based Todo Manager written in Python to help manage tasks via the terminal. It stores todo items in a JSON file and supports basic operations like add, view, update, delete, and mark as done.

---

## 🔧 Key Functions

| Function Name        | Purpose                                |
|----------------------|----------------------------------------|
| `add_todo()`         | Adds a new todo item                   |
| `view_todos()`       | Displays all existing todos            |
| `update_todo()`      | Updates title/description/status       |
| `delete_todo()`      | Deletes a todo item by ID              |
| `mark_todo_done()`   | Marks a todo item as "done"            |
| `load_todos()`       | Loads todos from the JSON file         |
| `save_todos()`       | Saves todos back to the JSON file      |

---

## 📁 File Structure

MyPythonProject/ ├── data/ │ └── todos.json ├── src/ │ └── mytodomanager.py └── README.md
note-    Make sure todos.json exists in the data/ folder. If not, the program will create it on first run.

![Flowchart](images/flowchart.png)

