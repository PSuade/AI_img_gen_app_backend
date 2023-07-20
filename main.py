from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello, World!"

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
    
    