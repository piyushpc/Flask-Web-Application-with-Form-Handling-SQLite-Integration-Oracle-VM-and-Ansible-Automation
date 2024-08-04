from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), nullable=False)

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form['task']
    new_todo = Todo(task=task)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({"message": "Task added successfully"})

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    return jsonify({"message": f"Received contact info: {name}, {email}"})

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure this runs inside an app context
    app.run(debug=True)

