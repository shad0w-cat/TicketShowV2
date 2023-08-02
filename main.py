from typing import ByteString
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db
from flask_cors import CORS
from views import initialize_views
from celery_worker import celery,ContextTask



app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///TicketShow_database.sqlite3"
app.config["DEBUG"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = "shushhh"

db.init_app(app)
with app.app_context():
    db.create_all()
initialize_views(app)

celery=celery

CELERY_BROKER_URL="redis://127.0.0.1:6379/1"
CELERY_RESULT_BACKEND="redis://127.0.0.1:6379/2"

celery.conf.update(
    broker_url="redis://127.0.0.1:6379/1",
    result_backend="redis://127.0.0.1:6379/2",
    timezone="Asia/Kolkata"
)

celery.Task=ContextTask

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
