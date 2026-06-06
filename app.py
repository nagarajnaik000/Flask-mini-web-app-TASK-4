from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    if 0 <= id < len(tasks):
        tasks.pop(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
