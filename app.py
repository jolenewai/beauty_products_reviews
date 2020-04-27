from flask import Flask, render_template, request, redirect, url_for
import os
import data
import datetime
from dotenv import load_dotenv
from bson.objectid import ObjectId
import cloudinary
import cloudinary.uploader
import cloudinary.api
import flask_login

load_dotenv()

DB_NAME = os.environ.get('DB_NAME')
ratings = [1,2,3,4,5]


cloudinary.config( 
  cloud_name = os.environ.get('CLOUDINARY_URL'), 
  api_key = os.environ.get('CLOUDINARY_PUBLIC_KEY'), 
  api_secret = os.environ.get('CLOUDINARY_PRIVATE_KEY')
)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.template.html')

@app.route('/read_reviews')
def read_reviews():
    client = data.get_client()
    reviews = client[DB_NAME].user_reviews.find()
    users = client[DB_NAME].users.find()
    user_list = []
    for user in users:
        user_list.append(user)

    return render_template('read_reviews.template.html', reviews=reviews, users=user_list)

    


@app.route('/add_review')
def add_review():
    client = data.get_client()
    public_key = os.environ.get('UPLOADCARE_PUBLIC_KEY')

    categories = client[DB_NAME].categories.find()
    cat_list = []

    for cat in categories:
        cat_list.append(cat)

    return render_template('add_review.template.html',cat=cat_list, ratings=ratings, public_key=public_key)


@app.route('/add_review', methods=['POST'])
def process_add_review():

    client = data.get_client()
    selected_categories = request.form.getlist('categories')
    cat_to_add = []

    if request.form.get('email'):
        user_email = request.form.get('email').strip()

        user = client[DB_NAME].users.find_one({
            'email': user_email
        })

        if user:
            user_id = user['_id']
        else:
            user_id = ''
            print("user not found")

    for sc in selected_categories:
        current_cat = client[DB_NAME].categories.find_one({
            '_id':ObjectId(sc)
        })

        cat_to_add.append({
            'category_id':ObjectId(current_cat['_id']),
            'name':current_cat['name']
        })

    client[DB_NAME].user_reviews.insert_one({
        'title': request.form.get('title'),
        'posted': datetime.datetime.now().isoformat(),
        # 'user_id': ObjectId(user_id),
        'product_name': request.form.get('product_name'), 
        'product_brand': request.form.get('brand'), 
        'country_of_origin': request.form.get('country_of_origin'),
        'categories': cat_to_add,
        'rating': request.form.get('rating'),
        'review': request.form.get('review'),
        'image': request.form.get('product_image')
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