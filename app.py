from flask import Flask, render_template, request, redirect, url_for
import os
import pymongo
import data
from dotenv import load_dotenv
from bson.objectid import ObjectId

load_dotenv()

DB_NAME = os.environ.get('DB_NAME')

app = Flask(__name__)


@app.route('/')
def index():
    client = data.get_client()
    reviews = client[DB_NAME].user_reviews.find()
    users = client[DB_NAME].users.find()
    return render_template('index.template.html', reviews=reviews, users=users)

@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    client = data.get_client()

    review = client[DB_NAME].user_reviews.find_one({
        '_id': ObjectId(review_id)
    })

    print (review)
    users = client[DB_NAME].users.find({
        '_id': review[user_id]
    })

    return render_template('edit_review.template.html', r=review, u=user)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)