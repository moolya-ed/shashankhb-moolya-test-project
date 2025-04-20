# Flask Message Board

This is a simple web application built with Flask and SQLite that allows users to submit messages and view previously submitted messages. The application ensures that no duplicate messages can be added.

## Features

- Submit a message to the board.
- Prevent duplicate messages from being added.
- View all previously submitted messages.
- Flash messages to notify users of actions (e.g., error or success).

## Requirements

To run this project, you need to have Python 3.x installed and the following dependencies:

- Flask
- SQLite3 (for the database)

You can install Flask using `pip`:

```bash
pip install flask

**Structure**
flask-message-board/
│
├── app.py              # Main application file
├── database.db         # SQLite database
├── templates/           # HTML templates
│   └── index.html      # Main page for submitting and viewing messages
└── README.md           # Project documentation

the url to look for frontend-http://127.0.0.1:5000/

