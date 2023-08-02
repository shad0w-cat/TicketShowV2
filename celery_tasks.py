from datetime import datetime
from celery_worker import celery
from flask import current_app as app
from models import User, Venue, user_show, Show
from send_mail import send_email
from jinja2 import Template
from datetime import date, datetime

from celery import Celery
from celery.schedules import crontab
from dateutil import parser


@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=18, minute=00), daily_task.s(), name='daily')
    sender.add_periodic_task(crontab(0, 0, day_of_month='1'), monthly_task.s(), name='monthly')

# @celery.task()
# def just_say_hello():
#     print("WUHAHAHAHA")

@celery.task()
def daily_task():
    send = False
    all_users = User.query.all()
    for user in all_users:
        user_shows = user_show.query.filter(user_show.user_id == user.user_id).all()
        for bookings in user_shows:
            if parser.parse(bookings.booking_time).date() == datetime.now().date():
                send = True
                break
        if send:
            with open("project/public/mail.html","r") as b:
                html=Template(b.read())
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

        with open("project/public/monthly.html","r") as b:
            html=Template(b.read())
            send_email(user.email, subject="Monthly Progress Report", message=html.render(d=d,user=user))
        
