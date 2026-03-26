from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

tasks = []

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do List</title>
    <style>
        body { background: #D6A4DD; font-family: sans-serif; }
        .container { max-width: 400px; margin: 40px auto; background: #fff; border-radius: 10px; padding: 20px; box-shadow: 0 2px 8px #aaa; }
        h2 { color: #556B2F; text-align: center; }
        ul { list-style: none; padding: 0; }
        li { padding: 8px 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; }
        form { display: flex; margin-bottom: 16px; }
        input[type=text] { flex: 1; padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
        button { background: #27ae60; color: #fff; border: none; padding: 8px 16px; border-radius: 4px; margin-left: 8px; cursor: pointer; }
        button.delete { background: #e74c3c; }
    </style>
</head>
<body>
    <div class="container">
        <h2>TO-DO List</h2>
        <form method="POST" action="/add">
            <input type="text" name="task" placeholder="Add a new task" required>
            <button type="submit">Add</button>
        </form>
        <ul>
            {% for idx, task in tasks %}
            <li>{{ task }}
                <form method="POST" action="/delete/{{ idx }}" style="display:inline;">
                    <button class="delete" type="submit">Delete</button>
                </form>
            </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML, tasks=list(enumerate(tasks)))

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:idx>', methods=['POST'])
def delete(idx):
    if 0 <= idx < len(tasks):
        tasks.pop(idx)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=81)
