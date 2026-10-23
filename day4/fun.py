from flask import Flask
import uuid
app = Flask(__name__)
@app.route('/')
def home():
    """default home page"""
    return "student home page"
@app.route('/studentid/<int:student_id>')
def student(student_id):
    """generate student id"""
    return f"Student ID: {student_id}"
@app.route('/attendance/<float:attendance>')
def attendance(attendance):
    """generate student attendance"""
    return f"Student Attendance: {attendance}"
@app.route('/file/<path:filename>')
def file(filename):
    """generate student file"""
    return f"Student File: {filename}"
@app.route('/studentuuid')
def studentuuid():
    """generate student uuid"""
    id = uuid.uuid4().hex
    print(id)
    return f"Generated Student UUID: {id}"
@app.route('/skills/<s1>/<s2>')
def skills(s1,s2):
    """generate student skills"""
    return f"Student Skills: {s1}, {s2}"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)