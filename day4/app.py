from flask import Flask,render_template,redirect,url_for
import uuid
app = Flask(__name__)
#universal unique identifier
@app.route('/')
def home():
    """default home page"""
    #return "Hello, World!"
    return redirect(url_for('aboutpage'))
@app.route('/generate')
def generate():
    """generate a unique identifier"""
    id = uuid.uuid4().hex
    print(id)
    return f"Generated UUID: {id}"
@app.route('/aboutpage')
def aboutpage():
    """about page"""
    return render_template('about.html')
@app.route('/indexpage')
def indexpage():
    """index page"""
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)