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

[Back to top ⇧](#ginamore)

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

[Back to top ⇧](#supplemet-store1)

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

[Back to top ⇧](#supplemet-store1)

