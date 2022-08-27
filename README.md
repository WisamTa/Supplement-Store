## Table of Content
* [User Experience Design (UX)](#User-Experience-Design)
    * [The Strategy Plane](#The-Strategy-Plane)
        * [User stories](#User-Stories)
    * [The Scope Plane](#The-Scope-Plane)
    * [The Skeleton Plane](#The-Skeleton-Plane)
        * [Wireframes](#Wireframes)
        * [Database Design](#Database-Design)
    * [The Surface Plane](#The-Surface-Plane)
        * [Design](#Design)
            * [Colour Scheme](#Colour-Scheme)
            * [Typography](#Typography)
            * [Imagery](#Imagery)
    * [Differences to Design](#Differences-to-Design)
    * [Features Implemented](#Features-Implemented)
    * [Existing Features](#Existing-Features)
* [Technologies Used](#Technologies-Used)
* [Testing](#Testing)
* [Deployment](#Deployment)
  * [Code](#Code)
  * [Acknowledgements](#Acknowledgements)

#### Project goals<br>

* The structure of the site is designed to be simple and easy to use. It has a good balance of images and content as not overload the user, 
while allowing the user to have all the information they require, and not leave the user needing more information to carry out all steps needed on the site.
* Create a website that uses Stripe payments ans amazon web services
* To make a full-stack site that uses HTML, CSS, JavaScript, Python + Django.
* Create a website that uses a relational database. (Postgres)
* To make a full-stack site based around business logic used to control a centrally-owned database.

## USER EXPERIENCE

### USER STORIES

#### CLIENT GOALS

* The site needs to be easily accesible.
* The navigation menu needs to be simple to use on a range of devices, including desktop, tablet and mobile.
* To be able to create a user account.
* It should be easy to register, login and logout.
* The site should be informative and all the text should be easy to read.
* The images should be clear and hoght quality with a fit logo on the product.

#### FIRST TIME VISITORS

* I want the site to be easy to understand
* I want the user how to navigate throughout the site easily.
* I want the user to be able to create an account easily and safely
* I want the content to be easily read and understandable.
* I want the checkout process to be straightforward and easy to understand.
* I want images to be clearly visible.

#### RETURNING USER

* To be able to login using their own personal information.
* To Recommend the site to friends and family.
* To make new purchases with saved details.

#### ADMIN USER

* I want the admin to be able to create an account.
* I want the admin to be able to add a product.
* I want the admin to be able to edit a product.
* I want the admin to be able to delete a product.
* All these steps should be either using fixtures data or adding or delete manually 

## Technologies Used
### Languges<br>
* [HTML5](https://en.wikipedia.org/wiki/HTML)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Pyhton3](https://www.python.org/)
---
### Frameworks and Libraries<br>
* [jQuery](https://jquery.com/)  
* [Bootstrap 4](https://getbootstrap.com/)
* [Google Fonts](https://fonts.google.com/)
* [Django](https://www.djangoproject.com/)
* [Pip3](https://pip.pypa.io/en/stable/)
* [Postgressql](https://www.postgresql.org/)
* [FontAwesome](https://fontawesome.com/)
---
### All Others<br>
* [Stripe](https://stripe.com/en-se)
    * used for the payments system.
* [GitHub](https://github.com/)
    * GithHub is the hosting site used to store the source code for the Website.
* [RandomKeygen](https://randomkeygen.com/)
    * used to create a strong password for required (Secret Key).
* [Git](https://git-scm.com/)
    * Git is used as version control software to commit and push code to the GitHub repository where the source code is stored.
* [Heroku](https://dashboard.heroku.com/apps)
    * Heroku was used to deploy the live website.
* [AWS](https://aws.amazon.com/)
    * A cloud application to hold media files.
* [Font Awesome](https://fontawesome.com/)
    * All the Icons displayed throughout the website are Font Awesome icons.
* [Favicon](https://favicon.io/)
    * Favicon.io was used to make the site favicon. 
* [Techsini](http://techsini.com/multi-mockup/index.php)
    * Multi Device Website Mockup Generator was used to create the Mock up image in this README. 
* [Privacy Policy](https://www.privacypolicygenerator.info/)
    * used to generate a privacy policy.
* [Lighthouse](https://developers.google.com/web/tools/lighthouse)
    * Used for performance review.
* [L3dsellers](https://www.3dsellers.com/)
    * Sku Generater

# Deployment

## Github
  * Created a new GitHub repository page using the 'Code Institute Template'.
  * Opened the new repository by clicking on the 'Gitpod' button.
  * Installed the relevant apps and packages needed to deploy to HEROKU.

## Django and Heroku

Deployment of my project was scaffolded using the Code Institute's [Django Blog Cheatsheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf). Furthermore, the following steps were taken to deploy the project to Heroku from the GitHub repository:

1. Create the Heroku App:
    - Before creating the Heroku app make sure your project has the following files:
        - requirements.txt to create this type the following within the terminal: **pip3 freeze > requirements.txt**.
        - Procfile to create this type the following within the terminal: **python run.py > Procfile**.
    - Select "Create new app" within Heroku.
2. Attach the Postgres database:
    - Search "Postgres" within the Resources tab and select the Heroku Postgres option.
3. Create the settings.py file:
    - In Heroku navigate to the Settings tab, click on Reveal Config Vars and copy the DATABASE_URL.
    - Create a SECRET_KEY value within the Reveal Config Vars in Heroku.
    - Add the DATABASE_URL value and your chosen SECRET_KEY variable.
    - Run the following command in your terminal **python3 manage.py migrate**.
    - Add the following sections to your settings.py file:
        - STATICFILES_STORAGE
        - STATICFILES_DIRS
        - STATIC_ROOT
        - MEDIA_URL
        - DEFAULT_FILE_STORAGE
        - TEMPLATES_DIR
        - Update DIRS in TEMPLATES with TEMPLATES_DIR
        - Update ALLOWED_HOSTS with ['app_name.heroku.com','localhost']
4. Store Static and Media files in Amazon and Deploy to Heroku:
    - Create a file named "Procfile" in the main directory and ass the following: [web: gunicorn project-name.wsgi].
    - Login to Heroku within the terminal window using **heroku login -i**
    - Run the following command in the terminal window: **heroku git:remote -a your_app_name_here**. By doing this you will link the app to your GidPod terminal.
    - After linking the app you can deploy new versions to Heroku by running the command **git push heroku main**.
  
[Back to top ⇧](#supplement-store1)

***