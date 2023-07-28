from typing import ByteString
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///TicketShow_database.sqlite3"
app.config["DEBUG"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = "secretkey"    
db.init_app(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)