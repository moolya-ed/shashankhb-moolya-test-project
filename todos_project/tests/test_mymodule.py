import unittest
from unittest.mock import patch, mock_open
#Imports tools for mocking (patch replaces functions or objects during tests; mock_open simulates file operations).
import json
import sys
import os

# Add src/ to path so we can import mytodomanage
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import mytodomanage


class TestTodoManager(unittest.TestCase):
    #TestTodoManager is a test class.,It inherits all the methods and functionality from unittest.TestCase, which is the base class for writing tests.

#In unittest, setUp() is a special method that runs before each individual test method in your test class. It’s used to prepare common test data or state, so you don’t have to repeat setup code in every test.
#self-refers to the instance of the test class, which is typically a subclass of unittest.TestCase
#mock_file is a mock object created by the patch() decorator applied to builtins.open.
#mock_input is a mock object that simulates the behavior of the input() function.
    def setUp(self):
        self.sample_todos = [
            {"id": "1", "title": "Task 1", "description": "Desc 1", "doneStatus": False},
            {"id": "2", "title": "Task 2", "description": "Desc 2", "doneStatus": True}
        ]#Initializes a list of sample to-do items used in various tests.

#Mocks file reading and path existence check. read_data='[]' simulates an empty to-do list in the file.
    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    @patch("os.path.exists", return_value=True)
    def test_load_todos(self, mock_exists, mock_file):
        todos = mytodomanage.load_todos()
        self.assertEqual(todos, [])#Calls the function and checks if it returns an empty list as expected.

    @patch("builtins.open", new_callable=mock_open)#Mocks the open function to prevent real file writing.
    #Checks that writing to a file was attempted when saving todos.
    def test_save_todos(self, mock_file):
        mytodomanage.save_todos(self.sample_todos)
        mock_file().write.assert_called()

    @patch("builtins.input", side_effect=["New Title", "New Description"])
    @patch("builtins.open", new_callable=mock_open)
    def test_add_todo(self, mock_file, mock_input):
        '''@patch("builtins.input", side_effect=["New Title", "New Description"]): Mocks the input() function to simulate user input. The user will enter "New Title" and "New Description" when prompted.

@patch("builtins.open", new_callable=mock_open): Mocks the open() function to simulate file operations, but without actually writing to a file.'''
        '''Initializes an empty list todos.

Calls add_todo() to add a new to-do to the list. The input() function is mocked to return the title and description that will be used for the new to-do.

Asserts that the length of the todos list is now 1 (meaning one to-do was added).

Verifies that the title of the newly added to-do is "New Title". and New Discription'''
        todos = []
        mytodomanage.add_todo(todos)
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0]["title"], "New Title")
        self.assertEqual(todos[0]["description"], "New Description")  # Verify the description

#@patch("builtins.input", side_effect=["1"]): Mocks the input() function to simulate the user entering "1", selecting the to-do with ID "1".
# with patch("builtins.print") as mock_print:: Mocks the print() function to capture output, ensuring the get_todo() function prints the selected to-do information.
#Calls get_todo() with self.sample_todos as the argument.

#Verifies that print() was called, meaning the to-do information was printed (the function shows details of the selected to-do).

    @patch("builtins.input", side_effect=["1"])
    def test_get_todo(self, mock_input):#The self argument refers to the instance of the test class (which likely inherits from unittest.TestCase).
        with patch("builtins.print") as mock_print:
            mytodomanage.get_todo(self.sample_todos)
            mock_print.assert_called()#as mock_print assigns the mock object to the variable mock_print, which you can later use to make assertions about how the print() function was used.
            #assert_called() is an assertion that verifies the mock print() function was called at least once. This ensures that some output (probably related to the to-do item) was printed, which indicates that the get_todo() function attempted to display or log some information.
    @patch("builtins.input", side_effect=["1", "Updated Title", "Updated Description"])
    @patch("builtins.open", new_callable=mock_open)
    def test_update_todo(self, mock_file, mock_input):#    Mocks the open() function, simulating the file operations involved in updating the to-do list.
        mytodomanage.update_todo(self.sample_todos)
        self.assertEqual(self.sample_todos[0]["title"], "Updated Title")
        self.assertEqual(self.sample_todos[0]["description"], "Updated Description")

    @patch("builtins.input", side_effect=["1"])
    @patch("builtins.open", new_callable=mock_open)
    def test_remove_todo(self, mock_file, mock_input):
        mytodomanage.remove_todo(self.sample_todos)
        self.assertEqual(len(self.sample_todos), 1)
        self.assertEqual(self.sample_todos[0]["id"], "2")# # after removing 1st iud ,The first item should now have ID "2"


if __name__ == '__main__':
    unittest.main()


