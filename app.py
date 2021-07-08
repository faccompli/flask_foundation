from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/todoapp'

db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description=  db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Todo {self.id} {self.description}>"

db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['item']
        todo = Todo(description=data)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    else: 
        return render_template('index.html', items=Todo.query.all())


if __name__ == '__main__':
    app.run(port=3000, debug=True)