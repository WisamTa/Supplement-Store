[Here is a link to the live final project](https://supplement-store-3yk1-onrender-com.onrender.com)
## INITIAL IDEA

My initial idea behind Supplement Store is to make an eCommerce site about food supplement, where anyone will be able to purchase their desirable goods
The user will be able to navigate easily throughout the site, and the site will be fully accessible for all users.

## FINAL DESIGN

![Final project image](https://github.com/WisamTa/Supplement-Store/blob/main/media/readme_images/FireShot%20Capture%20002%20-%20Multi%20Device%20Website%20Mockup%20Generator%20-%20techsini.com.png)
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
* [Marketing](#Marketing)


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

# Favicon

A simplistic favicon was created in the shape of a S letter, using simple lines

![Favicon Icon](https://github.com/WisamTa/Supplement-Store/blob/main/static/favicon/android-chrome-512x512.png)

### Features Implemented
##### Create Profile
* Users are able to:
  * Create a profile to save their orders and personal information
  * Confirm their details are correct via email verification
  * Store details for faster checkout
  

##### Log in to Profile
* Users are able to:
  * Log in to profile to see their orders and personal information
  * Edit personal information if required
  

##### Products Page
* Users are able to:
  * Products displayed and searchable to all users.
  * Sort products by A-Z, Name, Category, Price, Rating.
  * Price of product
  * See rating of product
  

##### Product Details Page
* Users are able to:
  * Click the products to find out more information including
  * Name,  price, SKU, category, ratings
  * Add products to bag to buy
  * See reviews of products and also review the products if logged in

* Super users are able to:
  * Add, edit and delete products
  * Delete reviews
  

##### Products Management
* If the user is a super user they can:
  * Add a product and image of product
  * Edit a product
  * Delete a Product

##### Bag
* Users are able to:
  * Adjust number of products in bag if they require
  * Find out delivery costs
  * Find out how much more they need to spend to get free delivery
  * Clearly see the total of their items by quantity and grand total
  

##### Checkout
* Users can:
  * Save time as personal details pulled from profile page if user is logged in
  * Save their delivery information to their profile
  * Clearly see how much they will be charged for their items and delivery
  

* Logged in users can:
  * Add a Review
  
 ##### Navigation

Header

* All users can:
  * Navigate to home, all products, all categories, bag pages, contact page, Faq page

* Users logged in can access:
  * Profile pages, review page

* Users not logged in can:
  * Access log in and register pages

   ##### Navigation
Bolg

  * All user can:
   * Creat a post comment and delete 

   ### Features For Furher Implementation 
   * Adding functionality for the most viewd or most popuale products


### Error Pages

#### 400.html

 * 400 page created to redirect users back to the main site in case of an bad request error.


#### 403.html

 * 403 page created to redirect users back to the main site in case they try to access a page they are not authorised to

#### 404.html

 * 404 page created to redirect users back to the main site in case of an error


#### 500.html

 * 500 error page created to redirect users to the main site after a server error

### The Skeleton Plane
#### Wireframes
* Desktop size wireframes can be viewed [here](https://github.com/WisamTa/Supplement-Store/tree/main/docs/desktop_wireframes)<br>
* Tablet size wireframes can be viewed [here](https://github.com/WisamTa/Supplement-Store/tree/main/docs/tablet_wireframes)<br>
* Mobile size wireframes can be viewed [here](https://github.com/WisamTa/Supplement-Store/tree/main/docs/mobile_wirfreames)<br>

### Database Design

![Database Design](https://github.com/WisamTa/Supplement-Store/blob/main/media/readme_images/database_schema%20(2).png)

## TECHNOLOGIES

### LANGUAGES

<img src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-plain-wordmark.svg" alt="HTML logo" width="50px" height="50px" /> <img src="https://github.com/devicons/devicon/blob/master/icons/css3/css3-plain-wordmark.svg" alt="CSS logo" width="50px" height="50px" /> <img src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-original.svg" alt="JavaScript logo" width="50px" height="50px" /> <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" alt="Python logo" width="50px" height="50px" /> 

## FRAMEWORKS AND LIBRARIES
<img src="https://github.com/devicons/devicon/blob/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="Bootstrap logo" height="50px" width="50px" /> <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" alt="Django logo" width="50px" height="50px" />
- [Django](https://www.djangoproject.com/) -  Used in the development of this project. Main python Framework.
    - The following python modules were used on this project:
```
asgiref==3.5.2
backports.zoneinfo==0.2.1
boto3==1.21.18
botocore==1.24.18
chardet==4.0.0
dj-database-url==0.5.0
Django==3.2
django-allauth==0.41.0
django-countries==6.0
django-crispy-forms==1.14.0
django-storages==1.13.1
gunicorn==20.1.0
jmespath==0.10.0
oauthlib==3.2.0
Pillow==9.0.1
psycopg2==2.9.3
psycopg2-binary==2.9.3
pylint-django==2.5.3
pylint-plugin-utils==0.7
python3-openid==3.2.0
pytz==2022.2.1
requests-oauthlib==1.3.1
s3transfer==0.5.2
sqlparse==0.4.2
stripe==2.67.0
```

### PROGRAMS

<img src="https://github.com/devicons/devicon/blob/master/icons/git/git-plain-wordmark.svg" alt="Git logo" width="50px" height="50px" />

[Git](https://git-scm.com/) was used for version control by using the Gitpod terminal to add and commit to Git and push to Github.

<img src="https://github.com/devicons/devicon/blob/master/icons/github/github-original-wordmark.svg" alt="GitHub logo" width="50px" height="50px" />

[GitHub](https://github.com/) was used to store all the code for this project after being pushed from GitPod, which I also used a Project board to 
keep track of the project development by splitting tasks into smaller and more managable sections.

<img src="https://github.com/devicons/devicon/blob/master/icons/heroku/heroku-original-wordmark.svg" alt="Heroku logo" width="50px" height="50px" />

[Heroku](https://id.heroku.com) was used for deployment of the live site.

<img src="https://github.com/devicons/devicon/blob/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="AWS logo" width="50px" height="50px" />

[AWS](https://aws.amazon.com/) was used for storing static files and media images for this project.

<img src="https://github.com/devicons/devicon/blob/master/icons/firefox/firefox-original-wordmark.svg" alt="Firefox logo" width="50px" height="50px" />

[Firefox Developer](https://www.mozilla.org/en-GB/firefox/developer/) Tools was used for troubleshooting and trying new visual changes without it affecting the current code.

### Other

* This video help me when I migrated the new app successfuly but could not find it on the live site due to a programming error
  * [Here](https://www.youtube.com/watch?v=6DI_7Zja8Zc)  

#### GitPod

[GitPod](https://gitpod.io) was used as an IDE whilst coding this site.
* [Favicon](https://favicon.io/)
    * Favicon.io was used to make the site favicon. 
* [Techsini](http://techsini.com/multi-mockup/index.php)
    * Multi Device Website Mockup Generator was used to create the Mock up image in this README. 
* [Privacy Policy](https://www.privacypolicygenerator.info/)
    * used to generate a privacy policy.
* [L3dsellers](https://www.3dsellers.com/)
    * Sku Generater
* [TempMail](https://temp-mail.org/en/)
    * Random E-mails Generator
* [Techsin](https://techsini.com/multi-mockup/index.php)
    * The mockup Screenshot

### Database Design

![Database Design](readme_images/database_schema/database_schema.png)

# The Supplement-Store - Testing

Back to my main README.md click [here](https://github.com/WisamTa/Supplement-Store/blob/main/README.md)
<br>


## Table of Content


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
  
[Back to top ???](#supplement-store1)

***

### Allauth

Within the Django Framework, Allauth a package that handles registration and login details was installed. More information on how this was installed can be found here: [Django Allauth Installation](https://django-allauth.readthedocs.io/en/latest/installation.html).
****

# AWS S3 Bucket Set Up

The deployed site uses AWS S3 Buckets to store the webpages static and media files. More information on how you can set up an AWS S3 Bucket can be found below:

1. Create an AWS account [here](https://portal.aws.amazon.com/billing/signup#/start/email).
2. Login to your account and within the search bar type in **S3**.
3. Within the S3 page click on the button that says **Create Bucket**.
4. Name the bucket and select the region which is closest to you.
5. Underneath **Object Ownership** select **ACLs enabled**.
6. Uncheck **Block Public Access** and acknowledge that the bucket will be made public, then click **Create Bucket**.
7. Inside the created bucket click on the **Properties** tab. Below **Static Website Hosting** click **Edit** and change the Static website hosting option to **Enabled**. Copy the default values for the index and error documents and click **Save Changes**.
8. Click on the **Permissions** tab, below **Cross-origin Resource Sharing (CORS)**, click **Edit** and then paste in the following code:

  ```
    [
        {
            "AllowedHeaders": [
            "Authorization"
            ],
            "AllowedMethods": [
            "GET"
            ],
            "AllowedOrigins": [
            "*"
            ],
            "ExposeHeaders": []
        }
    ]
  ```

9. Within the **Bucket Policy** section. Click **Edit** and then **Policy Generator**. Click the **Select Type of Policy** dropdown and select **S3 Bucket Policy** and within **Principle** allow all principals by typing *.
10. Within the **Actions** dropdown menu select **Get Object** and in the previous tab copy the **Bucket ARN number**. Paste this within the policy generator within the field labeled **Amazon Resource Name (ARN)**.
11. Click **Add statement > Generate Policy** and copy the policy that's been generated and paste this into the **Bucket Policy Editor**.
12. Before saving, add /* at the end of your **Resource Key**, this will allow access to all resources within the bucket.
13. Once saved, scroll down to the **Access Control List (ACL)** and click **Edit**.
14. Next to **Everyone (public access)**, check the **list** checkbox and save your changes.

[Back to top ???](#Supplement-Store1)

# IAM

1. Search for IAM within the AWS navigation bar and select it.
2. Click **User Groups** that can be seen in the side bar and then click **Create group** and name the group 'manage-your-project-name'.
3. Click **Policies** and then **Create policy**.
4. Navigate to the JSON tab and click **Import Managed Policy**, within here search **S3** and select **AmazonS3FullAccess** followed by **Import**.
5. Navigate back to the recently created S3 bucket and copy your **ARN Number**. Go back to **This Policy** and update the **Resource Key** to include your ARN Number, and another line with your ARN followed by a /*. Below is an example of what this should look like:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "YOUR-ARN-NO-HERE",
                "YOUR-ARN-NO-HERE/*"
            ]
        }
    ]
}

```

6. Ensure the policy has been given a name and a short description, then click **Create Policy**.
7. Click **User groups**, and then the group you created earlier. Under permissions click **Add Permission** and from the dropdown click **Attach Policies**.
8. Select **Users** from the sidebar and click **Add User**.
9. Provide a username and check **Programmatic Access**, then click 'Next: Permissions'.
10. Ensure your policy is selected and navigate through until you click **Add User**.
11. Download the **CSV file**, which contains the user's access key and secret access key.

[Back to top ???](#supplemet-store1)

# Connecting AWS to Django

1. Within your terminal install the following packages by typing 

```
  pip3 install boto3
  pip3 install django-storages 
```  

2. Freeze the requirements by typing 

```
pip3 freeze > requirements.txt
```

3. Add **storages** to your installed apps within your settings.py file.
4. At the bottom of the settings.py file add the following code:

```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
    AWS_S3_REGION_NAME = 'insert-your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
```
5. Add the following keys within Heroku: **AWS_ACCESS_KEY_ID** and **AWS_SECRET_ACCESS_KEY**. These can be found in your CSV file.
6. Add the key **USE_AWS**, and set the value to True within Heroku.
6. Remove the **DISABLE_COLLECTSTAIC** variable from Heroku.
7. Within your settings.py file inside the code just written add: 

```
  AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```
8. Inside the settings.py file inside the bucket config if statement add the following lines of code:

```
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
```

9. In the root directory of your project create a file called **custom_storages.py**. Import the following at the top of this file and add the classes below:

```
  from django.conf import settings
  from storages.backends.s3boto3 import S3Boto3Storage

  class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

  class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

10. Navigate back to you AWS S3 Bucket and click on **Create Folder** name this folder **media**, within the media file click **Upload > Add Files** and select the images for your site.
11. Under **Permissions** select the option **Grant public-read access** and click **Upload**.

[Back to top ???](#supplemet-store1)

#### GMail Client

In `settings.py` change the `DEFAULT_FROM_EMAIL` to your own email address.

1. Go to your Gmail account and navigate to the `Settings` tab.
2. Go to `Accounts and Imports`, `Other Google Account Settings`.
3. Go to the `Security` tab, and scroll down to `Signing in to Google`.
4. If required, click to turn on `2-step Verification`, then `Get Started`, and enter your password.
5. Verify using your preferred method, and turn on 2-step verification.
6. Go back to `Security`, `Signing in to Google`, then go to `App Passwords`.
7. Enter your password again if prompted, then set `App` to `Mail`, `Device` to `Other`, and type in `Django`.
8. Copy and paste the passcode that shows up, this is your `EMAIL_HOST_PASS` variable to add to your environment/config variables. `EMAIL_HOST_USER` is the Gmail email address.

### Config Vars

The config/environment variables should be set up as follows:

| Key                    | Value                      |
| ---------------------- |--------------------------- |
| SECRET_KEY             | YOUR_SECRET_KEY            |
| STRIPE_PUBLIC_KEY      | STRIPE_PUBLIC_KEY          |
| STRIPE_SECRET_KEY      | YOUR_STRIPE_SECRET_KEY     |
| STRIPE_WH_SECRET       | STRIPE_WEBHOOKS_KEY        |
| DATABASE_URL           | YOUR_POSTGRES_URL          |
| AWS_ACCESS_KEY_ID      | YOUR_AWS_ACCESS_KEY_ID     |
| AWS_SECRET_ACCESS_KEY  | YOUR_AWS_SECRET_ACCESS_KEY |   
| USE_AWS                | True                       |
| EMAIL_HOST_PASS        | YOUR_EMAIL_HOST_PASSCODE   |
| EMAIL_HOST_USER        | YOUR_EMAIL_HOST_USERNAME   |

#### Where to find Config Var Key-value Pairs 

To find the values of each key:

* `SECRET_KEY:` This is a random string provided when creating the Django project and can easily be changed to ensure extra security. 
* `DATABASE_URL:` This is temporary.
* `STRIPE_PUBLIC_KEY:` Retrieved from Stripe Dashboard in the Developer's API section (Publishable key).
* `STRIPE_SECRET_KEY:` Retrieved from Stripe Dashboard in the Developer's API section (Secret key)
* `STRIPE_WH_SECRET:` Retrieved from Stripe Dashboard in the Developer's after creating an endpoint for your webhook (Signing secret).
* `EMAIL_HOST_USER:` Your email address or username.
* `EMAIL_HOST_PASS:` Your passcode from your email client.
* `AWS_SECRET_ACCESS_KEY`: From the CSV file that you download having created a User in Amazon AWS S3.
* `AWS_ACCESS_KEY_ID:` From the CSV file that you download having created a User in Amazon AWS S3.

# Stripe Payments

To handle payments within the website ensure that you have set this up a guide on how this can be done can be found [here](https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details).

# Marketing

# # Business Model

The business model used for the Supplement store would be a B2C (Business to Customer), this is due to the business selling products directly to the customer through the platform. The target market for these products are users:

- Who have access to a credir card.
- Looking to purchase popular food supplement.

Customers who are buying products from Supplement Store should be able to:

- Easily view and purchase  products from the site.
- Easily navigate and search for products they wish to purchase.


# Search Engine Optimization

The site was optimized by careful selection of keywords. The following steps were taken to do this:

1. The entire table consists of important relevant topics based upon my initial understanding of the business.
2. Using these topics a 'brain dump' of keywords was made orientated around common topics and themes within the business.


## SEO Implementations in HTML
  - Words/phrases included within semantic HTML elements were optimized using the keywords above.
  - Careful consideration was given to the words chosen to avoid 'keyword stuffing'.
  - Keywords were used within links, urls and aria labels.
  - Social network links include **rel="noopener"** to not affect the assessment of the webpage.
  - External reliable links were included within the site to improve SEO, these include:
  
## sitemap.xml

A sitemap was made to list the websites important URL's to ensure that search engines are able to easily navigate through the site and understand its structure. This was made using [XML-sitemaps.com](https://www.xml-sitemaps.com/) using the following steps:

1. Paste the URL of the deployed site into XML-sitemaps.
2. Download the XML sitemap file.
3. Drag and drop this files into the projects root folder, and ensure it is labeled **sitemap.xml**

***
## robots.txt
***

A robots.txt file was created to tell search engines where not to allowed go on the site and increase the quality of the site, ultimetly improving the SEO rating. The following steps were taken to creat this:

1. A file was added named **robots.txt**.
2. The following code was written into this file, adding in your personalised sitemap url:

```
  User-agent: *
  Disallow:
  Sitemap: YOUR_SITEMAP_URL
```

## Facebook

  * Facebook Business page 

* ![Facebook](https://github.com/WisamTa/Supplement-Store/blob/main/media/readme_images/facebook.PNG)
* ![Facebook](https://github.com/WisamTa/Supplement-Store/blob/main/media/readme_images/facebook.PNG)


## Bugs unsolved
* [Mailchimp]
 While Trying to start a mailchimp account the website had some difficulties with customers so I could not set up newsletter at the momenet 
 * ![MAilchimp](https://github.com/WisamTa/Supplement-Store/blob/main/media/readme_images/mailchimp1.PNG) 
 * ![MAilchimp](https://github.com/WisamTa/Supplement-Store/blob/main/media/readme_images/mailchimp3.PNG) 
 * ![MAilchimp](https://github.com/WisamTa/Supplement-Store/blob/main/media/readme_images/mailchimp4.PNG) 
 * ![MAilchimp](https://github.com/WisamTa/Supplement-Store/blob/main/media/readme_images/rese2.PNG) 
 * ![MAilchimp](https://github.com/WisamTa/Supplement-Store/blob/main/media/readme_images/session.PNG) 
 * I tried to copy the code for css and html and left  js for the moment untill this bug is fixed, I connected tutorial support for this matter and could not assist.
 *  also the project functionalities work just fine and tested but I have an issue with media query for the shopping bag and blog app, on blog new post is hidden on larg screen with the welcoming card but on mobil and small screen worked just fine, I tried to minuplate the media query but no thing to be really helpful, otherwise all the requiremnts for passing are satified. 
* I mocked up the final design photo whitout newsletter code and uploaded the photo to be more orginized for useres and to have nicer view.  
## Bugs solved

* During the whole project I had so many bugs solved with the help of our fellows on Slack and tutor support
but my biggest one was solved with the help of a tutorial i found on youtube, I had to log in to heoku cli from gitpod and migrate from there. I connected tutorial support for this matter and could not assist,

* also the project functionalities work just fine and tested but I have an issue with media query for the shopping bag and blog app, on blog new post is hidden on larg screen with the welcoming card but on mobil and small screen worked just fine, I tried to minuplate the media query but no thing to be really helpful 


### **Acknowledgements**<br>
* My Friend Ivan M Ulysses that I met in on of code institue hachathons for his great advice and feedback, 
* My fellow student on Slack for thier quick answers and thier helful question 
* Friends and family for testing the site, and giving me feedback.



[Back to Table of Content](#table-of-content)