from flask import Flask, render_template, request, redirect, url_for, flash
import os
import data
import datetime
import pymongo
from passlib.hash import pbkdf2_sha256
from dotenv import load_dotenv
from bson.objectid import ObjectId
import flask_login
import dao

load_dotenv()

DB_NAME = os.environ.get('DB_NAME')
ratings = [1,2,3,4,5]

# create the flask app
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


#create the login manager
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


#create the user class
class User(flask_login.UserMixin):
    pass


def encrypt_password(password_text):
    return pbkdf2_sha256.hash(password_text)


def verify_password(password_text, encrypted_password):
    return pbkdf2_sha256.verify(password_text, encrypted_password)


@login_manager.user_loader
def user_loader(email):

    client = data.get_client()

    # attempt to get the user
    user_in_db = dao.get_user_by_email(client, email)

    user = User()
    user.id = user_in_db['email']

    if user:
        return user
    else:
        return None


def check_user_log_in(client):

    current_user = flask_login.current_user

    if current_user:
        user = dao.get_user_by_email(client, current_user.id)
    else:
        user = None

    return user

# Webpage Routes
@app.route('/')
def index():
    return render_template('index.template.html')


@app.route('/read_reviews')
def read_reviews():
    client = data.get_client()

    latest_review = client[DB_NAME].user_reviews.find().sort('posted', pymongo.DESCENDING).limit(1)

    users = dao.get_all_users(client)
    categories = dao.get_all_categories(client)

    skincare_reviews = client[DB_NAME].user_reviews.find(
        {
             'categories.name': 'Skin Care'
        }
    ).sort('posted', pymongo.DESCENDING).limit(3)

    cosmetic_reviews = client[DB_NAME].user_reviews.find(
        {
            'categories.name': 'Cosmetic'
        }
    ).sort('posted', pymongo.DESCENDING).limit(3)

    bodycare_reviews = client[DB_NAME].user_reviews.find(
        {
            'categories.name': 'Body Care'
        }
    ).sort('posted', pymongo.DESCENDING).limit(2)

    haircare_reviews = client[DB_NAME].user_reviews.find(
        {
            'categories.name': 'Hair Care'
        }
    ).sort('posted', pymongo.DESCENDING).limit(2)

    user_list = []
    for user in users:
        user_list.append(user)

    if flask_login.current_user.is_authenticated:
        current_user = flask_login.current_user

        if current_user:
            user = dao.get_user_by_email(client, current_user.id)
        else:
            user = None


    return render_template('read_reviews.template.html', review=latest_review, cat=categories, users=user_list, skincare=skincare_reviews, cosmetics=cosmetic_reviews, bodycare=bodycare_reviews, haircare=haircare_reviews, user=user)


@app.route('/read_reviews/<cat_id>')
def read_reviews_by_category(cat_id):

    client = data.get_client()
    
    reviews = dao.get_reviews_by_cat_id(client, cat_id)
    current_cat = dao.get_category_by_id(client, cat_id)
    all_cat = client[DB_NAME].categories.find()

    if flask_login.current_user.is_authenticated:
        current_user = flask_login.current_user

        if current_user:
            user = dao.get_user_by_email(client, current_user.id)
        else:
            user = None

    return render_template('read_reviews_by_cat.template.html', current_cat=current_cat, cat=all_cat, reviews=reviews, user=user)


@app.route('/add_review')
@flask_login.login_required
def add_review():

    client = data.get_client()
    public_key = os.environ.get('UPLOADCARE_PUBLIC_KEY')

    categories = dao.get_all_categories(client)
    cat_list = []

    for cat in categories:
        cat_list.append(cat)

    if flask_login.current_user.is_authenticated:
        current_user = flask_login.current_user

        if current_user:
            user = dao.get_user_by_email(client, current_user.id)
        else:
            user = None
    else:
        return redirect('/user_login?redirect=/add_review')

    return render_template('add_review.template.html',cat=cat_list, ratings=ratings, public_key=public_key, user=user)


@app.route('/add_review', methods=['POST'])
@flask_login.login_required
def process_add_review():

    client = data.get_client()
    selected_categories = request.form.getlist('categories')
    cat_to_add = []

    user = check_user_log_in(client)

    user_id = user['_id']

    for sc in selected_categories:
        current_cat = dao.get_category_by_id(client, sc)

        cat_to_add.append({
            'category_id': ObjectId(current_cat['_id']),
            'name': current_cat['name']
        })

    client[DB_NAME].user_reviews.insert_one({
        'title': request.form.get('title'),
        'posted': datetime.datetime.now(),
        'user_id': ObjectId(user_id),
        'product_name': request.form.get('product_name'),
        'product_brand': request.form.get('product_brand'),
        'country_of_origin': request.form.get('country_of_origin'),
        'categories': cat_to_add,
        'rating': request.form.get('rating'),
        'review': request.form.get('review'),
        'image': request.form.get('product_image')
    })

    return redirect(url_for('index'))


@app.route('/edit_profile/<user_id>')
@flask_login.login_required
def edit_profile(user_id):

    client = data.get_client()

    user = check_user_log_in(client)
    categories = dao.get_all_categories(client)

    return render_template('edit_profile.template.html', user=user, cat=categories)


@app.route('/edit_profile/<user_id>', methods=['POST'])
@flask_login.login_required
def process_edit_profile(user_id):
    client = data.get_client()

    user = check_user_log_in(client)
    email = request.form.get('email')
    name = request.form.get('name')
    password = user['password']
    age = request.form.get('age')
    gender = request.form.get('gender')
    occupation = request.form.get('occupation')

    dao.update_user_profile(client, user_id, email, name, password, age, gender, occupation)

    user = dao.get_one_user(client, user_id)
    categories = dao.get_all_categories(client)

    flash('Profile Updated')

    return render_template('edit_profile.template.html', user=user, cat=categories)


@app.route('/my_reviews/<user_id>')
@flask_login.login_required
def view_my_reviews(user_id):

    client = data.get_client()

    my_reviews = dao.get_review_by_userid(client, user_id)
    categories = dao.get_all_categories(client)
    user = dao.get_one_user(client, user_id)

    if flask_login.current_user.is_authenticated:
        current_user = flask_login.current_user

        if current_user:
            user = dao.get_user_by_email(client, current_user.id)
        else:
            user = None
    else:
        return redirect('/user_login?redirect=/read_reviews')

    return render_template('my_reviews.template.html', reviews=my_reviews, user=user, cat=categories)


@app.route('/edit_review/<review_id>')
@flask_login.login_required
def edit_review(review_id):
    client = data.get_client()

    review = dao.get_review_by_review_id(client, review_id)
    user = dao.get_one_user(client, review['user_id'])
    categories = dao.get_all_categories(client)

    return render_template('edit_review.template.html', r=review, user=user, cat=categories, ratings=ratings)


@app.route('/edit_review/<review_id>', methods=['POST'])
@flask_login.login_required
def process_edit_review(review_id):
    client = data.get_client()

    selected_categories = request.form.getlist('categories')
    cat_to_add = []

    review_to_edit = dao.get_review_by_review_id(client, review_id)

    posted_date = review_to_edit['posted']

    title = request.form.get('title')
    posted = posted_date
    user_id = request.form.get('user_id')
    product_name = request.form.get('product_name')
    product_brand = request.form.get('product_brand')
    country_of_origin = request.form.get('country_of_origin')
    rating = request.form.get('rating')
    review = request.form.get('review')

    if request.form.get('product_image'):
        image = request.form.get('product_image')
    else:
        image = request.form.get('existing_product_image')

    for sc in selected_categories:
        current_cat = dao.get_category_by_id(client, sc)

        cat_to_add.append({
            'category_id': ObjectId(current_cat['_id']),
            'name': current_cat['name']
        })

    dao.update_review_by_id(client, review_id, user_id, title, posted, product_name, product_brand, country_of_origin, rating, review, image, cat_to_add)

    return redirect(url_for('view_my_reviews', user_id=user_id))


@app.route('/delete_review/<review_id>')
def confirm_delete_review(review_id):

    client = data.get_client()

    review = dao.get_review_by_review_id(client, review_id)
    user = check_user_log_in(client)

    return render_template('delete_review.template.html', r=review, user=user)


@app.route('/delete_review/<review_id>', methods=['POST'])
def delete_review(review_id):
    client = data.get_client()

    dao.delete_review_by_id(client, review_id)
    user = check_user_log_in(client)

    return redirect(url_for('view_my_reviews', user_id=user._id))


@app.route('/register_user')
def add_user():

    client = data.get_client()

    categories = dao.get_all_categories(client)

    if flask_login.current_user.is_authenticated:
        current_user = flask_login.current_user

        if current_user:
            user = dao.get_user_by_email(client, current_user.id)
        else:
            user = None

    return render_template('register.template.html', cat=categories, user=user)


@app.route('/register_user', methods=['POST'])
def process_add_user():

    client = data.get_client()

    password = request.form.get('password')
    encrypted_password = pbkdf2_sha256.hash(password)

    client[DB_NAME].users.insert_one({
        'email': request.form.get('email'),
        'name': request.form.get('name'),
        'password': encrypted_password,
        'age': request.form.get('age'),
        'gender': request.form.get('gender'),
        'occupation': request.form.get('occupation')
    })

    redirect_url = request.args.get('redirect')

    if redirect_url is None:
        redirect_url = "/"

    return redirect(redirect_url)


@app.route('/search', methods=['POST'])
def search():

    client = data.get_client()
    search_str = request.form.get('search')
    results = dao.search_by_query(client, search_str)

    categories = dao.get_all_categories(client)

    user = check_user_log_in(client)

    return render_template('search_result.template.html',results=results, search_str=search_str, user=user, cat=categories)


@app.route('/user_login')
def user_login():
    return render_template('user_login.template.html')


@app.route('/user_login', methods=['POST'])
def proccess_user_login():

    client = data.get_client()

    user_in_db = dao.get_user_by_email(client, request.form.get('email'))

    print(user_in_db)
    user = User()
    user.id = user_in_db['email']

    redirect_url = request.args.get('redirect')

    if redirect_url == None:
        redirect_url = "/"

    if verify_password(request.form.get('password'), user_in_db['password']):
        flask_login.login_user(user)
        return redirect(redirect_url)
    else:
        flash('Login Failed. Invalid Email or Password')
        return render_template('user_login.template.html')


@app.route('/logout')
def logout():
    flask_login.logout_user()
    redirect_url = request.args.get('redirect')
    return redirect(redirect_url)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)