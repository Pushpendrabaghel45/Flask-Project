# app.py – Complete Detailed Explanation (Line-by-Line)

## 1. Imports

```python
import sys
import os
from flask import Flask, render_template, redirect, url_for, request, flash, session, abort
from werkzeug.security import generate_password_hash, check_password_hash

from config import Config
from models import db, User, Task
```

### Explanation
- **sys, os** — for file paths and environment operations.
- **Flask** — creates the main Flask app.
- **render_template** — loads HTML templates.
- **redirect, url_for** — for page navigation.
- **request** — handles GET/POST form data.
- **flash** — small UI messages.
- **session** — stores logged-in user data.
- **abort** — stop execution with HTTP error codes.
- **generate_password_hash, check_password_hash** — secure password hashing.
- **Config** — settings from config.py.
- **db, User, Task** — SQLAlchemy database + models.

---

## 2. Application Factory Pattern

```python
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app
```

### Explanation
Creates an extensible Flask app:
- Loads config (secret key, DB).
- Initializes SQLAlchemy.
- Returns the app instance.

---

## 3. App Instance

```python
app = create_app()
```

Initializes your Flask app.

---

## 4. Authentication Decorators

### 4.1 login_required

```python
def login_required(fn):
    from functools import wraps
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access that page.', 'warning')
            return redirect(url_for('login'))
        return fn(*args, **kwargs)
    return wrapper
```

#### Explanation
- Protects routes.
- Redirects to login if user not authenticated.

---

### 4.2 admin_required

```python
def admin_required(fn):
    from functools import wraps
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session or session.get('role') != 'admin':
            flash('Admin access required.', 'danger')
            return redirect(url_for('login'))
        return fn(*args, **kwargs)
    return wrapper
```

#### Explanation
- Ensures user is logged in **and** has role = admin.

---

## 5. Public Homepage

```python
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index_public.html')
```

---

## 6. User Registration

```python
@app.route('/register', methods=['GET', 'POST'])
def register():
    ...
```

### How it works
- GET → show register page.
- POST → validate -> hash password -> save user.

---

## 7. User Login

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    ...
```

### Flow
- Reads username/password.
- Verifies user exists.
- Validates password using `check_password_hash`.
- Stores session:
  - user_id
  - username
  - role

---

## 8. Logout

```python
@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))
```

### Explanation
Clears all session data.

---

## 9. User Dashboard

```python
@app.route('/dashboard')
@login_required
def dashboard():
    ...
```

### Explanation
Shows:
- total tasks
- completed tasks
- user welcome message

---

## 10. Task CRUD

### 10.1 View Tasks

```python
@app.route('/tasks')
@login_required
def tasks():
    ...
```

### 10.2 Add Task

```python
@app.route('/tasks/add', methods=['GET', 'POST'])
@login_required
def add_task():
    ...
```

### 10.3 Edit Task

```python
@app.route('/tasks/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_task(id):
    ...
```

### 10.4 Delete Task

```python
@app.route('/tasks/delete/<int:id>', methods=['POST'])
@login_required
def delete_task(id):
    ...
```

---

## 11. Admin Panel

### 11.1 Admin Dashboard
```python
@app.route('/admin')
@admin_required
def admin_dashboard():
    ...
```

### 11.2 List Users
```python
@app.route('/admin/users')
@admin_required
def admin_users():
    ...
```

### 11.3 Delete User
```python
@app.route('/admin/users/delete/<int:user_id>', methods=['POST'])
@admin_required
def admin_delete_user(user_id):
    ...
```

### 11.4 All Tasks
```python
@app.route('/admin/tasks')
@admin_required
def admin_tasks():
    ...
```

### 11.5 Tasks by User
```python
@app.route('/admin/user/<int:user_id>/tasks')
@admin_required
def admin_user_tasks(user_id):
    ...
```

---

## 12. Database Init Utility

```python
def init_db(create_admin=True):
    ...
```

### Explanation
- Creates tables.
- Creates default admin:
  - username: admin
  - password: admin123

Run using:
```
python app.py init
```

---

## 13. App Runner

```python
if __name__ == '__main__':
    ...
```

Modes:
1. Init DB
2. Run development server

---

## Summary
This file handles:

- Registration/Login
- Secure authentication
- User dashboard
- Full Task CRUD
- Admin management of users + tasks
- DB initialization
- Session handling
- Role-based access (user/admin)

A complete and scalable Flask web application.
