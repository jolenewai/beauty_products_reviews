# Pretty Good 

**Pretty Good** is a informal website that allow consumers to freely post their honest reviews on any type of beauty products. The aim is to assure the audience that there's no paid review here. It serves as a information exchange platform. Users may read the reviews for free and without the needs to login. However, to add a review, registation and login are required so that the user may edit or delete their review(s) in the future.
 
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


### Features Left to Implement
- To allow users to change the sorting of the reviews (currently it's sorted automatically by Descending order of Posted Date)

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

* Animate on Scroll [AOS] (https://michalsnik.github.io/aos/)

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for the reviews was copied from the [MakeupAlley](https://www.makeupalley.com/)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
