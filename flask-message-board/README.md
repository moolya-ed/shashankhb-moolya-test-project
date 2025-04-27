Flask Message Board
This is a simple web application built using Flask and SQLite that allows users to submit messages and view previously submitted ones. The application ensures that no duplicate messages are added, offering a simple interface to interact with.
Features
- Submit a message to the board: Users can add a message to the board.
- Prevent duplicate messages: The application checks for and prevents the submission of duplicate messages.
- View all previously submitted messages: Users can view all the messages that have been submitted so far.
- Flash messages: Inform users of success or error actions (e.g., successful submission or duplicate message detection).
Requirements
To run this project, you need to have **Python 3.x** installed. The following dependencies are required:

- **Flask**: The web framework used to build the application.
- **SQLite3**: Used for the database to store the messages.

You can install Flask using pip:

```bash
pip install flask
```
SQLite3 should be installed by default with Python. If not, you can install it based on your environment.
Setup
1. Clone the repository:

```bash
git clone https://github.com/your-username/flask-message-board.git
cd flask-message-board
```

2. Install dependencies:

Make sure you have Flask installed. You can use a virtual environment for better project isolation:

```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
pip install flask
```

3. Run the application:

In the project directory, run the Flask application:

```bash
python app.py
```

4. Access the application:

Once the app is running, visit `http://127.0.0.1:5000/` in your browser to interact with the message board.
Project Structure
The project has the following structure:

```
flask-message-board/
│
├── app.py              # Main application file
├── database.db         # SQLite database
├── templates/           # HTML templates
│   └── index.html      # Main page for submitting and viewing messages
└── README.md           # Project documentation
```

- **app.py**: Contains the main Flask application and route definitions.
- **database.db**: The SQLite database file that stores the messages.
- **templates/index.html**: The HTML page for the user interface (UI), where users can submit and view messages.
- **README.md**: This documentation file.
How It Works
- **Submission of Messages**: When a user submits a message, it is checked against the database for duplicates. If the message already exists, an error flash message is shown. Otherwise, the message is added to the database and a success flash message is shown.
- **Viewing Messages**: The submitted messages are retrieved from the SQLite database and displayed on the main page.
- **Duplicate Prevention**: The application uses simple logic to compare new submissions against existing messages to avoid duplicates.
URL to Access Frontend
You can access the frontend of the application by visiting the following URL:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)
License
This project is open-source and available under the MIT License.
Contributions
Feel free to fork this project, submit issues, or create pull requests if you'd like to contribute to the project.
