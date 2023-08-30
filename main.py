import os
from flask import Flask, render_template, request, url_for, redirect
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import psycopg2
from configparser import ConfigParser

app = Flask(__name__)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))

def get_db_info(filename,section):
    parser=ConfigParser()
    parser.read([filename])

    db_info={}
    if parser.has_section(section):
         key_val_tuple = parser.items(section) 
         for item in key_val_tuple:
             db_info[item[0]]=item[1]

    return db_info

@app.route('/')
def get_index_data():
    return "We will return something"

@app.route('/sign-up', methods=['POST'])
@cross_origin()
def sign_up():
    json = request.json
    print(json);

    try:
        db_params = get_db_info('database.ini', 'postgresql')
        conn = psycopg2.connect(**db_params);
        # create a cursor
        cur = conn.cursor()
        cur.execute("INSERT INTO users (id, first_name, last_name, email, password) VALUES (%s, %s, %s, %s, %s)", (2, json["firstName"], json["lastName"], json["email"], json["password"])) 
        conn.commit()
        cur.close()
        conn.close()

        return {
            "status": 200
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
    
    