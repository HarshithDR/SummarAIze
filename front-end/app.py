from flask import Flask, render_template, session, request, redirect, url_for,jsonify
from db import access_data, add_interests_to_database
from flask_cors import CORS
import os
secret_key = os.urandom(24)

print(secret_key)
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5000"}})
app.secret_key = secret_key  # Change this to a random string


interests = [
    {
        "interest": "music",
        "content": [
            {"image": "imageURL1", "videoId": "1"},
            {"image": "imageURL2", "videoId": "2"},
            {"image": "imageURL3", "videoId": "3"},
            {"image": "imageURL4", "videoId": "4"}
        ]
    },
    {
        "interest": "dance",
        "content": [
            {"image": "imageURL5", "videoId": "5"},
            {"image": "imageURL6", "videoId": "6"},
            {"image": "imageURL7", "videoId": "7"},
            {"image": "imageURL8", "videoId": "8"}
        ]
    }
]


@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/displaycontent')
def displaycontent():
    return render_template('displaycontent.html')

@app.route('/questions')
def questions():
    return render_template('questions.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Check credentials and sign in user
        email = request.form['email']
        # Check if email exists in the database (implementation required)
        # If user exists, store email in session and redirect to interests page
        session['email'] = email
        return redirect(url_for('interests'))
    return render_template('signin.html')

@app.route('/interests', methods=['GET', 'POST'])
def interests():
    if request.method == 'POST':
        # Get interests from the form and store in the database
        interests = request.form.getlist('interest')
        store_interests_in_database(session.get('email'), interests)
        return redirect(url_for('suggestions'))
    return render_template('interests.html')

@app.route('/suggestions')
def suggestions():
    
    return render_template('suggestions.html')

def store_interests_in_database(email, interests):
    # Connect to the database and store the interests associated with the email
    # Update your database access code to handle this operation
    try:
        with access_data() as cursor:
            for interest in interests:
                sql = "INSERT INTO interests (useremailid, interests) VALUES (%s, %s)"
                cursor.execute(sql, (email, interest))
    except Exception as e:
        # Handle the exception (e.g., log the error)
        pass

@app.route('/signout')
def signout():
    session.pop('email', None)
    return redirect(url_for('landing'))

@app.route('/some-protected-route')
def protected_route():
    if 'email' in session:
        # User is logged in
        return render_template('protected.html')
    else:
        # Redirect to sign in page
        return redirect(url_for('signin'))
    
@app.route('/add_interest', methods=['POST'])
def add_interest():
    email = session.get('email')  # Get email from session
    interest = request.json.get('interest')  # Get interest from JSON data
    
    # Insert data into the interests table
    try:
        with access_data() as cursor:
            sql = "INSERT INTO interests (id, useremailid, interests) VALUES (1, %s, %s)"
            cursor.execute(sql, (email, interest))
            return "Interest added successfully"
    except Exception as e:
        return f"Error: {str(e)}", 500  # Return error message with status code 500

@app.route('/update_interests', methods=['POST'])
def update_interests():
    if 'email' in session:
        email = session['email']
        interests = request.json.get('interests')
        add_interests_to_database(email, interests)
        return jsonify({'message': 'Interests updated successfully'}), 200
    else:
        return jsonify({'error': 'User not logged in'}), 401
    
if __name__ == '__main__':
    app.run(debug=True)
