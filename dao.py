import os
import data
import pymongo
from dotenv import load_dotenv
from bson.objectid import ObjectId

load_dotenv()

DB_NAME = os.environ.get('DB_NAME')


# function to get one user with user_id
def get_one_user(client, user_id):

    user = client[DB_NAME].users.find_one({
            '_id': ObjectId(user_id)
    })

    return user

# function to get one user with email address
def get_user_by_email(client, email):

    user = client[DB_NAME].users.find_one({
            'email': email
    })

    return user

# function to get all categories
def get_all_categories(client):

    all_cat = client[DB_NAME].categories.find()

    return all_cat

# function to get reviews in certain category
def get_reviews_by_cat_id(client, cat_id):

    reviews = client[DB_NAME].user_reviews.find(
        {
            'categories.category_id':ObjectId(cat_id)
        }
    )

    return reviews


# function to get category by its id 
def get_category_by_id(client, cat_id):

    current_cat = client[DB_NAME].categories.find_one({
        '_id': ObjectId(cat_id)
    })

    return current_cat


# function to get reviews by user id
def get_review_by_userid(client, user_id):

    reviews = client[DB_NAME].user_reviews.find(
        {
            'user_id': ObjectId(user_id)
        }
    )
    
    return reviews


def get_review_by_review_id(client, review_id):

    review = client[DB_NAME].user_reviews.find_one({
        '_id': ObjectId(review_id)
    })

    return review


def delete_review_by_id(client, review_id):

    client[DB_NAME].user_reviews.delete_one({
        '_id': ObjectId(review_id)
    })

def search_by_query(client, search_str):

    results = client[DB_NAME].user_reviews.find({
      'product_name': { 
          '$regex': search_str,
          '$options': 'i'
        }
    })

    return results


def update_review_by_id(client, review_id, user_id, title, posted, product_name, product_brand, country_of_origin, rating, review, image, cat_to_add):

     client[DB_NAME].user_reviews.update_one({
        '_id': ObjectId(review_id)
        },
        {
            '$set': 
            {
                'title': title,
                'user_id': ObjectId(user_id),
                'posted': posted,
                'product_name': product_name, 
                'product_brand': product_brand, 
                'country_of_origin': country_of_origin,
                'categories': cat_to_add,
                'rating': rating,
                'review': review,
                'image': image

            }
        }
    )