from flask import Flask, render_template, request, redirect, url_for
import os
import pymongo
from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI')
DB_NAME = "animal_shelter"

def get_client():
    #create a mongo client
    client = pymongo.MongoClient(MONGO_URI)
    return client

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.template.html')





# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host='localhost',
            port=8080,
            debug=True)