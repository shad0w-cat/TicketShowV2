from celery import Celery, Task
from models import User, Venue, user_show, Show
from send_mail import send_email
from jinja2 import Template
from celery.schedules import crontab
from dateutil import parser
from datetime import date, datetime
# from flask import current_app as app

# celery = Celery(broker_url="redis://127.0.0.1:6379/1",
#     result_backend="redis://127.0.0.1:6379/2",
#     timezone="Asia/Kolkata")
celery = Celery()

def initialize_celery(app):
    app = app
    class FlaskTask(Task):
            def __call__(self, *args, **kwargs):
                with app.app_context():
                    self.run(*args, **kwargs)

    # celery = Celery(app.name)
    # celery.config_from_object("celeryconfig")
    celery = Celery(broker_url="redis://127.0.0.1:6379/1",
        result_backend="redis://127.0.0.1:6379/2",
        broker_connection_retry_on_startup=True,
        timezone="Asia/Kolkata")
    
    # celery.set_default()
    app.extensions["celery"] = celery
    print("celery created")

@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    print("in celery")
    sender.add_periodic_task(15.0, test_func.s())
    sender.add_periodic_task(30.0, daily_task.s(), name='daily')
    sender.add_periodic_task(600.0, monthly_task.s(), name='monthly')

@celery.task()
def test_func():
    print("yaha aa gya")

@celery.task()
def daily_task():
    print("in daily task")
    send = False
    all_users = User.query.all()
    for user in all_users:
        user_shows = user_show.query.filter(user_show.user_id == user.user_id).all()
        for bookings in user_shows:
            if parser.parse(bookings.booking_time).date() == datetime.now().date():
                send = False
                break
        if send:
            with open("public/send_mail.html","r") as b:
                html=Template(b.read())
                print("sent yayayayaya")
                send_email(user.email, subject="Daily Reminder", message=html.render(user=user))
                

@celery.task()
def monthly_task():
    all_users = User.query.all()
    for user in all_users:
        d = {}
        user_shows = user_show.query.filter(user_show.user_id == user.user_id).all()
        month = datetime.now().month()-1
        for bookings in user_shows:
            booking = parser.parse(bookings.booking_time)
            if booking.month() == month:
                show = Show.query.filter(Show.show_id == bookings.show_id).first()
                venue = Venue.query.filter(Venue.venue_id == bookings.venue_id).first()
                
                if (show.name in d.keys()) and (d[show.name]['booking'] == booking.date()):
                    d[show.name]["count"] += 1
                    d[show.name]["booking"].append(booking.date())
                    continue
                d[show.name] = {'count' : 1, 'booking' : [booking.date()]}

        with open("public/send_monthly.html","r") as b:
            html=Template(b.read())
            send_email(user.email, subject="Monthly Progress Report", message=html.render(d=d,user=user))


    
    # app.config['CELERY_BROKER_URL'] = "redis://127.0.0.1:6379/1"
    # app.config['CELERY_RESULT_BACKEND'] = "redis://127.0.0.1:6379/2"
    # celery.conf.update(app.config)
    

