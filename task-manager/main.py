from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize tasks as an empty list
tasks = []

@app.route('/')
def index():
    """Render the main page with the list of tasks."""
    return render_template('index.html', tasks=tasks)

@app.route('/task/add', methods=['GET', 'POST'])
def add_task():
    """Add a new task."""
    if request.method == 'POST':
        # Get the title and description from the form
        title = request.form.get('title')
        description = request.form.get('description')

        # Create a new task with the title and description
        task = {'title': title, 'description': description}

        # Add the new task to the list
        tasks.append(task)

        # Redirect the user to the main page
        return redirect(url_for('index'))

    # If the request method is GET, return the form for adding a task
    return render_template('add_task.html')

