from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    """default home page"""
    return "Hello, World!"
@app.route('/about/')
def details():
    """about page"""
    return "This is the about page."
@app.route('/profile/')
def profile():
    """profile page"""
    return "This is the profile page."
@app.route('/name/<name>')
def name(name):
    """name page"""
    return f"Hello, {name}!"
@app.route('/student/<int:student_id>')
def student(student_id):
    """student page"""
    return f"Hello, student with ID: {student_id}!"
@app.route('/percentages/<float:percentage>')
def percentages(percentage):
    """percentages page"""
    return f"Hello, student with percentage: {percentage}!"
@app.route('/file/<path:filename>')
def file(filename):
    """file page"""
    return f" This is the <b> {filename} </b> file page."
@app.route('/student_id/<uuid:student_id>')
def student_id(student_id):
    """student id page"""
    return f" This is the <b> {student_id} </b> student id page."
@app.route('/course/<course_name>')
def course(course_name):
    """course page"""
    return f" This is the <b> {course_name} </b> course page."
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)