import os
from flask import Flask, render_template, request, url_for, redirect
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///postgres:1234@localhost:5432/ai_app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def testdb():
    try:
        db.session.query("1").from_statement("SELECT 1").all()
        return '<h1>It works.</h1>'
    except:
        return '<h1>Something is broken.</h1>'

@app.route("/sign-up", methods=['POST'])
@cross_origin()
def sign_up():
    json = request.json
    print(json);
    return "got your info"

        # // we want to do things with the data
        # Parse the data from the payload
        # Insert into data base
        # Return a status code
    
    