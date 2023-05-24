from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Database connection
conn = sqlite3.connect('employment.db')
c = conn.cursor()

# Render the HTML template for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# API route for submitting user credentials and saving to the database
@app.route('/submit_credentials', methods=['POST'])
def submit_credentials():
    # Extracting user credentials from the request
    username = request.form['username']
    password = request.form['password']
    # Additional credentials (work experience, expected salary, etc.) can be added here

    # Inserting user credentials into the database
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

    return jsonify({'message': 'Credentials submitted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
