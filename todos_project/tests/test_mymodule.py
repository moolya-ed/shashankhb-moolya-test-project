import unittest
from unittest.mock import patch, mock_open
import json
import sys
import os

# Add src/ to path so we can import mytodomanage
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mypythonproject', 'src')))

import mytodomanage


class TestTodoManager(unittest.TestCase):

    def setUp(self):
        self.sample_todos = [
            {"id": "1", "title": "Task 1", "description": "Desc 1", "doneStatus": False},
            {"id": "2", "title": "Task 2", "description": "Desc 2", "doneStatus": True}
        ]

    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    @patch("os.path.exists", return_value=True)
    def test_load_todos(self, mock_exists, mock_file):
        todos = mytodomanage.load_todos()
        self.assertEqual(todos, [])

    @patch("builtins.open", new_callable=mock_open)
    def test_save_todos(self, mock_file):
        mytodomanage.save_todos(self.sample_todos)
        mock_file().write.assert_called()

    @patch("builtins.input", side_effect=["New Title", "New Description"])
    @patch("builtins.open", new_callable=mock_open)
    def test_add_todo(self, mock_file, mock_input):
        todos = []
        mytodomanage.add_todo(todos)
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0]["title"], "New Title")

    @patch("builtins.input", side_effect=["1"])
    def test_get_todo(self, mock_input):
        with patch("builtins.print") as mock_print:
            mytodomanage.get_todo(self.sample_todos)
            mock_print.assert_called()

    @patch("builtins.input", side_effect=["1", "Updated Title", "Updated Description"])
    @patch("builtins.open", new_callable=mock_open)
    def test_update_todo(self, mock_file, mock_input):
        mytodomanage.update_todo(self.sample_todos)
        self.assertEqual(self.sample_todos[0]["title"], "Updated Title")

    @patch("builtins.input", side_effect=["1"])
    @patch("builtins.open", new_callable=mock_open)
    def test_remove_todo(self, mock_file, mock_input):
        mytodomanage.remove_todo(self.sample_todos)
        self.assertEqual(len(self.sample_todos), 1)
        self.assertEqual(self.sample_todos[0]["id"], "2")


if __name__ == '__main__':
    unittest.main()
