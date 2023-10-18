import os
from flask import Flask, render_template, request, url_for, redirect
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import psycopg2

import get_db_info
from models.User import User;

app = Flask(__name__)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def get_index_data():
    return "We will return something"

@app.route('/sign-up', methods=['POST'])
@cross_origin()
def sign_up():
    json = request.json
    print(json);

    try:
        user = User(json["firstName"], json["lastName"], json["email"], json["password"])
        user.save()

        return {
            "status": 200
        }
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return {
            "status": 500
        }


@app.route('/log-in', methods=['POST'])
@cross_origin()
def log_in():
    json = request.json
    print(json);

    try:
        email = json["email"]
        password = json["password"]

        user = User.get_user_by_email(email)
        
        if(password == user[4]):
            return {
                "status": 200
            }
        else:
            return {
                "status": 400
            }

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return {
            "status": 500
        }        

        # // we want to do things with the data
        # Parse the data from the payload
        # Insert into data base
        # Return a status code
    

    