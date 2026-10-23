from flask import Flask, render_template

app = Flask(__name__)

# Each student record contains id, name, and marks percentage.
students = [
    {"id": 1, "name": "sanjay", "percentage": 95},
    {"id": 2, "name": "rocky", "percentage": 84},
    {"id": 3, "name": "narasimha", "percentage": 78},
    {"id": 4, "name": "chaitu", "percentage": 67},
    {"id": 5, "name": "ganesh", "percentage": 88},
    {"id": 6, "name": "Rohit", "percentage": 73},
    {"id": 7, "name": "kohli", "percentage": 59},
    {"id": 8, "name": "ABD", "percentage": 81},
    {"id": 9, "name": "david", "percentage": 46},
    {"id": 10, "name": "doremon", "percentage": 95}
]

def calculate_grade(percentage):
    if percentage > 80:
        return "A"
    elif percentage > 70:
        return "B"
    elif percentage > 60:
        return "C"
    elif percentage > 50:
        return "D"
    else:
        return "F"

@app.route('/')
def home():
    for student in students:
        student["grade"] = calculate_grade(student["percentage"])
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True, port=5001)