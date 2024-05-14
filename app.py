from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_url_path='/static', static_folder='static')

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class TodoApp:
    def __init__(self):
        self.task_file = 'todo.txt'
        self.tasks = self.load_todo()

    def load_todo(self):
        try:
            with open(self.task_file, 'r') as f:
                tasks = [line.strip() for line in f.readlines()]
                return [Task(description) for description in tasks]
        except FileNotFoundError:
            return []

    def save_todo(self):
        with open(self.task_file, 'w') as f:
            for task in self.tasks:
                f.write(task.description + '\n')

todo_app = TodoApp()

@app.route('/')
def index():
    return render_template('index.html', tasks=todo_app.tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_description = request.form['task']
    if task_description.strip():  # Check if task description is not empty
        new_task = Task(description=task_description)
        todo_app.tasks.append(new_task)
        todo_app.save_todo()
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 0 <= task_id < len(todo_app.tasks):
        del todo_app.tasks[task_id]
        todo_app.save_todo()
    return redirect(url_for('index'))

@app.route('/task_status/<int:task_id>', methods=['POST'])
def task_status(task_id):
    if 0 <= task_id < len(todo_app.tasks):
        todo_app.tasks[task_id].completed = not todo_app.tasks[task_id].completed
        todo_app.save_todo()
    return redirect(url_for('index'))

@app.route('/delete_all_task', methods=['POST'])
def delete_all():
    todo_app.tasks.clear()
    todo_app.save_todo()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
