from flask import Flask, render_template, request, redirect, flash
import sqlite3

'''Flask: This creates your web application.

render_template: Used to load HTML files.

request: Used to access form data sent by the user.

redirect: Sends the user to another route (like /).

sqlite3: Python’s built-in library to interact with SQLite databases.
'''

# This line initializes your Flask app and tells Python that this file will run your web server.
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for flash messages to work


# Initialize database (run only once when app starts)
def init_db():
    try:
        conn = sqlite3.connect('database.db')  # Connect to database or create it if not exists
        c = conn.cursor()  # Create a cursor object to run SQL queries
        c.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, content TEXT)')
        # This creates a table named 'messages' with columns: id and content

        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        flash('Database error occurred while initializing.')


@app.route('/')
def index():
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('SELECT * FROM messages')
        messages = c.fetchall()
        conn.close()
        return render_template('index.html', messages=messages)
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        flash('Error retrieving messages from the database.')
        return render_template('index.html', messages=[])


@app.route('/add', methods=['POST'])
def add():
    try:
        # Access the submitted form data using the 'content' key
        content = request.form['content']  # This will raise KeyError if 'content' is missing
        print(f"Received content: {content}")  # Debugging: print what the user submitted

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # Check if the message already exists
        c.execute('SELECT * FROM messages WHERE content = ?', (content,))
        existing_message = c.fetchone()  # Fetch row, if it exists

        if existing_message:
            flash('Kindly enter new input. This message already exists.')  # Flash a message to user
        else:
            c.execute('INSERT INTO messages (content) VALUES (?)', (content,))
            conn.commit()

        conn.close()
        return redirect('/')  # Redirect the user to the home page

    except KeyError:
        print("Form field 'content' is missing.")  # Specific error if form input is not found
        flash("There was a problem with your form submission.")
        return redirect('/')

    except sqlite3.Error as e:
        print(f"Database error: {e}")  # If database error occurs
        flash('An error occurred while saving the message.')
        return redirect('/')

    except Exception as e:
        print(f"Unexpected error: {e}")  # Catch any unexpected error
        flash('An unexpected error occurred.')
        return redirect('/')


if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
