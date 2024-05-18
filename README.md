# TaskTrek App

A simple and intuitive ToDo application built with Flask. This app helps users manage their tasks efficiently by allowing them to create, edit, complete, and delete tasks. It is designed for individuals who want a straightforward way to keep track of their daily tasks and ensure nothing is forgotten.


## Features

- User registration and authentication
- Create, edit, and delete tasks
- Mark tasks as completed or incomplete
- Search for tasks by title or description
- Responsive design for mobile and desktop



## Installation Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/todo-app.git
   cd todo-app
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**:
   Create a `.env` file in the project root and add the following:
   ```plaintext
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   SQLALCHEMY_DATABASE_URI=sqlite:///site.db
   ```

5. **Initialize the database**:
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

6. **Run the application**:
   ```bash
   flask run
   ```

7. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000`


## Usage

1. **Run the application**:
   Ensure your virtual environment is activated, then start the Flask server:
   ```bash
   flask run
   ```

2. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000`

3. **Register an account**:
   - Click on the "Register" link in the navigation bar.
   - Fill out the registration form and submit.

4. **Log in**:
   - Click on the "Login" link in the navigation bar.
   - Enter your credentials and submit.

5. **Create a new task**:
   - Click on the "Create new task" button.
   - Fill out the task form and submit.

6. **Edit a task**:
   - Click the edit icon next to the task you want to edit.
   - Update the task details and submit.

7. **Mark a task as completed**:
   - Check the checkbox next to the task to mark it as completed.

8. **Delete a task**:
   - Click the delete icon next to the task you want to delete.

9. **Search for tasks**:
   - Use the search bar to find tasks by title or description.

Great! Let's proceed to the next step.



## Screenshots

### Home Page
![Home Page](/static/screenshots/home-page.png)

### Registration Form
![Registration Form](/static/screenshots/registration.png)


## Routes and Endpoints

- `/`: Home page displaying a list of tasks.
- `/login`: Login page for users to authenticate.
- `/register`: Registration page for new users to sign up.
- `/logout`: Route to log out the current user.
- `/create_task`: Route to create a new task.
- `/edit_task/<task_id>`: Route to edit an existing task.
- `/delete_task/<task_id>`: Route to delete a task.
- `/complete_task/<task_id>`: Route to mark a task as completed.



## Technologies Used

- **Flask**: Micro web framework for Python.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Jinja2**: Template engine for Python.
- **SQLite**: Embedded relational database management system.


## Contributing

I welcome contributions from the community! If you find any issues or have suggestions for improvements, please feel free to open an issue or pull request on my GitHub repository.

To contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.


## Contact

For any questions, feedback, or inquiries about this project, feel free to contact me:

- **Name:** Adham Emam
- **Email:** adhamh372002@gmail.com
- **GitHub:** (https://github.com/Adham-Emam/Adham-Emam)
