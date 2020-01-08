
[![Build Status](https://travis-ci.org/Deirdre18/yoda-design-ecommerce-app-Milestone4-project.svg?branch=master)](https://travis-ci.org/Deirdre18/yoda-design-ecommerce-app-Milestone4-project)

<h6>Deirdre Weldon</h6>

<h1>Full Stack Framework Milestone - An ecommerce project using Django and Python</h1>

[View Project](https://yoda-design.herokuapp.com/)

## **Purpose of Project**


## **UX Design**

[Image of Products Page](https://github.com/Deirdre18/yoda-design-ecommerce-app-Milestone4-project/blob/master/UX%20Design/Products%20Page.png)

[Image of Checkout Mobile View Page](https://github.com/Deirdre18/yoda-design-ecommerce-app-Milestone4-project/blob/master/UX%20Design/checkout_page.png)


GARRET'S FIVE PLANS OF UX DESIGN:-

### - Strategy (The goal)

### - Scope (What tasks can be done)

### - Structure (Plan or Flow of Interactions)

### - Skeleton

### - Surface

## **Quick Tutorial**

## **Features Overview**

## **Existing Features**

## **Features that could be implemented in future versions**

## **Testing**

### - General Testing
After some time testing both debug and alternating deployment in production mode, I was able to understand how static files worked in both modes. In production mode, debug should be off for security reasons, however this then can cause conflict with displaying static and media files. As I installed Whitenoise, I added ''whitenoise.runserver_nostatic'in my installed apps in settings.py. I refered to [Whitenoise docs]("http://whitenoise.evans.io/en/stable/django.html"). This meant that static file handling was taken over by Whitenoise instead of Django and so I could view static files in production mode locally. However when I deployed to Heroku, an error occurred saying that I should add DISABLE_COLLECTATIC=1 into config variables in Heroku, which I did.  

On further testing I worked out a way to test in debug mode, whilst commenting out STATIC_ROOT = os.path.join(BASE_DIR, 'static') in base.html file, and uncommenting it when deploying to Heroku. In this way I can test in debug mode and view all static and media files and deploy to Heroku confident that static/media files will be displayed in production mode.

### - Django Built-in Tests

I tested products using tests.py, the code was as follows. After running python3 manage.py test products, all tests passed.

from django.test import TestCase
from .models import Product

class ProductTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model. In order to run tests, 'test' must be defined at start.
    """
    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')

### - Travis Testing

Travis Continuous Integration has been passing tests since I first started this project. The Travis link is at the top of README. I have found it very useful in aligning integrated testing with development.

### - Manual testing

Manually tested login, register, add products to cart, view blogs, profile and login status, search bar.

### - Developer tools

Used Chrome and Firefox developer tools to view app in responsive mode and debug throughout developing this project.

### - Testing STRIPE

Tested STRIP payments on checkout using testing card 42424242424242 CVV 111 (or any 3 digits). This worked and got message saying "payment successful". On trying other varients of testing card number I got some interesting messages. Instead of inputting the 16 digit test card number, if I put in the same numbers but had 19 digits, I got no messages displayed but got email from STRIPE saying that the charging  API used for testing purposes doesn't cover SCA (strong customer authentication) and as such testing doesn't support SCA or 2-factor. authentication.

## **Databse schema**:

### Postgres Database Schema Explorer in heroku

products_prodct                     auth_user

description     text                date_joined      timestamptz
id              int4                email            varchar
image           varchar             first_name       varchar
name            varchar             id               int4
price           numeric             is_active        bool
                                    is_staff         bool
                                    is_superuser     bool
                                    last_login       timestamptz
                                    last_name        varchar
                                    password         varchar
                                    username         varchar

django_admin_log                      django_session

action_flag           int2            expire_date   timestamptz
action_time           timestamptz     session_data  text
change_message        text            session_key   varchar
content_type_id       int4
id                    int4
object_id             text
object_repr           varchar
user_id               int4

checkout_order                        posts

country               varchar         content           text
county                varchar         created_date      timestamptz
date                  date            id                int4
full_name             varchar         order_id          int4
id                    int4            product_id        int4
phone_number          varchar         quantity          int4
postcode              varchar
street_address        1varchar
street_address        2varchar
town_or_city          varchar

checkout_orderlineitem








idint4
imagevarchar
published_datetimestamptz
tagvarchar
titlevarchar
viewsint4

## **Version Control (GitHub)**

I continuously pushed to GitHub with useful comments in every commit. It was therefore easier to track back to any problems.

## **Deployment**

I deployed this project to Heroku Platform, which is a free cloud based platform. I provisioned PosgressSQL add-on (free hobby version) on Heroku. I connected my deployment to GitHub, so that whenever I pushed to GitHub, the deployed app was also updated to the current version. In Heroku, I configured variables, such as SECRET_KEY, STRIPE_PUBLISHABLE, STRIPE_SECRET, DISABLE_COLLECTSTATIC=1, DJ_DATABASE_URL.

This project is developed on Heroku Platform - [Yoda Design](https://yoda-design.herokuapp.com/)

## **How I developed this project and how to run the code for this project**

## **Difficulties I came across**

I encountered difficulty using STRIPE at one point, as I had changed base.html file and moved jquery script to bottom of page, which is where it usually goes. However for STRIPE to work and a payment to be accepted (using testing card 4242 4242 4242 4242 and CVV, which can be any three digits) - jquery needs to go at the top of base.html file. I used firefox developer tools to debug and saw a jquery reference error relating to this.

## **Credits**

For some code I used, I give credit to fellow student (Lucas Suarez) -[Django-tech-ecommerce](https://github.com/Code-Institute-Submissions/django-tech-ecommerce-app).

I also give credit to Code Institute for their solutions on GitHub - [GitHubSolutions](https://github.com/Code-Institute-Submissions/django-tech-ecommerce-app)

## **Content**

## **Code**

## **References/Acknowledgement**
Referred to these websites to look for images:-

[Yoda Mousepad](https://www.amazon.com/Abystyle-STAR-WARS-Mousepad-Yoda/dp/B01BFGCJ38)

[Mandalorian products](https://money.com/baby-yoda-toys-t-shirt-mandalorian-disney-plus/)

[Baby Yoda Dolls](https://www.eonline.com/news/1099401/baby-yoda-dolls-are-here-but-there-s-a-catch)

[Yoda Lego](https://www.lego.com/en-us/kids/sets/star-wars/yoda-495867f9321e4189a2e241fc88bafd3e)

[Yoda gifts Amazon](https://www.amazon.com/slp/yoda-gifts/7hw5autakufk8oo)

[Star Wars Products](https://www.liveabout.com/yoda-in-star-wars-2957947)

For help with making jumbotron responsive across different sized devices, I referred to this [Jumbotron Responsiveness](https://stackoverflow.com/questions/29592302/bootstrap-responsive-jumbotron/50710437)

## Licence
Copyright (c) Deirdre Weldon

Written with [StackEdit](https://stackedit.io/)
