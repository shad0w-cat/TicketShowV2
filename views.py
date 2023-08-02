from ast import arg
from email import message
from re import A
from flask_restful import Resource, reqparse, marshal, Api, fields, marshal_with, abort
from flask import current_app, jsonify, send_from_directory, session
from datetime import datetime, timedelta
from models import User, Venue, Show, user_show, db
import os
import json
from datetime import datetime
from jwt_auth import auth_required
import jwt
import pandas as pd
from flask_caching import Cache

api = Api()

ven = {
    "venue_id": fields.Integer,
    "name": fields.String,
    "place": fields.String,
    "location": fields.String,
    "capacity": fields.Integer,
}

user = {
    "firstname": fields.String,
    "lastname": fields.String,
    "username": fields.String,
    "email": fields.String,
    "password": fields.String,
}

create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument("firstname")
create_user_parser.add_argument("lastname")
create_user_parser.add_argument("username")
create_user_parser.add_argument("email")
create_user_parser.add_argument("password")

login_user_parser = reqparse.RequestParser()
login_user_parser.add_argument("email")
login_user_parser.add_argument("password")

create_show_parser = reqparse.RequestParser()
create_show_parser.add_argument("showName")
create_show_parser.add_argument("price")
create_show_parser.add_argument("available_seats")
create_show_parser.add_argument("rating")
create_show_parser.add_argument("tags")
create_show_parser.add_argument("venue")

create_venue_parser = reqparse.RequestParser()
create_venue_parser.add_argument("venueName")
create_venue_parser.add_argument("place")
create_venue_parser.add_argument("location")
create_venue_parser.add_argument("capacity")

create_booking_parser = reqparse.RequestParser()
create_booking_parser.add_argument("userId")
create_booking_parser.add_argument("showId")
create_booking_parser.add_argument("rating")


def initialize_views(app):
    app = app
    api.init_app(app)

app = current_app
# app.config["CACHE_TYPE"] = "RedisCache"
# app.config['CACHE_REDIS_HOST'] = "localhost"
# app.config['CACHE_REDIS_PORT'] = 6379
# app.config["CACHE_REDIS_URL"] = "redis://localhost:6379"  
# app.config['CACHE_DEFAULT_TIMEOUT'] = 200
# cache = Cache(app)


class Signup(Resource):
    def post(self):
        args = create_user_parser.parse_args()
        firstname = args.get("firstname", None)
        lastname = args.get("lastname", None)
        email = args.get("email", None)
        password = args.get("password", None)
        username = args.get("username", None)

        if firstname is None:
            abort(404, message="Firstname not provided")

        if lastname is None:
            abort(404, message="Lastname not provided")

        if email is None:
            abort(404, message="Please provide a valid email id")

        if username is None:
            abort(404, message="Please provide a valid email id")

        if password is None:
            abort(404, message="Password not provided")

        user = User.query.filter(User.email == email).first()
        if user:
            abort(404, message="User with this email already exists...")

        name = firstname + " " + lastname
        newuser = User(
            name=name, username=username, email=email, password=password, role="user"
        )

        db.session.add(newuser)
        db.session.commit()

        uid = newuser.user_id
        # app = current_app._get_current_object()
        jt = jwt.encode(
            {"uid": uid, "exp": datetime.utcnow() + timedelta(minutes=30)},
            app.config["SECRET_KEY"],
        )
        # return valid_user
        return jsonify(
            {
                "userId": uid,
                "name": user.name,
                "username": user.username,
                "userRole": user.role,
                "token": jt,
            }
        )


class Login(Resource):
    def post(self):
        args = login_user_parser.parse_args()
        print(args)
        email = args.get("email", None)
        password = args.get("password", None)

        if email is None:
            return {"message": "Please provide a valid email"}, 404

        if password is None:
            return {"message": "Password can not be empty"}, 404

        user = User.query.filter(User.email == email).first()
        app = current_app._get_current_object()
        if user:
            if user.password == password:
                uid = user.user_id
                jt = jwt.encode(
                    {"uid": uid, "exp": datetime.utcnow() + timedelta(minutes=30)},
                    app.config["SECRET_KEY"],
                )
                # return valid_user
                return jsonify(
                    {
                        "userId": uid,
                        "name": user.name,
                        "username": user.username,
                        "userRole": user.role,
                        "token": jt,
                    }
                )
            else:
                abort(404, message="Invalid Password")

        else:
            abort(404, message="User with this email does not exist")


class Logout(Resource):
    @auth_required
    def get(self, userId=None):
        if userId:
            user = User.query.filter(User.user_id == userId).first()
            if user:
                return user
            else:
                abort(404, message="Invalid user id")
        else:
            abort(404, message="Enter user id")


class Profile(Resource):
    @auth_required
    def get(self, userId=None):
        results = []
        if userId:
            user = User.query.filter(User.user_id == userId).first()
            if user:
                user_shows = user_show.query.filter(user_show.user_id == userId).all()
                if user_shows:
                    for shows in user_shows:
                        temp_show = Show.query.filter(
                            Show.show_id == shows.show_id
                        ).first()
                        venue = Venue.query.filter(
                            Venue.venue_id == temp_show.venue_id
                        ).first()
                        d = {
                            "Show": temp_show.name,
                            "Venue": venue.name,
                            "Rate": shows.rated,
                        }
                        results.append(d)
                    return results
                else:
                    return {"msg": "No booking history. Book a show now", "user": user}
            else:
                abort(404, "User with this id does not exist")

        else:
            abort(404, "Provide user id")


class Booking(Resource):
    @auth_required
    def post(self, userId=None):
        args = create_booking_parser.parse_args()
        print(type(args))
        user_id = args.get("userId", None)
        show_id = args.get("showId", None)
        rating = args.get("rating", None)
        if user_id is None:
            abort(404, message="User id not provided")
        if show_id is None:
            abort(404, message="Show id not provided")

        user = user_show.query.filter(
            user_show.user_id == user_id, user_show.show_id == show_id
        ).first()
        if user:
            abort(404, "This show is already booked by you")
        new_booking = user_show(
            user_id=user_id,
            show_id=show_id,
            booking_time=datetime().now(),
            rated=rating,
        )
        db.session.add(new_booking)
        db.session.commit()

        return "Booking Successfull", 200


class VenueApi(Resource):
    @auth_required
    def get(self, venueId=None):
        if venueId:
            ven = Venue.query.filter(Venue.venue_id == venueId).first()
            if ven:
                return jsonify(
                    {
                        "name": ven.name,
                        "place": ven.place,
                        "location": ven.location,
                        "capacity": ven.capacity,
                    }
                )
            else:
                return "Venue does not exist", 200

        else:
            abort(404, message="Enter venue id")

    def post(self, venueId=None):
        args = create_venue_parser.parse_args()
        print(args)
        venue_name = args.get("venueName", None)
        place = args.get("place", None)
        location = args.get("location", None)
        if venue_name is None:
            abort(404, message="Venue name not provided")

        if place is None:
            abort(404, message="Provide a valid Place")

        if location is None:
            abort(404, message="Provide a valid Location")

        ven = Venue.query.filter(Venue.name == venue_name).first()
        if ven:
            abort(404, message="Venue with this Name already exists...")

        new_venue = Venue(
            name=venue_name,
            place=place,
            location=location,
            capacity=args.get("capacity", "undefined"),
        )
        db.session.add(new_venue)
        db.session.commit()

        return "New venue added", 200

    def put(self, venueId=None):
        args = create_venue_parser.parse_args()

        venue_name = args.get("venueName", None)
        place = args.get("place", None)
        location = args.get("location", None)
        capacity = args.get("capacity", None)

        ven = Venue.query.filter(Venue.venue_id == venueId).first()
        if ven:
            if venue_name:
                ven.name = venue_name
            if place:
                ven.place = place
            if location:
                ven.location = location
            if capacity:
                ven.capacity = capacity
            db.session.commit()

            return jsonify(
                {
                    "name": ven.name,
                    "place": ven.place,
                    "location": ven.location,
                    "capacity": ven.capacity,
                }
            )
        else:
            abort(404, "invalid card")

    def delete(self, venueId=None):
        if venueId:
            ven = Venue.query.filter(Venue.venue_id == venueId).first()
            if ven:
                db.session.delete(ven)
                db.session.commit()
                return "Venue deleted successfully", 200
            else:
                abort(404, message="Venue does not exists")
        else:
            abort(404, message="Enter venue id")


class ShowApi(Resource):
    @auth_required
    def get(self, showId=None, venueId=None):
        if showId:
            show = Show.query.filter(Show.show_id == showId).first()
            if show:
                return jsonify(
                    {
                        "name": show.name,
                        "price": show.price,
                        "available_seats": show.available_seats,
                        "tags": show.tags,
                    }
                )
            else:
                return "Show does not exist with this id", 200
        elif venueId:
            show = Show.query.filter(Show.venue_id == venueId).first()
            if show:
                return jsonify(
                    {
                        "name": show.name,
                        "price": show.price,
                        "available_seats": show.available_seats,
                        "tags": show.tags,
                    }
                )
            else:
                return "Show does not exist with this venue id", 200
        else:
            abort(404, message="Enter show id or venue id")

    def post(self, showId=None, venueId=None):
        args = create_show_parser.parse_args()
        print(args)
        show_name = args.get("showName", None)
        price = args.get("price", None)
        seats = args.get("available_seats", None)
        venue = args.get("venue", None)
        if show_name is None:
            abort(404, message="Show name not provided")

        if price is None:
            abort(404, message="Show price not provided")

        if seats is None:
            abort(404, message="Available seats for the show not provided")

        if venue is None:
            abort(404, message="Provide a venue for the show")

        ven = Venue.query.filter(Venue.name == venue).first()
        if ven:
            new_show = Show(
                name=show_name,
                price=price,
                available_seats=seats,
                rating=args.get("rating", None),
                tags=args.get("tags", None),
                venue_id=int(ven.venue_id),
            )
            db.session.add(new_show)
            db.session.commit()
        else:
            abort(404, message="Venue with this Name does not exists...")

        return "New Show added", 200

    def put(self, showId=None, venueId=None):
        args = create_show_parser.parse_args()
        print(args)
        show_name = args.get("venue_name", None)
        price = args.get("price", None)
        seats = args.get("available_seats", None)

        show = Show.query.filter(Show.show_id == showId).first()
        if show:
            if show_name:
                show.name = show_name
            if price:
                show.price = price
            if seats:
                show.available_seats = seats

            db.session.commit()
            return jsonify(
                {
                    "name": show.name,
                    "price": show.price,
                    "available_seats": show.available_seats,
                    "tags": show.tags,
                }
            )
        else:
            abort(404, "invalid card")

    def delete(self, showId=None, venueId=None):
        if showId:
            show = Show.query.filter(Show.show_id == showId).first()
            if show:
                db.session.delete(show)
                db.session.commit()
                return "Show deleted successfully", 200
            else:
                abort(404, message="Show does not exists")
        else:
            abort(404, message="Show venue id")


class GetVenueList(Resource):
    @auth_required
    def get(self):
        venue = Venue.query.all()
        filtered_json = [ven.to_dict() for ven in venue]
        return {"data": filtered_json}


class GetShowList(Resource):
    @auth_required
    def get(self, venueId = None):
        if venueId:
            shows = Show.query.filter(Show.venue_id == venueId)
            filtered_json = [show.to_dict() for show in shows]
            return {"data": filtered_json}
        else:
            abort(404, message="Venue Id not provided")

class GetUserRole(Resource):
    @auth_required
    def get(self, userId = None):
        if userId:
            user = User.query.filter(User.user_id == userId).first()
            return user.role, 200
        else:
            abort(404, message = "User Id not provided")

class ExportVenue(Resource):
    @auth_required
    def get(self,venueId=None):
        
        username = []
        shows = []
        bookings = []
        ratings = []

        if venueId:
            venues = user_show.query.filter(user_show.venue_id == venueId).all()
            venue_name = Venue.query.filter(Venue.venue_id == venueId).first().name
            if venues:
                for record in venues:
                    if record.rated != "":
                        ratings.append(record.rated)
                    else:
                        ratings.append("Not rated")
                    
                    username.append((User.query.filter(User.user_id == record.user_id).first()).name)
                    shows.append((Show.query.filter(Show.show_id == record.show_id).first()).name)
                    bookings.append(record.booking_time)

                Username = pd.Series(username)
                Shows = pd.Series(shows)
                Bookings = pd.Series(bookings)
                Ratings = pd.Series(ratings)

                df = pd.DataFrame({'User' : Username, 'Shows' : Shows, 'Booked On' : Bookings, "Ratings" : Ratings})
                df.to_csv(f"{venue_name}.csv")
            else:
                abort(404, "no bookings for this venue")
            
        else:
            abort(404,message="Venue id not provided")

api.add_resource(GetShowList, "/api/getVenueShow/<int:venueId>")
api.add_resource(Signup, "/api/signup")
api.add_resource(Login, "/api/login")
api.add_resource(Logout, "/api/logout/<int:uid>")
api.add_resource(VenueApi, "/api/venue/<int:venueId>")
api.add_resource(ShowApi, "/api/show/<int:showId>/<int:venueId>")
api.add_resource(GetVenueList, "/api/getVenue")
api.add_resource(Profile, "/api/userProfile/<int:userId>")
api.add_resource(GetUserRole, "/api/getUserRole/<int:userId>")
api.add_resource(ExportVenue,"/api/exportVenue/<int:venueId>")
