from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a random string

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/interests')
def interest():
    return render_template('interests.html')


if __name__ == '__main__':
    app.run(debug=True)
