
   # Nerd Alert API

Nerd Alert API is the backend used by this website (https://github.com/Kimskogfelter/pp5-frontend-nerdalert).
<hr>
<br>

## Development Goals

The goal of this API is to make the frontend work as expected by having the users being able to do C.R.U.D. 
<hr>
<br>

### Agile Planning

I used a kanban board when developing this project to help me track each of the steps I needed to take to complete this website.

During the development of the webpage I deleted all the stories I found not necessary to keep in the websise so I only could focus on the ones I really needed.

The Kanban board was created using github projects and can be located [here](https://github.com/users/Kimskogfelter/projects/6/views/1).

<hr>

### Entity Relationship Diagram (ERD)

Entities

#### User
* Attributes: id, username, email, password (not shown in the models but typically present in Django's built-in User model).
* Relationships:
One-to-One with Profile.
One-to-Many with Comment, Favourite, Post, Follower.
#### Profile
* Attributes: id, owner (ForeignKey to User), created_at, updated_at, name, content, image.
* Relationships: One-to-One with User.
#### Post
* Attributes: id, owner (ForeignKey to User), created_at, updated_at, title, content, image, image_filter.
* Relationships: One-to-Many with Comment, Favourite.
#### Comment
* Attributes: id, owner (ForeignKey to User), post (ForeignKey to Post), created_at, updated_at, content.
* Relationships: One-to-Many with Post.
#### Favourite
* Attributes: id, owner (ForeignKey to User), post (ForeignKey to Post), created_at.
* Relationships: One-to-Many with User and Post.
#### Follower
* Attributes: id, owner (ForeignKey to User), followed (ForeignKey to User), created_at.
* Relationships: One-to-Many with User.
#### ContactModel
* Attributes: id, contact_name, contact_topic, contact_email, contact_message, created_at, read.
* Relationships: None.
#### Relationships
* User to Profile: One-to-One
* User to Comment: One-to-Many
* User to Favourite: One-to-Many
* User to Post: One-to-Many
* User to Follower: One-to-Many
* Post to Comment: One-to-Many
* Post to Favourite: One-to-Many
* Favourite to User: Many-to-Many (through owner)
* Favourite to Post: Many-to-Many (through post)
* Follower to User (as owner): Many-to-Many
* Follower to Followed User: Many-to-Many

### Epics

The epics for this project can be found in this readme: https://github.com/Kimskogfelter/pp5-frontend-nerdalert/blob/main/README.md

<hr>
<br>

### User Stories

The user stories for this project can be found in this readme: https://github.com/Kimskogfelter/pp5-frontend-nerdalert/blob/main/README.md


## Security

The ermissions class IsOwnerOrReadOnly was added to this project to make sure that only the users who create the content are able to edit or delete it.

## Technologies

* Django
* Django REST Framework
* Heroku
* Git
* Github
* Python
    

<hr>
<br>

## Testing

This API's was tested during development but the main testing was done on the frontend application. Testing that the real API's manually worked as expected via forms, inputs and page loads.

The results of the tests can be found in the frontends readme: https://github.com/Kimskogfelter/pp5-frontend-nerdalert/blob/main/README.md

**Validator Results**

All files in this API were tested in a python validator. 
All the files got "All clear" except the settings.py file. 
The validator think the lines on rows 73, 126 and 182 are to long. 
The were left as they were because I didnt want to break any code so close
to the end date. 

![python validator result](https://github.com/Kimskogfelter/pp5-drf-nerd-alert/blob/main/readme/images/python%20validator.jpg)


**Bugs and their fixes**

The CSS for the deployed API website isnt working. I have checked the devtools for help on where the code 
needs to be changed in order for the CSS to apply. I havent been able to find and correct that part of the code
so the CSS is still not working. 

### Manual testing

I also did manual testings on all API pages to ensure that everything was working as expected:

* Comments page

Description: Make sure all the created comments are listed

Steps:

Go to the /comments page for the API
Check that the created comments are listed

Expected:

I should be able to see all the created comments

Actual:

I was able to see all the created comments

* Contact page

Description: Make sure all the submitted contact forms are listed

Steps:

Go to the /contact page for the API
Check that the submitted contact forms are listed

Expected:

I should be able to see all the submitted contact forms

Actual:

I was able to see all the submitted contact forms

* Favourites page

Description: Make sure the favourites counts are listed 

Steps:

Go to the /favourites page for the API
Check that the favourites are displayed in a list

Expected:

I should be able to see post that are marked with a heart to be a favourite

Actual:

I was able to see the different post marked as a favourite in a list

* Followers page

Description: Make sure the followers counts are listed 

Steps:

Go to the /followers page for the API
Check that the followers are displayed in a list

Expected:

I should be able to see all the profiles that got a follower, and which follower that is

Actual:

I was able to see the different profiles and which profiles that followed them

* Posts page

Description: Make sure the posts list are displayed

Steps:

Go to the /posts page for the API
Check that all the created posts are displayed in a list

Expected:

I should be able to see all the created posts in a list

Actual:

I was able to see the listing for all the created posts

* Profiles page

Description: Make sure the created profiles are listed

Steps:

Go to the /profiles page for the API
Check that all the created profiles are displayed in a list

Expected:

I should be able to see all the created profiles in a list

Actual:

I was able to see the listing for all the created profiles


<hr>
<br>

## Deployment

## Version Control

The following git commands were used throughout development to push code to the remote repo:

```git add .``` - This command was used to add the file(s) to the staging area before they are committed.

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

* Click the deploy tab
* Scroll down to Connect to GitHub and sign in / authorize when prompted
* In the search box, find the repositoy you want to deploy and click connect
* Scroll down to Manual deploy and choose the main branch
* Click deploy

<hr>
<br>

### Run Locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

In order to run, you will need to create an env.py file and add the config vars as used in heroku steps above.

## Credits

### Content:
<br>

- I used Code Institutes API project walkthru to make this API https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/f775d54df4da44d18309888b3fe884f7/a146472df94c4691951c4f58ac43e30e/?child=first and be able to add own modules to it to make it "my own". I changed the likes app to be favourites insted. And the contact app is taken from another source: see below. The rest in this API is copied from the above links walkthru. 
- I used this github projec to help me create the contact app and make it work: https://github.com/Hujanen91/sourdoughcircle_api/tree/main/contact. 
I used the views.py, models.py and serializers.py to help me structure my own code.
- I used this readme to help me create this one: https://github.com/Gareth-McGirr/body-doodles/blob/main/README.md


### Media:
<br>

- The images are from the below sources:
  - default post picture https://codeinstitute.s3.amazonaws.com/ReactEssentials/DRF/Images/default_post.jpg 
  - default profile picture https://codeinstitute.s3.amazonaws.com/ReactEssentials/DRF/Images/default_profile.jpg


#### All the thanks to the lovely students on slack. Specially the students in the community-sweden group for helping out when needed and my mentor for being so supportive and helpfull