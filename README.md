
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


### Epics

The epics for this project can be found in this readme: https://github.com/Kimskogfelter/pp5-frontend-nerdalert/blob/main/README.md

<hr>
<br>

### User Stories

The user stories for this project can be found in this readme: https://github.com/Kimskogfelter/pp5-frontend-nerdalert/blob/main/README.md


## Security

The ermissions class IsOwnerOrReadOnly was added to this project to ensure that only the users who create the content are able to edit or delete it.

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

No bugs found.

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