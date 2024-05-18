from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm, TaskForm
from models import User, Task
from extensions import db, bcrypt, login_manager
from flask_login import login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

first_request = True


@app.before_request
def create_tables():
    global first_request
    if first_request:
        db.create_all()
        first_request = False


@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
def error_handler(error):
    # Render the same template for all errors
    return render_template('error.html', error=error), error.code


@app.route('/')
def home():
    search_query = request.args.get('q')
    if current_user.is_authenticated:
        if search_query:
            tasks = Task.query.filter(Task.user_id == current_user.id, Task.title.contains(
                search_query) | Task.description.contains(search_query), Task.completed == False).all()
            completed_tasks = Task.query.filter(Task.user_id == current_user.id, Task.title.contains(
                search_query) | Task.description.contains(search_query), Task.completed == True).all()
        else:
            tasks = Task.query.filter_by(
                user_id=current_user.id,  completed=False).all()

            for task in tasks:
                if len(task.description) > 50:
                    task.description = task.description[:50] + '...'

            completed_tasks = Task.query.filter_by(
                user_id=current_user.id, completed=True).all()
            for task in completed_tasks:
                if len(task.description) > 50:
                    task.description = task.description[:50] + '...'

    else:
        tasks = []
        completed_tasks = []

    return render_template('home.html', tasks=tasks, completed=completed_tasks, authentication=current_user.is_authenticated)


@app.route('/creat_task', methods=['POST', 'GET'])
@login_required
def create_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data,
                    description=form.description.data, user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create_task.html', title='Create New Task', form=form)


def create_user_and_task():
    user = User.query.filter_by(username='example_user').first()
    if not user:
        return render_template('login.html')

    task = Task(title='Task Title', description='Task Description', user=user)
    db.session.add(task)
    db.session.commit()

    return redirect(url_for(home))


@app.route('/edit_task/<int:task_id>', methods=['POST', 'GET'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    form = TaskForm()

    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.completed = form.completed.data
        db.session.commit()
        flash('Task has been updated!', 'success')
        return redirect(url_for('home'))

    if request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
        form.completed.data = task.completed

    return render_template('edit_task.html', title='Edit task', task=task, form=form)


@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/complete_task/<int:task_id>', methods=['POST', 'GET'])
@login_required
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
