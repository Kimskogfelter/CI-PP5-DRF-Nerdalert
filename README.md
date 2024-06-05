
   # Body Doodles API

Body Doodles API is the backend service used by the [Body Doodles Application](https://github.com/Gareth-McGirr/body-doodles).
<hr>
<br>

## Table of Contents
* [Development Goals](#Development-Goals)
* [Agile Planning](#Agile-Planning)
    * [Epics](#Epics)
    * [User Stories](#User-Stories)
* [API End Points](#API-End-Points)
* [Future Features](#Features-Left-to-Implement)
* [Database Design](#Database-Design)
* [Security](#Security)
* [Technologies](#Technologies)
* [Testing](#Testing)
* [Deployment](#Deployment)
    * [Version Control](#Version-Control)
    * [Heroku Deployment](#Heroku-Deployment)
    * [GCP](#Google-Cloud-Platform)
    * [Run Locally](#Run-Locally)
    * [Fork Project](#Fork-Project)
* [Credits](#Credits)
  * [Content](#Content)
  * [Acknowledgements](#Acknowledgements)

## Development Goals

The goal of this API is provide a backend service to allow the Body Doodles front end application to perform, Create, Read, Update and Delete operations via the user interface.
<hr>
<br>

## Agile Planning

This project was developed using agile methodologies by delivering small features in incremental sprints. There were 3 sprints in total, spaced out evenly over three weeks.

All stories were assigned to epics, prioritized under the labels, Must have, should have, could have and assigned to sprints. "Must have" stories were completed first, "should haves" and then finally "could haves". It was done this way to ensure that all core requirements were completed first to give the project a complete feel, with the nice to have features being added should there be capacity.

The Kanban board was created using github projects and can be located [here](https://github.com/users/Gareth-McGirr/projects/1/views/1) and can be viewed to see more information on the project cards. All stories except the documentation tasks have a full set of acceptance criteria in order to define the functionality that marks that story as complete.

![Kanban](https://raw.githubusercontent.com/Gareth-McGirr/body-doodles-api/main/readme/kanban.PNG)

### Epics

**Set Up**

This Epic covers all the initial setup of the Django application and Django REST Framework in order to begin coding the features.

**Posts**

This Epic covers all API endpoint creation and database connections relating to the CRUD functionality of user posts. This includes like activity.

**Comments**

This Epic covers all API endpoint creation and database connections relating to the CRUD functionality of user comments in relation to posts.

**Profiles**

This Epic covers all API endpoint creation and database connections relating to the CRUD functionality of user created profiles. This includes following functionality.

**Artists**

This Epic covers all API endpoint creation and database connections relating to the CRUD functionality of users who register as Artists.

**Reviews**

This Epic covers all API endpoint creation and database connections relating to the CRUD functionality of Artist reviews and average rating as displayed on user profile.
<hr>
<br>

### User Stories

**By Epics** 

**Setup**

* As a developer, I need to create the base project set up so that I can build out the features.

* As a developer, I need to create the google cloud bucket and create the connection to the project so that static images can be uploaded by users.

* As a user I can create a new account so that I can access all the features for signed up users

**Artists**

* As a developer, I want to create api views for artists so that they are available to the front end

**Contact**

* As a developer, I want to create a contact model and API view so that users can contact the site owner with issues

**Posts**

* As a user, I want to be able to view edit or delete a post
* As a user, I want to able to create a post and list posts

**Profiles**

* As a developer, I want to create a new blank profile with default image when a user is created.
* As a user, I want to able to get a list of profiles

### API Endpoints

User Story:

`As a developer, I need to create the base project set up so that I can build out the features.`

Implementation:

The base project was created and a virtual environment created with all neccessary packages installed and frozen into the requirements.

The settings were also edited to hide any secret variables and set dev and production environments apart.

User Story:

`As a developer, I need to create the google cloud bucket and create the connection to the project so that static images can be uploaded by users.`

Implementation:

A google cloud bucket was created and a service account created to allow image uploads via the service account. Create and read IAM roles were givent to the service account to ensure it had only the minimum required permissions.


User Story:

`As a user I can create a new account so that I can access all the features for signed up users`

Implementation:

Django rest framework and dj_rest_auth were installed and added to the url patterns and site packages to make use of their built in authentication system.

User Story:

`As a developer, I want to create api views for artists so that they are available to the front end`

Implementation:

Endpoint: /artists/

Methods:
* POST - Used to create an artist
* GET - Used to retrieve a list of artists

Endpoint: /artists/<int:pk>/

Methods:
* GET - Used to view single artist profile
* PUT - Used to update an artist profile
* DELETE - Used to delete an artist profile

User Story:

`As a developer, I want to create a contact model and API view so that users can contact the site owner with issues`

Implementation:

Endpoint: /contacts/

Methods:
* POST - Used to create contact request
* GET - Used to get a list of contact requests

Endpoint: /contacts/<int:pk>/

Methods:
* GET - Get a single contact request
* PUT - Used to update a single contact request
* DELETE - Used to delete a contact request

User Story:

`As a user, I want to be able to view edit or delete a post`

`As a user, I want to able to create a post and list posts`

Implementation:

Endpoint: /posts/

Methods:
* POST - Used to create post
* GET - Used to get a list of posts

Endpoint: /posts/<int:pk>/

Methods:
* GET - Get a single post
* PUT - Used to update a single post
* DELETE - Used to delete a post


User Story:

`As a developer, I want to create a new blank profile with default image when a user is created.`

Implementation:

In the profiles app, a signal was created in order to create a new user profile on signup.


User Story:

`As a user, I want to able to get a list of profiles`

Implementation:

Endpoint: /profiles/

Methods:
* POST - Used to create post
* GET - Used to get a list of posts

Endpoint: /profiles/<int:pk>/

Methods:
* GET - Get a single profile
* PUT - Used to update a single profile
* DELETE - Used to delete a profile


## Database Design

![ER Diagram](https://raw.githubusercontent.com/Gareth-McGirr/body-doodles-api/main/readme/erdiagram.jpg)

## Security

A permissions class was added called IsOwnerOrReadOnly to ensure only users who create the content are able to edit or delete it.

GCP IAMS permissions for service account were added for create and read only to ensure minimum permissions needed were granted.

## Technologies

* Django
    * Main framework used for application creation
* Django REST Framework
    * Framework used for creating API
* Google Cloud Platform
    * Used for static image hosting
* Heroku
    * Used for hosting the application
* Git
    * Used for version control
* Github
    * Repository for storing code base and docs

<hr>
<br>

## Python Packages
<details open>
<summary> Details of packages </summary>

* dj-database-url==1.0.0
    * Used to parse the DATABASE_URL connection settings
* dj-rest-auth==2.2.5
    * Used with auth system
* Django==4.1.1
    * Main framework used to start the project
* django-allauth==0.50.0
    * Used for authentication
* django-cors-headers==3.13.0
    * Used for Cross-Origin Resource Sharing (CORS) headers to responses
* django-filter==22.1
    * Used to filter API results in serializers
* django-storages==1.13.1
    * Used to help connect with the google cloud storage bucket
* djangorestframework==3.13.1
    * Framework used to build the API endpoints
* djangorestframework-simplejwt==5.2.0
    * Used with djange rest framework to create access tokens for authentication
* gunicorn==20.1.0
    * Used for deployment of WSGI applications
* Pillow==9.2.0
    * Imaging Libray - used for image uploading
* psycopg2==2.9.3
    * PostgreSQL database adapter to allow deployed application to perform crud on the postgresql db
* PyJWT==2.5.0
    * For creating the Python Json Web Tokens for authentication

Installed as package dependcies with above installations:
* asgiref==3.5.2
* autopep8==1.7.0
* cachetools==5.2.0
* certifi==2022.6.15.1
* cffi==1.15.1
* charset-normalizer==2.1.1
* cryptography==38.0.1
* defusedxml==0.7.1
* idna==3.3
* oauthlib==3.2.1
* protobuf==4.21.5
* pyasn1==0.4.8
* pyasn1-modules==0.2.8
* pycodestyle==2.9.1
* pycparser==2.21
* python3-openid==3.2.0
* pytz==2022.2.1
* requests==2.28.1
* requests-oauthlib==1.3.1
* rsa==4.9
* six==1.16.0
* sqlparse==0.4.2
* toml==0.10.2
* types-cryptography==3.3.23
* tzdata==2022.2
* urllib3==1.26.12

Auto installed as package dependencies with django-storages[GOOGLE] to aid connection to google cloud buckets for static image hosting:
* google-api-core==2.10.0
* google-auth==2.11.0
* google-cloud-core==2.3.2
* google-cloud-storage==2.5.0
* google-crc32c==1.5.0
* google-resumable-media==2.3.3
* googleapis-common-protos==1.56.4
</details>
<hr>
<br>

## Testing

Unit tests in posts app

![Post Tests](https://raw.githubusercontent.com/Gareth-McGirr/body-doodles-api/main/readme/unit-test.PNG)

The API's were tested locally during development but the core testing was done as part of the front end repos and testing to the real API's manually via form inputs and page loads.

The results can be found in [Body Doodles](https://github.com/Gareth-McGirr/body-doodles)

**Validator Results**

All folders were run through flake8. Several issues appeared with various reasons, lines too long, blank spaces, indentation and docstrings.

All issues were resolved with the exception of lines too long in migration files (these are auto generated so I did not fix) and the auth validator lines in the settings.py which seem to be unbreakable but are framework code.

A warning appeared for env.py being imported but unused although this is being used in the development version, so this was ignored.

![artists](https://raw.githubusercontent.com/Gareth-McGirr/body-doodles-api/main/readme/artists_validator.PNG)

![comments](https://raw.githubusercontent.com/Gareth-McGirr/body-doodles-api/main/readme/comments_validator.PNG)

![contacts](https://raw.githubusercontent.com/Gareth-McGirr/body-doodles-api/main/readme/contacts_validation.PNG)

![drf_api](https://raw.githubusercontent.com/Gareth-McGirr/body-doodles-api/main/readme/settings_validation.PNG)

![followers](https://raw.githubusercontent.com/Gareth-McGirr/body-doodles-api/main/readme/followers_validation.PNG)

![likes](https://raw.githubusercontent.com/Gareth-McGirr/body-doodles-api/main/readme/likes_validation.PNG)

![posts](https://raw.githubusercontent.com/Gareth-McGirr/body-doodles-api/main/readme/posts_validator.PNG)

![profiles](https://raw.githubusercontent.com/Gareth-McGirr/body-doodles-api/main/readme/profiles_validation.PNG)

![reviews](https://raw.githubusercontent.com/Gareth-McGirr/body-doodles-api/main/readme/reviews_validator.PNG)

**Bugs and their fixes**

A bug occured causing a 500 error on post and profile form submissions. It was caused by GCP not accepting dulicate file names so to remedy this, I created a function to renamed the files before uploading with a uuid.

<hr>
<br>

## Deployment

## Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘Gars-Steakhouse’.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

<hr>
<br>

## Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

* Navigate to heroku and create an account
* Click the new button in the top right corner
* Select create new app
* Enter app name
* Select region and click create app
* Click the resources tab and search for Heroku Postgres
* Select hobby dev and continue
* Go to the settings tab and then click reveal config vars
* Add the following config vars:
  * SECRET_KEY: (Your secret key)
  * DATABASE_URL: (This should already exist)
  * ALLOWED_HOST:
  * CLIENT_ORIGIN: url for the client front end react application that wil be making requests to these APIs
  * CLIENT_ORIGIN_DEV: address of the local server used to preview and test UI during development of the front end client application
  * GOOGLE_APPLICATION_CREDENTIALS:
  * GOOGLE_CREDENTIALS: json file with authentication keys and tokens to access the google cloud bucket where images are stored
  * GS_BUCKET_NAME: name of the bucket to upload images to.

* Click the deploy tab
* Scroll down to Connect to GitHub and sign in / authorize when prompted
* In the search box, find the repositoy you want to deploy and click connect
* Scroll down to Manual deploy and choose the main branch
* Click deploy

<hr>
<br>

## Google Cloud Storage

To set up bucket and service account. Please see - [Medium Article](https://medium.com/@mohammedabuiriban/how-to-use-google-cloud-storage-with-django-application-ff698f5a740f). The service account credentials will be needed for deployment.

**Code** 

Packages needed for deployment:

* django-storages[google]
* Pillow

Create a .profile file with the following line inside:

```echo ${GOOGLE_CREDENTIALS} > /app/ga-creds.json```

This line is used to instruct heroku that the GOOGLE_CREDENTIALS var is called ga-creds.json

**Heroku**

1. Log in to heroku and open the boody-doodle-api app
2. Click settings
3. Click Config vars
4. Add the following variables:

    * Key: GOOGLE_APPLICATION_CREDENTIALS -  Value: ga-creds.json
    * Key: GOOGLE_CREDENTIALS - Value: json contents of the service account key
    * Key: GS_BUCKET_NAME - Value: Name of the bucket where files are stored

### Run Locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

In order to run, you will need to create an env.py file and add the config vars as used in heroku steps above.

[Create Environment Variables locally](https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5#:~:text=To%20set%20and%20get%20environment%20variables%20in%20Python%20you%20can,Get%20environment%20variables%20USER%20%3D%20os.)

**Virtual Environment setup** 

Windows:

```
python -m venv venv \
venv/Scripts/activate \
pip install -r requirements.txt
```

Mac:

```
python -m venv venv \
source venv/bin/activate \
pip install -r requirements.txt
```

### Forking

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

- Navigate to the GitHub Repository you want to fork.

- On the top right of the page under the header, click the fork button.

- This will create a duplicate of the full project in your GitHub Repository.

## Credits

### Content:
<br>

This article was followed in order to implement google cloud storage for static image hosting.
* [how-to-use-google-cloud-storage-with-django-application](https://medium.com/@mohammedabuiriban/how-to-use-google-cloud-storage-with-django-application-ff698f5a740f)
<br>
<br>

This  article was followed in order to implement google cloud storage for static image hosting:   
* [django-imagefield-rename-file-on-upload](https://www.dangtrinh.com/2015/11/django-imagefield-rename-file-on-upload.html)
<br>
<br>

This  article was followed in order to implement average rating calculations in the correct way
* [How to calculate average of some field in Dango models and send it to rest API?](https://django.fun/en/qa/16172/)
   
   
   
   
   
   
   
   
   
   
   # Welcome to my fifth project

## NERD ALERT DRF API - PICTURE SHARING SITE


### PURPOSE

---

It's a website for people who want to share their favourite picture from any computer/video game they like to play and be able to discuss the games with likeminded people. Maybe you want to find people just like you who enjoys the worlds of video/computer games. Or want some motivation or find new games to try. Or just have someone to talk about video/computer games with. The goal is to make people want to join the Nerd Alert community and hopefully find new likeminded friends. Users can easily navigate to the different pages of the website with the navigation menu at the top. The navigation menu contains a logo which takes the user to the home page if they click on it. It also has a total of seven menus: Home, Feed, Favourites, Profile, Contact, Sign in, Sign out and Sign up. If the user has registered and is logged in he/she can see Add a picture, check out their own feed which shows posts by the users they are following, check their liked favourite posts and Sign in, Sign up is replaced by Sign out. If the user havent created a user or is logged out they can only see the home, contact, sign in and sign up menus. The webpage got a back and frontend part which are in two separate IDEs. This is the backend/API IDE. 



### AGILE METHODS

---

#### KANBAN 

I used github projects to make my own kanban board to be able to keep track on all different steps I needed to take during this project

![picture from my github pages where i used github projects to make my own kanban board](static/images/readme/github-kanban-board.jpg)

### STRUCTURE

---

#### HOME PAGE

- The home page welcomes the user to the Health You website. 
- A text informs the user what the websites purpose is.
- The user can click on green links that takes he/she to a specific type of recipe
- The user can also use the search bar at the top right corner to search for specific recipes

  
#### RECIPES PAGE

- Shows all the latest recipes
- The user can click on a specific recipe to see more detail about it
  
#### RECIPE DETAIL PAGE

- The detail page for a recipe
- Shows the name of the recipe, ingridients, steps on how to make the recipe
- The user can choose to edit or delete their own created recipes on this page but needs to be logged in for these functions to show.
- The user can leave a comment on the recipe of they are logged in. Also edit/delete and old comment they have made


#### ABOUT US PAGE

- The About Page explains more about Healthy You and the purpose of the website
  
#### CONTACT PAGE

- The user can choose to contact Healthy You if he/she got any questions with the form on this page

#### REGISTRATION PAGE

- If the user want to join the website to be able to save and create own recipes its done in this page

#### LOG IN PAGE

- If the user want to log in to their own profile and see saved/own recipe its done on this page

#### PROFILE PAGE

- If the user want to see the recipes they have created its done on this page
- The user needs to be logged in to used the feature

#### ADD RECIPE PAGE

- If the user want to add a new recipe its done on this page
- The user needs to be logged in to used the feature

### FEATURES

#### FUTURE FEATURES

My plan in the future is to add the star rating for each recipe so the users can rate the recipes after how good they were. 
Also adding the heart symbol to make each user able to save a recipe they really like to their own profile page. 

---

#### HEADER AND NAVIGATION BAR/MENU

- The header is at the top of the website and contains the logo and the navigation bar/menu. For screens bigger then 1024px you can see all the different navigation menus at the top at the right side of the header logo.
- Users can easy find the websites different pages through the navigation menu where they can go to the Recipes, About, Contact, Register or Log in page. 
- The logo in the top left corner of the navigation bar is also a link to the home page.
- The user can see both the logo and navigation menu easy because of the color scheme of the offwhite background with the green text

![picture of the header and navigation bar for screens bigger then 1024px](static/images/readme/header-nav-searchbar.jpg)

- For mobile phones the navigation menu turns into a hamburger bar icon which they can click on to activate the navigation menu

![picture of the header and navigation bar for mobile phones](static/images/readme/header-nav-searchbar-mobiles.jpg)

#### HOME PAGE

- #### HERO IMAGE

  - The hero image is one of the first things you notice when you enter the website. The goal is to make the users want to stay and want to search for delicious recipes to make on their own'
  - It also contains some text which explains the purpose of the website and what the user can do

![picture of hero image](static/images/readme/hero-image.jpg)

- #### CLICKABLE LINKS

  - The home page also got clickable links under the hero image
  - Each link goes to a different type of food recipes
  - This is to make users want to explore more and easy be able to that directly from the home page 

![picture of the clickable links under the hero image](static/images/readme/clickable-links.jpg)

#### RECIPES PAGE

- Its at the recipes page the user can see all the recipes that is added to the webpage
- The user can press the heart icon to save a recipe to their own profile if they are logged in


![picture of recipes page](static/images/readme/recipes-page.jpg)

- #### RECIPE DETAIL PAGE

  - If the user click on a recipe they are taken to the detail page of that recipe
  - It shows the ingredients, instructions, and any comments that made
  - The user can leave a comment if they are logged in
  - If any user have made a comment they are published at the bottom of the webpage, under the recipe

![picture of the top of the recipe detail page](static/images/readme/recipe-detail-page-top.jpg)
![picture of the bottom of the recipe detail page](static/images/readme/recipe-detail-page-bottom.jpg)

#### ABOUT PAGE

- The about page describes what the user can do on the Healthy You webpage and what its purpose

![picture of the about page](static/images/readme/about-page.jpg)

#### CONTACT PAGE

- If users needs to contact Healthy You for some reason they can go to the contact page and fill in the form

![picture of the contact page](static/images/readme/contact-page.jpg)

#### REGISTER PAGE

- If the user want to create a user to be able to create and save/comment on recipe its done on this page

![picture of the register page](static/images/readme/register-page.jpg)

#### LOG IN PAGE

- If the user want to log in to be able to see created or saved recipes and edit their own recipes or comments its done on this page

![picture of the log in page](static/images/readme/login-page.jpg)

#### PROFILE PAGE

- If the user want to see their own recipes or recipes that they have liked its done on this page
- The user needs to be logged in for this page to show

![picture of the profile page](static/images/readme/profile-page.jpg)

#### ADD RECIPE PAGE

- If the user want to add their own recipe to the Healthy You webpage its done on this page
- The user needs to be logged in for this page to show

![picture of the add recipe page](static/images/readme/add-recipe-page.jpg)

### COLOR SCHEME

---

- The color on the background of the header and footer is a beautiful off-white #F1EDE1.
- The color of the logo and navigation menu text is green #49892a, to stand out from the off-white background color
- The color of the all buttons is a darker green #198754, to stand out more from the rest of the content. They are first white with a darkgreen text and border, but when hovered over they text turns white and the background turns to dark green
- The main background is white to make the header and footer stand out more from the rest of the content


### TECHNOLOGIES

---

- Django REST
- Cloudinary
- Python 


### TESTING

---

- I tested the website in Chrome, Firefox and Edge browser to see that all pages loaded and that every link, button, form, images and navigation menu was working
- The site is also responsive which I tested in google chromes devtools by selecting different screensizes and test each function
- I tested that all text is easy to read and to understand
- The CSS code got valified through a CSS validator

  ![Picture of the results of the CSS validator](static/images/readme/css-validator.jpg)
- The HTML code got valified through a HTML validator
  I viewed each pages source code on the live website and copy and pasted that html code to the 
  html validator, so I wouldnt get any django errors. I got some other errors from the live page html code 
  which I couldnt see in the html template code in the IDE:
  - #### RECIPE DETAIL PAGE
  Said that I had stray < p >, < tr >, < td > and < th > tags, which I couldnt find in the html code in the IDE.
  All the other html pages was OK. 

  ![Picture of the results of the html validator](static/images/readme/html-validator.jpg)
- All the Javascript code is valified through .......

  ![Picture of the results of the Javascript validator](static/images/readme/python-linter-results.jpg)


#### MANUAL TESTING 

I also did manual testings on all website pages to ensure that everything was working as expected:

  - #### HOME PAGE 
  Description:
  Make sure all the links to the 5 different recipe types are working

  Steps:

  1. Go to the home page
  2. Click on each link and see if it takes you to the correct type of recipe
  
  Expected:

  The user should be sent to a recipe containing meat when clicking on the meat link

  Actual:

  I was sent to the recipes page which showed me a recipe with meat in it

- #### HEADER AND NAVIGATION MENU

 Description:
  Make sure all the navigation links and the search bar is working

  Steps:

  1. Click on each navigation link to see that i'm taken to the correct page
  2. Click on the logo at the left corner of the header to see that i'm taken to the home page
  3. Write something in the search bar, for example "meat" to see that im taken to a recipe with meat in it
  
  Expected:

  The user should be taken to the correct page when clicking on a navigation link
  The user should be taken to the correct recipe when using the searchbar, and if no recipes are found the recipes page is showed empty

  Actual:

  I was sent to all correct pages through the navigation links and the searchbar showed me the correct recipes i was searching for

  - #### RECIPES PAGE 

  Description:
  Make sure all the recipes are showed and that the user is taken to the correct recipe when clicking on it

  Steps:

  1. Click on the recipes link in the navigation menu
  2. See that the recipes are showing and then click on one recipe
  3. See that the user is taken to the correct recipe that is clicked on
  
  Expected:

  The user should see all the different recipes when first visiting the recipes page
  The user should be taken to the correct recipe when clicking on one of the recipes

  Actual:

  When I clicked on the recipes link in the navigation menu I was taken to the recipes page. It showed me all the different recipes. 
  I then clicked on all the recipes to see that I was taken to the correct recipe, which I was

- #### RECIPE DETAIL PAGE 

  Description:
  Make sure that the user is taken to the correct recipe detail page, showing the correct information, ingredients, instructions and made comments. 
  If the user has made that recipe / and/ or comment they should  also be able to edit/delete that recipe/comment.
  Make sure that a logged in user can make a comment 

  Steps:

  1. Click on one recipe on the recipes page
  2. See that the correct recipe is showing
  3. Check that all information, ingredients, instructions and comments are showing
  4. Check that the user can edit/delete that recipe if they are the creator of that recipe
  5. Check that the user can edit/delete a made comment if they are the creator of that comment
  6. Check that I can make a comment on a recipe if i'm logged in
  
  Expected:

  The user should see the correct recipe with all the information about it
  The user should be able to edit/delete the recipe/comment if they are the creator
  The user can make a comment if they are logged in at the website. If not logged in a message should tell them to log in to be able to create a comment

  Actual:

  When I clicked on one recipe i was taken to that specific recipe. All the information, ingredients and instructions seemed correct due to the title of the recipe.
  I could also edit/delete both the recipe and comments I had made if I were the creator of those. I could write and post a comment as I was logged in. When I wasnt logged in a got a message under the "Add a comment" title that telled me I had to log in to be able to use that feature

  - #### ABOUT PAGE 

  Description:
  Make sure that the about page is showing the correct image and text 

  Steps:

  1. Click on about link in the navigation menu
  2. See that the user is taken to the about page 
  3. See that the correct text is showing that tells the user about this webpage
  
  Expected:

  The user should be taken to the about page displaying a text describing the purpose about this webpage

  Actual:

  When I clicked on about pages navigation link in the navigation menu I was taken to the correct page, showing me the text describing what this webpage purpose is


- #### CONTACT PAGE 

  Description:
  Make sure that all the different fields in the contact form is working and that the user get a message when the form is successfully sent

  Steps:

  1. Write nothing in each field in the contact form tells you to fill that specific field
  2. Write a number in the first name/ last name fields too see if the form tells you that is wrong
  3. Write a name only in the email field to see that the form tells you that you need a email adress
  4. Write nothing on the message field to see that the form tells you that you need to fill this in

  Expected:

  The user should be informed to fill in each field with the correct information before being able to submit the form

  Actual:

  When I filled in each field correct the form was sent and I got a message telling me "Thank you for your message. We will contact you as soon as possible."

- #### REGISTER PAGE 

  Description:
  Make sure the registration is working and that the user can create their own user at the website

  Steps:

  1. Fill in the email field with a name only and see that the form is telling me to use email adress
  2. Fill in the username and then choose a password the is short and see that its telling me to choose another password
  3. Fill in the username and then choose a password the is only numbers and see that its telling me to choose another password
  4. Fill in the username and then choose a password and write it in a different way in the second field to ensure that the form is telling you that the password needs to be the same
  5. Fill in each field correct and see that the user is created successfully
  6. Check that the link to the lon in page under the "Sign up" title is working and is taking the user to the log in page

  Expected:

  The user should be informed to fill in each field with the correct information before being able to create a user
  The user should be taken to the log in page when clicking on the log in link under the Sign up title

  Actual:

  When I filled in each field correct I was able to create my own user. I was also taken to the log in page when I clicked on the log in link in the text under the "Sign up" title

- #### LOG IN PAGE 

  Description:
  Make sure the user is able to log in with a created user

  Steps:

  1. Fill in each field with the wrong username and password to see that the user isnt able to log in
  2. Fill in each field with a correct username and password to see tha the user in being able to log in

  Expected:

  The user should be informed to fill in each field with the correct information before being able to log in
  The user should be able to log in and see their own profile page, and the Add recipes page if they log in with the correct username and password

  Actual:

  When I filled in each field correct I could see my own profile page and add recipe page at the navigation menu

- #### PROFILE PAGE 

  Description:
  Make sure the user is able to see their own profile page when logged in to the website, and see recipes they have created on their profile page

  Steps:

  1. Log in to the website and see that the profile link is showing in the navigation menu
  2. Click on the profile page and see that the correct profile page is showing
  3. If the user has created recipes those should be showed on this page
  4. The user should also be able to click on one recipe and be taken to that specific recipe

  Expected:

  The user should be able to see a profile page link in the navigation menu and when clicked on being taken to their own profile page
  The user should be able to see all the recipes they have created IF they have created any
  The user should be taken to the correct recipe detail page if they click on a specific recipe they have created that is showing on their profile page

  Actual:

  When I logged in and clicked on the profile page I was taken to my own profile page. I Could see all the different recipes I had created.
  I then tried to click on a specific recipe and was taken to the correct one



- #### ADD RECIPE PAGE 

  Description:
  Make sure that the user can add their own recipe when logged in to the website, and that the recipe is showing on the recipes page

  Steps:

  1. Log in to the website and see that the add recipe link is in the navigation menu
  2. Click on the Add Recipe link too see that the correct page is loaded
  3. Fill in the information and image that is needed for the recipe
  4. Click on the "Create recipe" button at the bottom of the page to see that the user is taken to the recipes page and that the new recipe is added

  Expected:

  The user should be able to see a add recipe link in the navigation menu when logged in. The user should be able to create a new recipe that is added to the recipes page

  Actual:

  When I logged in and clicked on the Add Recipe link in the navigation menu i was taken to the correct page. I then created a new recipe and pressed the "create recipe" button.
  I was then taken to the recipes page and my own new recipe was showed on the page

#### BUGS

- 

### DEPLOYMENT

---
    This project was deployed to Github.com. The following steps shows how you do it:

1. Log in to your Github.
2. Go to the Nerd Alert DRF repository in Github: [https://github.com/Kimskogfelter/pp5-drf-nerd-alert]
3. Select Settings in the repository navigation menu at the top.
4. Select Pages at the left handside of the website.
5. Choose: Deploy from a branch as Source.
6. Choose: Main as branch and /root as folder and press save.
7. Wait a few minutes and press the Code menu to the top left.
8. At the right handside go to Deployment.
9. Then press the ![picture of the deployment icon on github](https://github.com/Kimskogfelter/Safari-Retreat/blob/main/assets/images/readme/deployment-icon.jpg) to go to the live website.



    This project was deployed to Heroku.com. The following steps shows how you do it:
    
1. Start by creating a account on Herokus website
2. Then log in to your account and create the app for your website
3. When the app is created go to the settings tab
4. Reveal the config vars and add a KEY of DISABLE_COLLECTSTATIC, and a VALUE of 1
5. In your IDEs terminal pip install gunicorn~=20.1 
6. In your IDE use this command: "pip freeze --local > requirements.txt" to update your requirements.txt file with the installed gunicorn
7. Create a file in your root directory named Procfile, it needs to be the same directory as your requirements.txt
8. In your procfile add this text: "web: gunicorn my_project.wsgi"
9. Change "my_project" to the name of your own project
10. Open your settings.py file and change your DEBUG settings to False. It should always be False when deploying your project to Heroku!
11. In your settings.py under the ALLOWED_HOSTS add this text ",'.herokuapp'" 
12. Now git add, commit and push all the changes to Github
13. Return to your Heroku dashboard and go to the deploy tab
14. Choose to connect your Heroku account to your Github account 
15. When your Heroku account is connected to your Github account search for your project repo name and choose it
16. Then scroll down to the bottom of the page and click on the "deploy branch" button to start a manual deployment
17. When the deployment is done you'll see a "View" button at the bottom of the page
18. Press that button to view your deployed app

  This project uses a database from ElephantSQL. The following steps shows how you create a database through ElephantSQL:

1. Log in to or create a new account at the ElephantSQL database webpage
2. Click at "create new instance"
3. Choose a name and plan for your database, name could be the same as your webpage to make things easy
You can leave the tags field blank
4. Click on the "select region" button and choose a region/data center close to you and then press the "review" button
5. Check that all information is correct and press the "create instance" button
6. Click on your newly made database
7. Click on the STATS menu and check that the PostgresSQL version is higher then 12 (if its not higher then 12 you need to go back to step 1 and create a new instance and choose a different data center. If you are in Europe choose one thats in Europe)
8. When your PostgresSQL version is 12 or higher go to the DETAILS menu and copy the URL
9. Go back to your IDE and create a new file named "env.py" in your root directory, the same as your Procfile
10. Open the ".gitignore" file and add the "env.py" to that
11. Open your "env.py" file and add this text: "import os os.environ.setdefault('DATABASE_URL', '')"
12. Change the text "" to your own data base URL you copied from ElephantSQL
13. Pip install dj-database-url~=0.5 and psycopg2~=2.9, these are required to be able to connect to your PostgresSQL database
14. Pip freeze your requirements.txt file
15. Open your "settings.py" and add this at the top of it "import os import dj_database_url if os.path.isfile('env.py'): import env"
16. Still in your "settings.py" file, find the local sqlite3 database that Django provides and comment that one out so you dont use it
17. Then add this text under the local database you just commented out "DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL")) }"
18. Now that your project is connected to the database you need to use the migrate command in your terminal, copy this text to your terminal and press enter "python manage.py migrate"
19. In your "settings.py" file change DEBUG to False! IMPORTANT
20. Now git add, commit and push all the changes to Github
21. Go to your Heroku dashboard and go to the DEPLOY tab and do a manual deployment
22. When the deployment is done go to the settings tab and reveal your config vars
23. Add a new confiv var with the KEY "DATABASE_URL" and the VALUE is your ElephantSQL URL
24. Now your deployed app should be connected to your new PostgresSQL database

### ISSUES

- 

### CREDITS

---

#### MEDIA

- The images are from the below sources:
  - default post picture https://codeinstitute.s3.amazonaws.com/ReactEssentials/DRF/Images/default_post.jpg 
  - default profile picture https://codeinstitute.s3.amazonaws.com/ReactEssentials/DRF/Images/default_profile.jpg

#### CODE

- I used Code Institutes API project walkthru to make this API https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/f775d54df4da44d18309888b3fe884f7/a146472df94c4691951c4f58ac43e30e/?child=first and be able to add own modules to it to make it "my own". I changed the likes app to be favourites insted. And the contact app is taken from another source: see below. The rest in this API is copied from the above links walkthru. 
- I used this github projec to help me create the contact app and make it work: https://github.com/Hujanen91/sourdoughcircle_api/tree/main/contact. 
I used the views.py, models.py and serializers.py to help me structure my own code.
- I used this github project to help me create the star_rating in the comments app: https://github.com/Gareth-McGirr/body-doodles-api/tree/main/reviews


#### All the thanks to the lovely students on slack. Specially the students in the community-sweden group for helping out when needed and my mentor for being so supportive and helpfull