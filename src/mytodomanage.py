import json
import logging
import os
import uuid

# Setup basic logging
#logging.basicConfig(level=logging.INFO)

#save logs adn view logs- it be todo_manager.log
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("todo_manager.log")  # Only saves to a file
    ]
)


# Function to get the absolute path to the todos.json file
def get_default_todo_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "../data/todos.json")

# Function to load todos from a JSON file
def load_list(file_path=None):
    if file_path is None:
        file_path = get_default_todo_path()

    abs_path = os.path.abspath(file_path)
    print(f" Looking for file at: {abs_path}")

    if not os.path.exists(abs_path):#if no file
        logging.warning(f"File '{file_path}' not found. Returning an empty list.")
        return [] ## If loading fails and we don't return [] make it as empty list, it defaults to None → causes TypeError 'None Type' when iterating.

    #try block is used because when there is an error reading the file or decoding the JSON,Python will throw an uncaught exception
    try:
        with open(abs_path, 'r') as file:#open the file in read mode
            todos = json.load(file)#converst json into python
            logging.info(f" Loaded {len(todos)} todos from {file_path}")
            return todos
    except json.JSONDecodeError as e:
        logging.error(f" Error decoding JSON from file '{file_path}': {e}")
        return []
    except Exception as e:
        logging.error(f" An unexpected error occurred: {e}")
        return []

#Function: Save list of todos to file
def save_list(todo_list, file_path=None):#This line runs right after the
    if file_path is None:
        file_path = get_default_todo_path()

    try:
        with open(file_path, 'w') as file:
            json.dump(todo_list, file, indent=4)  # Save JSON with pretty indent
                                                  #Dumps the todo_list (a Python list of dicts) into the file as JSON.
                                                    #list of dicts-collection of dictionaries(key/value)

            logging.info(f" Saved {len(todo_list)} todos to {file_path}")
    except Exception as e:
        logging.error(f" Failed to save todos to file: {e}")#If something goes wrong (e.g., memory  error), it logs the error.

#function to update the todos
def update_todo(todo_id, updated_data, file_path=None):
    todos = load_list(file_path)#Loads all todos from the file
    updated = False #Flag to track if we successfully found and updated a todolist item.

    for todo in todos:
        if todo["id"] == todo_id:
            todo.update(updated_data)  # Update only provided fields
            updated = True
            logging.info(f" Updated todo with ID {todo_id}: {updated_data}")
            break

#above for loop works
#If it matches:
#todolist.update(updated_data) updates only the fields in the dictionary (e.g., "title" or "doneStatus").
#updated flag is set to True.
# Logs what was updated.
#Breaks the loop (don’t need to check further)

    if not updated:#If the flag is still False, that means the ID wasn’t found.
        error_message = f" Error: Todo with ID {todo_id} not found. 404 Not Found."
        print(error_message)
        logging.warning(error_message)
        return

    save_list(todos, file_path)
    print(f" Todo with ID {todo_id} has been updated.")

#function to add todolist and generate uuid
def add_todo(title, description, done_status, file_path=None):
    todos = load_list(file_path)

    new_todo = {
        "id": uuid.uuid4().hex,
        "title": title,
        "description": description,
        "doneStatus": done_status
    }

    todos.append(new_todo)
    save_list(todos, file_path)

    print(f" New todo added with ID {new_todo['id']}")
    logging.info(f" Added new todo: {new_todo}")

#Function: Save remove of todos to file
def remove_todo(todo_id, file_path=None):
    todos = load_list(file_path)
    original_count = len(todos)#Stores the original number of todos for comparison later.

    updated_todos = [todo for todo in todos if todo["id"] != todo_id]#creates a new list that contains all todos except the one with the matching todo_id

#below if condition does
#Checks if the length of the list did not change.,That means no todolist was removed, so the ID wasn't found.


    if len(updated_todos) == original_count:
        error_message = f" Error: Todo with ID {todo_id} not found. 404 Not Found."
        print(error_message)
        logging.warning(error_message)
        return

    save_list(updated_todos, file_path)#update and save
    print(f" Todo with ID {todo_id} has been removed.")
    logging.info(f" Removed todo with ID {todo_id}")


# Function to get details of a specific todolist by ID
def get_todo_details(todo_id, file_path=None):
    todos = load_list(file_path)

    for todo in todos:
        if todo["id"] == todo_id:
            logging.info(f" Found todo with ID {todo_id}")
            return todo

    error_message = f" Error: Todo with ID {todo_id} not found. 404 Not Found."
    print(error_message)
    logging.warning(error_message)
    return None

# Function to show menu to user
def show_menu():
    print("\n====== TODO MANAGER ======")
    print("1. View All Todos")
    print("2. Get Todo by ID")
    print("3. Add a New Todo")
    print("4. Remove Todo by ID")
    print("5. Update Todo by ID")
    print("6. Exit")


# Main CLI block
if __name__ == "__main__":
    print(" Welcome to the Todo Manager!")

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            todos = load_list()
            print("\n Todos:")
            for todo in todos:
                print(f" - ID: {todo['id']}")
                print(f"   Title: {todo['title']}")
                print(f"   Description: {todo.get('description', 'No description provided')}")
                print(f"   Done: {todo['doneStatus']}")


        elif choice == '2':
            todo_id = input("Enter the Todo ID: ").strip()#strip() is used to remove all unnecessary spaces
            todo = get_todo_details(todo_id)
            if todo:
                print(f"\n Todo Details:\n{json.dumps(todo, indent=4)}")

        elif choice == '3':
            title = input("Enter title: ").strip()
            description = input("Enter description: ").strip()
            done_status_input = input("Enter done status (True/False): ").strip().lower()#letter case sensitive
            done_status = done_status_input == "true"
            add_todo(title, description, done_status)

        elif choice == '4':
            todo_id = input("Enter the Todo ID to remove: ").strip()
            remove_todo(todo_id)

        elif choice == '5':
            todo_id = input("Enter the Todo ID to update: ").strip()
            field = input("Enter the field to update (e.g., title, description, doneStatus): ").strip()
            value = input("Enter the new value: ").strip()

            if field == "doneStatus":
                value = value == "True"

            update_todo(todo_id, {field: value})

        elif choice == '6':
            print("Exiting Todo Manager")
            break

        else:
            print(" Invalid choice. Please select a valid option.")
