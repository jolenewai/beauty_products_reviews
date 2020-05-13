# Pretty Good 
<img src="Pretty_Good_Screenshot.png" style="margin:0">

**Pretty Good** is a informal website that allow consumers to freely post their honest reviews on any type of beauty products. The aim is to assure the audience that there's no paid review here. It serves as a information exchange platform. Users may read the reviews for free and without the needs to login. However, to add a review, registation and login are required so that the user may edit or delete their review(s) in the future.
 
You may access the deployed website from [here](https://beauty-reviews-app.herokuapp.com/)

## UX/UI
 
This website targets to girls/ladies who are looking for 100% consumers based reviews on beauty products including skin care, cosmetics, body care, hair care and also products for men. 

### User Stories:
- Susan, Female, 35, looking for skin foundation with good reviews for herself, she can perform a search for foundation with the search branch
- Alicia, Female, 26, looking for a present for her boyfriend, she can browse through the reviews by clicking on the Category "For Men" that appears on every page
- Jojo, Female, 25, likes to share her reviews of beauty products that she use, she can register herself and login to add a reviews

The wireframes and mockup of the website can be accessed here:
- For [Desktop](https://xd.adobe.com/view/b6c63e20-4de9-4ee9-6413-0442a04b7214-c0f7/) 
- For [Mobile](https://xd.adobe.com/view/6d136527-3e95-45ec-5ecf-4f18ca32edfb-1b22/)

The ER diagrams can be accessed [here](https://drive.google.com/open?id=119lge3_tqhiwuxFHjstO4N5Cng6vkmdG)


### Navigation

- Users can access to the reviews of different categories by clicking on the main navigation that appears on each of the page. 
- Search bar, Login and Add A Review link are on sticky-top bar on the page which enable users to access to them at any point of the website

### Colour Scheme

Different shades of pink and black are used in this website as the intended users are mainly female.

### Typography

- "Amatic SC", a handwritten style font is used for Headers, Navigation and Form Labels to make the website looks casual and less formal
- "Avenir", a sans serif font is used for other contents, as it has better readability on smaller fonts


## Features

### Existing Features
- Landing Page, greet users with choice of "Read Reviews" or "Add A Review", there's also option to login or register
- Home Page, list out the "Latest Reviews" in each of the categories
- Seach, allow user to perform search on keywords in "Product Name" and "Review" attributes in "Reviews" document
- All, perform the same as the Home Page 
- Skin Care, displays all the reviews in "Skin Care" Category 
- Cosmetics, displays all the reviews in "Cosmetics" Category
- Body Care, displays all the reviews in "Body Care" Category 
- Hair Care, displays all the reviews in "Hair Care" Category
- For Men, displays all the reviews in "For Men" Category
- Login, allow user to login
- Register, allow user to register before they can login
- Add A Review, allow login user to add a review to the website
- My Reviews, list out all the reviews the login user has posted and allow them to delete and edit from there
- Edit Profile, allow login user to edit their personal information registered with the website
- Review Details, display all information for selected review, user can view reviewer's basic info by clicking on their name


### Features Left to Implement
- To allow users to change the sorting of the reviews (currently it's sorted automatically by Descending order of Posted Date)
- To allow users to edit/delete their review/s from any page after they have login

## Technologies Used

* HTML 
* CSS
* Javascript 
* [JQuery](https://jquery.com/) to simplify DOM manipulation
* [Adobe XD](https://www.adobe.com/sea/products/xd.html) for wireframing and UI design 
* [Bootstrap version 4.4](https://getbootstrap.com/) for toggle of tabs navigation  
* [MongoDB](https://www.mongodb.com/cloud/atlas) for storing data on database 
* [Flask version 1.1.2](https://flask.palletsprojects.com/en/1.1.x/) to create this appears
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/) for user login functions
* [pymongo](https://pymongo.readthedocs.io/en/stable/) to communicate with MongoDB in Python

## Plugins

The animation on the website are created using the following plugin created by [michalsnik](https://github.com/michalsnik/aos)

* Animate on Scroll [AOS](https://michalsnik.github.io/aos/) for animations on the cards
* [Uploadcare API](https://uploadcare.com/) for uploading images on a separate cloud

## Testing

Testing process conducted as follows:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

1. User Registration
    1. On the home page, click on Register
    2. Try to submit the empty form and verify that error messages about the required fields appear and highlighted in red

2. Login 
    1. On one of the review page, click on Login
    2. Try to submit the empty form and verify that error messages about the required fields appear and highlighted in red
    3. Try to submit the form with an invalid email address and verify that it is an invalid login
    4. Try to submit the form with a wrong password and verify that it is an invalid login
    5. Try to submit the form with all inputs valid and verify that the redirection is successful and the navigation changed from "Login" to "Logout"

3. Add A Review (before login)
    1. On home page, click on Write A Review
    2. The page will be redirected to Login
    3. Repeat steps in Login testing

4. Add A Review (after login)
    1. On one of the review page, click on My Account, then Add A Review on My Account Page
    2. Try to submit the empty form and verify that error messages about the required fields appear and highlighted in red
    3. Try to submit the form with all inputs valid and verify the review has been added when redirected to My Reviews page

5. Update A Review 
    1. On My Reivews page, click on the edit icon beside the title of the review
    2. Verify that information from the database are presented in the form inputs, try to change one of the field and verify that the field is updated after submit the form
    3. Try to change image and submit and verify that the image is updated after submit the form

6. Delete A Review
    1. On My Reviews page, click on the delete icon beside the title of the review
    2. Verify that confirmation message is displayed and try to press confirm and verify that the review is deleted when redirected to My Reviews page

7. Update Profile
    1. On My Account page, click on the Update Profile link in login user section
    2. Verify that information from the database are presented in the form inputs, try to change one of the field and verify that the field is updated after submit the form
    3. Try to change image and submit and verify that the image is updated after submit the for

8. Search 
    1. On one of the review page, type in any keyword in the search bar, choose one of the search options from the select box, repeat with the other 2 options and verify that the matching results appear in Search Result page
    2. On Search Result page, apply filter with one of the product category and rating, and verify that the matching results displayed

9. Browsing Reviews by Category on Main Navigation
    1. Click on each button and verify that the matching reviews are displayed

10. Responsivenesss
    1. This website is responsive on various devices such as Desktop, iPad (works better in vertical), Mobile Phone

11. Unsolved bugs/problems 
    1. Bootstrap form validation unable to enforce at least one of the multiple checkboxes to be selected
    2. Product name is not able to be enforced to standardised, for example, different user will enter a different name for the same product, this problem is not resolveable unless we build a database with all the products stored on the database.
    3. There's horizontal overflow on the page that displays all the product categories on iPad horizontal format due to the size of the card column


## Deployment

This website is deployed on [Heroku](https://www.heroku.com). The deployed website can be accessed [here](https://beauty-reviews-app.herokuapp.com/)

- All the requirements for the app to run is listed in requirements.txt which will be automatically run by Heroku when deployed
- Debug is set to False after the website is launched
- All public keys and private keys for the following need to be set in Heroku Config Vars for the app to run:
    1. Uploadcare API
    2. MongoDB URI and Dabatase Name
- App will run automatically on Heroku after deployment without the need to manually run the app as we were developing


## Credits

### Content
- The text for the reviews was copied from the [MakeupAlley](https://www.makeupalley.com/)

### Media
- The photos used in this site were obtained from [MakeupAlley](https://www.makeupalley.com/)
- The vector graphics used in the background were obtained from [Freepik](https://www.freepik.com/)

### Acknowledgements
- I received inspiration for this project from beauty reviews websites
