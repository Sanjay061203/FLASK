from flask import Flask 
app = Flask(__name__)
@app.route('/')
def home():
    """default home page"""
    return "Hello, World!"
@app.route('/about')
def details():
    """about page"""
    return "This is the about page."
@app.route('/profile')
def profile():
    """profile page"""
    return "This is the profile page."
@app.route('/contact/')
def contact():
    """contact page"""
    return "This is the contact page."

if __name__ == '__main__':
    app.run()