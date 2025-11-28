from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_manager.db'
    app.config['SECRET_KEY'] = 'mysecretkey'

    db.init_app(app)

    from task_manager.routes import main
    app.register_blueprint(main)

    return app