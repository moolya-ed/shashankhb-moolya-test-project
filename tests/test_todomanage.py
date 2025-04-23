import unittest
import os
import json
import sys
'''unittest: Python’s built-in module for unit testing. You use it to write test cases, assertions, and run the test suite.

os: Used here to construct paths in a system-independent way.

json: Used to read and write JSON files (your todo list).

from src import mytodomanage: Imports the main logic file so you can test its functions.'''

# Add src to the system path so mytodomanage can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import mytodomanage  # Now directly from src/mytodomanage.py

# Get the correct path to the todos.json file
TEST_DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/todos.json')
'''Dynamically creates the path to your todos.json file.

__file__ is the path to the current test file.

os.path.dirname(__file__) → gives you the folder that test file is in.

'../data/todos.json' → navigates one level up to find the actual JSON file.

'''

class TestTodoManager(unittest.TestCase):
#This defines a test class. All functions that start with test_ inside this class will automatically be run by the test runner.


    def setUp(self):#This runs before each test. It prepares the environment so each test starts fresh.


        # Backup the original data
        with open(TEST_DATA_PATH, 'r') as f:
            self.original_data = json.load(f)
            '''Reads the existing todo list.
Stores it so you can restore it later after the test.'''

        # Use controlled test data (matching your actual todos.json structure)
        self.test_data = [
            {
                "id": "8af52e54045b423aabaa9bcf7003ff4d",
                "title": "Sample Todo Item",
                "description": "This is sample that comes with the app.You can add more looking at the swagger docs.",
                "doneStatus": False
            },
            {
                "id": "7f3d774efcad4dcbbccd891c2b121860",
                "title": "Integration Happy Path.",
                "description": "This is created using automated Integration tests.",
                "doneStatus": False
            }
        ]
        with open(TEST_DATA_PATH, 'w') as f:#Overwrites the real file with your controlled test data.
            json.dump(self.test_data, f, indent=4)

    def tearDown(self):
        # Restore the original todos.json after each test
        '''Runs after each test. resets the file to its original state.'''
        with open(TEST_DATA_PATH, 'w') as f:
            json.dump(self.original_data, f, indent=4)

    def test_load_list(self):
        todos = mytodomanage.load_list(TEST_DATA_PATH)#(TEST_DATA_PATH-Calls your actual code to load todos.


        self.assertEqual(len(todos), 2)
        self.assertEqual(todos[0]["id"], "8af52e54045b423aabaa9bcf7003ff4d")
        #Confirms there are 2 items, and the first item has the expected ID.


    def test_get_todo_details(self):
        todo = mytodomanage.get_todo_details("8af52e54045b423aabaa9bcf7003ff4d", TEST_DATA_PATH)
        #Tries to fetch a todo using a known ID.

        self.assertIsNotNone(todo)
        self.assertEqual(todo["title"], "Sample Todo Item")

    def test_update_todo(self):
        mytodomanage.update_todo("8af52e54045b423aabaa9bcf7003ff4d", {"doneStatus": True}, TEST_DATA_PATH)
        updated = mytodomanage.get_todo_details("8af52e54045b423aabaa9bcf7003ff4d", TEST_DATA_PATH)
        self.assertTrue(updated["doneStatus"])#Fetches it again and checks that the update worked.


    '''Updates": The function changes existing data — specifically, it toggles doneStatus from False to True.

"doneStatus": This is a key in the todo dictionary that indicates whether the task is completed (True) or not (False).

"of a known todo": It refers to a todo item whose ID is already present in your test dataset. In this test, it's the one with ID "8af52e54045b423aabaa9bcf7003ff4d".

In simple terms:
This test checks if your function can correctly mark a known task as "done."

'''

    def test_add_and_remove_todo(self):#Adds a new todo to the file.

        mytodomanage.add_todo("New Test", "desc", False, TEST_DATA_PATH)
        todos = mytodomanage.load_list(TEST_DATA_PATH)
        new_id = todos[-1]["id"]
        self.assertEqual(todos[-1]["title"], "New Test")
        '''Removes the todo.

Then confirms it no longer exists.

'''
        mytodomanage.remove_todo(new_id, TEST_DATA_PATH)#Confirms the new todo is added and is the last one in the list.


        updated = mytodomanage.get_todo_details(new_id, TEST_DATA_PATH)
        self.assertIsNone(updated)

if __name__ == "__main__":
    unittest.main()
