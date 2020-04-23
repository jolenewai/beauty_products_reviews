from flask import Flask, render_template, request, redirect, url_for
import os
import pymongo
import data
import datetime
from dotenv import load_dotenv
from bson.objectid import ObjectId


load_dotenv()

DB_NAME = os.environ.get('DB_NAME')
ratings = [1,2,3,4,5]



app = Flask(__name__)


@app.route('/')
def index():
    client = data.get_client()
    reviews = client[DB_NAME].user_reviews.find()
    users = client[DB_NAME].users.find()
    return render_template('index.template.html', reviews=reviews, users=users)


@app.route('/add_review')
def add_review():
    client = data.get_client()

    categories = client[DB_NAME].categories.find()

    return render_template('add_review.template.html',cat=categories, ratings=ratings)


@app.route('/add_review', methods=['POST'])
def process_add_review():

    client = data.get_client()
    client[DB_NAME].user_reviews.insert_one({
        'title':request.form.get('title'),
        'posted': datetime.datetime.now(),
        'user_id':'',
        'product_name':request.form.get('product_name'),
        'product_brand':request.form.get('brand'),
        'categories':'',
        'rating': request.form.get('rating'),
        'review':request.form.get('review')
    })

    return redirect(url_for('index'))


@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    client = data.get_client()

    review = client[DB_NAME].user_reviews.find_one({
        '_id': ObjectId(review_id)
    })

    user = client[DB_NAME].users.find({
        '_id': review['user_id']
    })
    categories = client[DB_NAME].categories.find()
    return render_template('edit_review.template.html', r=review, u=user, cat=categories, ratings=ratings)
    

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)