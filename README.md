[![Build Status](https://travis-ci.org/sweetmentor/Str4-eCommerce-App.svg)](https://travis-ci.org/sweetmentor/Str4-eCommerce-App)

###This Project meant for Education purpose only.
### The code is available at https://github.com/sweetmentor/Str4-eCommerce-App and its running [here](https://chestergreen-ecommerce-app.herokuapp.com/)

# Chester Appliances.

## Overview:

This is a Django E-commerce App for Stream 4 Project.
The website has various pages to showcase the company products from home and products page which list out all the products available for sale, to product detail page which gives full detail about each product. It also has the blog session that both the admin and customer have the previledge to write about useful advice and information for the company customers, though the blog needs admin approval to get added but can be editted by the author thereafter. The site also avails customer ability to review and rate products based on their experience to help other customers make a choice.

## UX
This website is for a household appliances and tech merchant, the aim is to have a standard e-commerce website to present the company products to the world and to make it a place where customers can come to for useful tips and advice on maitenance of appliances in form of a blog. The website has been built with those needs in mind. Both return and new customer can browse the products, add it to basket and make payment with Stripe for easy flow of transaction. Registered users have the previledge to review products, have a profile on site and ability to add post to the website blog subject to admin approval.  
Balsamiq was used to wireframe the site whice served as guide through out the whole process. The files are included in the wireframe folder of this project and also available [here](https://balsamiq.cloud/st8pqbr/py93qxc/r446E) for a limited period. The website is also optimised for both mobile and desktop devices for good user experience.

## Features

* Home page showcase featured items for the day and the customer can from there make a purchase or go to products page to see all the available products. 
* A product can be selected to view details before added to basket or can be added to basket from products page and home page. 
* Customer can search the site for a particular product through search feature on home, products and cart pages to see if its available.
* Product details shows available reviews and rating for the product to help the buyer makes informed decision.
* Both registered and new customers can add product to basket and securely make payment with Stripe. Stripe was used because customer do not have to leave the site before making payment unlike other mediums like paypal.
* Registered and authenticated customers have certain priviledges over others which includes ability to review and rate products, add new post to the blog and edit their existing blogs.
* Blog is available for every visiting customers to read.

## Tech Used

This app is built usin Django 2 framework, uses PYTHON3 to route viewers through the site and it's styled with Bootstrap and CSS. 
### Some of the tech used includes:
* DataBase
Sqlite3 to run the project locally and AWS to run on production. 
* Django
* HTML and Python
Base languages used to create app
* CSS
Used to style the app.
* Bootstrap
This was used to give the project a simple, responsive layout with lots of defaults modified.
* Cloud 9 - Used to code the project.
* Javascript - For form submission.
* Github and Github Pages - Used to track the progress of the project, and host the site for submission.

## Testing

* A coverage Test conducted with a report of 73% available [here](https://str4-ecommerce-sweetmentor.c9users.io/htmlcov/index.html) and in test_report folder of this project.
* All code used on the site has been tested to ensure everything is working as expected, by making demo purchase from adding item to cart, deleting from cart to making payment using Stripe.
* Anonymous User trying to add post from the browser by hacking the https should throw a "ValueError at /blogs/new/ Cannot assign "<SimpleLazyObject: <django.contrib.auth.models.AnonymousUser object at 0x7fc3cfdc7da0>>": "Post.author" must be a "User" instance".
* Site viewed and tested in the following browsers:
Google Chrome and Safari
* Pages were inspected to test responsiveness on both mobile and desktop.

## Deployment

The project is hosted on GitHub and set to run on production so using static folder on AWS. The master branch is deployed and running on Heroku.  

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
These are the things you need to install

* Firstly you will need to clone this repository by running the git clone <https://github.com/sweetmentor/Str4-eCommerce-App> command
* Install django verson 2.0 on your system and you can get it [here](https://www.djangoproject.com/download/)
* sudo pip3 install pillow and django-forms-bootstrap;
* please ensure DJANGO_SETTINGS_MODULE is set to run on local and these two lines below are in settings local file, otherwise it would be crashing. 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SYSTEM_EMAIL = 'admin@example.com'
* The project can now run on localhost.
* requirement.txt file is part of the cloned repository, it contain every other thing needed to run the project locally.
* Feel free to make changes to the code and if you think it belongs in here then just submit a pull request.

## Credits

### Media

* The photos used in this site were obtained randomly from google images.
* Logo belongs to Chester Entertainment Bar obtained via google images.

### Codes

* Some of the codes used for this project are results of google search and classroom based work adapted and refactored to meet the project need.
