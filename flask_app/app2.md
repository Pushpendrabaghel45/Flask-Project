# app.py – Full Explanation (No Code)

This document explains every part of the provided `app.py` file in a structured and clear way.

---

## 1. Purpose of `app.py`

`app.py` is the **main controller** of your Flask application. It:

* Creates and configures the Flask app
* Connects to the database
* Defines user authentication (Register, Login, Logout)
* Provides user dashboard and task management
* Provides admin dashboard and admin-level controls
* Controls sessions, permissions, and routing

It acts as the central heart of the application.

---

## 2. Application Factory (`create_app()`)

The file uses an **Application Factory Pattern**, meaning the Flask app is created inside a function:

* Loads configuration from `Config`
* Initializes SQLAlchemy with the app
* Prepares the app for use

This pattern makes the app modular and production-ready.

---

## 3. Authentication Helpers (Decorators)

Two custom decorators control access:

### `login_required`

Ensures only logged-in users can open protected routes.
If not logged in → redirect to login.

### `admin_required`

Ensures only admin users can access admin routes.
Checks:

* User is logged in
* User’s role is `admin`

These decorators help maintain security and separate roles.

---

## 4. Public Route

### `/`

* If the user is logged in → redirect to dashboard
* Otherwise → show a public landing page (`index_public.html`)

A clean entry point for visitors.

---

## 5. Registration (`/register`)

Handles both GET and POST requests:

* Validates form fields
* Ensures username/email are unique
* Hashes the password
* Saves the new user to the database

This ensures safe and secure registration.

---

## 6. Login (`/login`)

Authenticates users:

* Checks if username exists
* Verifies hashed password
* Stores user info in session (id, name, role)

Sessions allow the website to remember who is logged in.

---

## 7. Logout (`/logout`)

Clears the session completely.
User is fully logged out and redirected to login page.

---

## 8. User Dashboard (`/dashboard`)

Accessible only to logged-in users.
Displays:

* Logged-in username
* Task statistics (total tasks, completed tasks)

This page is personalized per user.

---

## 9. User Task Management

### `/tasks`

Shows all tasks belonging to the logged-in user.

### `/tasks/add`

Form to create a new task.
Stores:

* Title
* Description
* User ID (to link task with owner)

### `/tasks/edit/<id>`

Allows updating task details.
Checks permissions:

* Owner
* OR Admin

### `/tasks/delete/<id>`

Deletes a task.
Same permission checks apply.

Together, these routes implement complete CRUD functionality.

---

## 10. Admin Panel

Only accessible by admin role.

### `/admin`

Displays:

* Total users
* Total tasks

### `/admin/users`

Admin can view all users.

### `/admin/users/delete/<id>`

Admin can delete any user except themselves.
Also deletes all tasks belonging to that user.

### `/admin/tasks`

Admin can view all tasks from all users.

### `/admin/user/<id>/tasks`

Shows all tasks created by a specific user.

This gives full administrative control.

---

## 11. Database Initialization Function

`init_db()` helps:

* Create database tables
* Create a default admin if none exists

It is triggered using:

```
python app.py init
```

Useful during fresh setup.

---

## 12. Running the App

If no command-line argument is passed:

* Flask runs in debug mode
* Ensures the SQLite database file exists

Executed normally with:

```
python app.py
```

---

## Summary

The `app.py` file implements:

* User registration and login system
* Task manager CRUD module
* Complete admin panel
* Role-based access control
* Secure session management
* Database setup tools


