from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///TicketShow_database.sqlite3"
    app.config["DEBUG"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.secret_key = "secretkey"

if __name__ == "__main__":
    db.create_all()
    
    app = create_app()
    app.app_context().push()
    db.init_app(app)
    app.run()