from datetime import time
import time as time_module
from typing import ByteString
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, User
from flask_cors import CORS
from views import initialize_views
from flask_caching import Cache
import celery_task

app = Flask(__name__)
CORS(app)
cache = Cache()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///TicketShow_database.sqlite3"
app.config["DEBUG"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = "shushhh"
app.config["CACHE_TYPE"] = "RedisCache"
app.config['CACHE_REDIS_HOST'] = "localhost"
app.config['CACHE_REDIS_PORT'] = 6379
app.config["CACHE_REDIS_URL"] = "redis://localhost:6379"
app.config['CACHE_DEFAULT_TIMEOUT'] = 200
cache.init_app(app)
celery_task.initialize_celery(app)

db.init_app(app)
with app.app_context():
    db.create_all()
    admin = User.query.filter_by(role = "admin").first()
    if not admin:
        admin = User(name="SIMRAN", username="simran", email="simran@gmail.com", password="2345", role="admin")
        db.session.add(admin)
        db.session.commit()
initialize_views(app)

@app.route('/abcd')
@cache.cached(timeout=10)
def testingcache():
    time_module.sleep(10)
    return "done"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
