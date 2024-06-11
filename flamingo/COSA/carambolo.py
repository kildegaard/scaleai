from flask import Flask, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo
from bson import ObjectId
from datetime import datetime
import plotly
import plotly.graph_objs as go
import json

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/project-management'
mongo = PyMongo(app)
app.secret_key = 'secret_key'

# User roles
roles = ['admin', 'project_manager', 'team_member']

# Login and registration
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = mongo.db.users.find_one({'username': username, 'password': password})
        if user:
            session['user_id'] = str(user['_id'])
            session['role'] = user['role']
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        mongo.db.users.insert_one({'username': username, 'password': password, 'role': role})
        return redirect(url_for('login'))
    return render_template('register.html', roles=roles)

# Index page
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    projects = mongo.db.projects.find()
    return render_template('index.html', projects=projects)

# Project management
@app.route('/project/create', methods=['GET', 'POST'])
def create_project():
    if 'user_id' not in session or session['role'] not in ['admin', 'project_manager']:
        return redirect(url_for('index'))
    if request.method == 'POST':
        project_name = request.form['project_name']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        mongo.db.projects.insert_one({'project_name': project_name, 'start_date': start_date, 'end_date': end_date})
        return redirect(url_for('index'))
    return render_template('create_project.html')

@app.route('/project/<project_id>')
def view_project(project_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    project = mongo.db.projects.find_one({'_id': ObjectId(project_id)})
    tasks = mongo.db.tasks.find({'project_id': ObjectId(project_id)})
    return render_template('view_project.html', project=project, tasks=tasks)

# Task management
@app.route('/task/create/<project_id>', methods=['GET', 'POST'])
def create_task(project_id):
    if 'user_id' not in session or session['role'] not in ['admin', 'project_manager']:
        return redirect(url_for('index'))
    if request.method == 'POST':
        task_name = request.form['task_name']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        mongo.db.tasks.insert_one({'task_name': task_name, 'start_date': start_date, 'end_date': end_date, 'project_id': ObjectId(project_id)})
        return redirect(url_for('view_project', project_id=project_id))
    return render_template('create_task.html')

# Gantt chart
@app.route('/gantt/<project_id>')
def gantt(project_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    tasks = mongo.db.tasks.find({'project_id': ObjectId(project_id)})
    task_list = []
    for task in tasks:
        task_list.append({
            'Task': task['task_name'],
            'Start': task['start_date'],
            'Finish': task['end_date']
        })
    fig = go.Figure(data=[go.Bar(name='Task', x=[task['Task'] for task in task_list], y=[(datetime.strptime(task['Finish'], '%Y-%m-%d') - datetime.strptime(task['Start'], '%Y-%m-%d')).days for task in task_list], hovertext=[task['Start'] + ' to ' + task['Finish'] for task in task_list])])
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('gantt.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True)