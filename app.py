from flask import Flask, render_template, request, redirect, url_for
import os
import data
import datetime
from passlib.hash import pbkdf2_sha256
from dotenv import load_dotenv
from bson.objectid import ObjectId
import flask_login

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
    user_in_db = client[DB_NAME].users.find_one({
        'email':email
    })

    user = User()
    user.id = user_in_db['email']

    if user:
        return user
    else:
        return None


# Webpage Routes
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
        'product_brand': request.form.get('product_brand'), 
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
    
@app.route('/edit_review/<review_id>', methods=['POST'])
def process_edit_review(review_id):
    client = data.get_client()

    selected_categories = request.form.getlist('categories')
    cat_to_add = []

    for sc in selected_categories:
        current_cat = client[DB_NAME].categories.find_one({
            '_id':ObjectId(sc)
        })

        cat_to_add.append({
            'category_id':ObjectId(current_cat['_id']),
            'name':current_cat['name']
        })

    client[DB_NAME].user_reviews.update_one({
        '_id': ObjectId(review_id)
        },
        {
            '$set':{
            'title': request.form.get('title'),
            'posted': datetime.datetime.now().isoformat(),
            'product_name': request.form.get('product_name'), 
            'product_brand': request.form.get('product_brand'), 
            'country_of_origin': request.form.get('country_of_origin'),
            'categories': cat_to_add,
            'rating': request.form.get('rating'),
            'review': request.form.get('review'),
            'image': request.form.get('product_image')
            }
        }
    )
   
    return redirect(url_for('read_reviews'))

@app.route('/delete_review/<review_id>')
def confirm_delete_review(review_id):

    client = data.get_client()

    review = client[DB_NAME].user_reviews.find_one({
        '_id': ObjectId(review_id)
    })

    return render_template('delete_review.template.html', r=review)


@app.route('/delete_review/<review_id>', methods=['POST'])
def delete_review(review_id):
    client = data.get_client()

    review = client[DB_NAME].user_reviews.delete_one({
        '_id': ObjectId(review_id)
    })

    return redirect(url_for('read_reviews'))


@app.route('/register_user')
def add_user():
    return render_template('register.template.html')


@app.route('/register_user', methods=['POST'])
def process_add_user():
    
    client = data.get_client()

    password = request.form.get('password')
    encrypted_password = pbkdf2_sha256.hash(password)

    client[DB_NAME].users.insert_one({
        'email':request.form.get('email'),
        'name': request.form.get('name'),
        'password': encrypted_password,
        'age': request.form.get('age'),
        'gender': request.form.get('gender'),
        'occupation': request.form.get('occupation')
    })

    return "User Created"

@app.route('/user_login')
def user_login():
    return render_template('user_login.template.html')
    

@app.route('/user_login', methods=['POST'])
def proccess_user_login():

    client = data.get_client()

    user_in_db = client[DB_NAME].users.find_one({
        'email': request.form.get('email')
    })

    user = User()
    user.id = user_in_db['email']
    if verify_password(request.form.get('password'), user_in_db['password']):
        flask_login.login_user(user)
        return "User Login Successful"
    else:
        return "User Login Fail"
        

@app.route('/protected')
@flask_login.login_required
def private_section():
    return "Only member can see this"


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return "Logged out"


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)