# Cosmos
"They say there are no sounds in space. So let's share and create some noise together with Cosmos."
Cosmos is your number one source to go to if you want to discuss and connect with others through music.

amiresponisive image

## User Stories
* Create Posts: As a Verified User/Admin, I can create, read, edit and delete posts about music I like and start conversations with other users.

* Choose Category: As a Verified User/Admin, I can choose among different categories to quickly find the relevant post of interest.

* Categories: As a User/Admin, I can choose among different categories to see all the relevant posts about that topic.

* Post Comments: As a Verified User, I can leave comments on uploaded posts to participate in the conversation.

* View Comments: As a User/Admin, I can view comments on individual posts to read the conversation.

* Like/Vote/Unlike: As a Verified User, I can Like/Vote/Unlike a post to show my interest in the subject.

* View Likes: As a User/Admin, I can see the number of Likes/Votes a post has.

* View popular posts: As a User/Admin, I can view a list of the post with the most Likes/Votes to see which posts are the most popular.

* Account Registration: As a User, I can create a user profile to use the website's functionalities.

* Approve Comments: As Admin of the web application, I can approve or disapprove of comments to filter out objectionable comments.

* Deleting of created Content: As a Verified User, I get notified if I want to delete a post or comment I made and get a chance to regret it.

## UX 
The forum's design is minimalistic yet a bit colorful to let the topics and posts speak for the website. Cosmos wants the user to feel like they are in a record store with a modern twist, refering to space.

### Colour Scheme
The website's primary colors are:
* Black  
* different kinds of dark blue
* a bluish-white(rgb(252, 251, 255)) 

### Typography
* Headings/Menu/Footer/Comments: [Montserrat subrayada](https://fonts.google.com/specimen/Montserrat+Subrayada?query=monts)
* paragraph text: [Quicksand](https://fonts.google.com/specimen/Quicksand?query=quick)
* Logo: [Modak](https://fonts.google.com/specimen/Modak?query=moda)
* Icons: [FontAwsome]()

The fonts for this project are minimalistic but still familiar to the user. The font Montserrat subrayada is used for the significant headings to create a clean and minimalistic feel to the website.
The font Quicksand creates a soft, warm, and familiar feeling for the paragraph text.
Modak gives a vintage feel, which is in great contrast to the other fonts' more modern feeling.
The Icon used for like, comment and social media are from FontAwsome.

### Wireframes


## Features
### Existing Features
#### Menu/Navbar 
The site has two different navbars at the top. The first navbar holds the links to the home page, the sign up to become a member, the login if you are already a member, and an add-post button will show if the member/user is active as a site user. The signup and login link will change to a logout link when the user is active on the site. 
The menu is collapsable, so it becomes a hamburger menu when the screen size is 990px or lower.

The second navbar holds the links to all the different categories that the post can have. So it is easier for the users to find posts and get involved in conversations about the topic of their interest. The genre link is a drop-down button that displays all the current genres available at the site.

#### SignUp/LogIn/LogOut 
To add a post and start a conversation, the user must become a site member. 
To signup for the site, the user must create a username and password. When that user has a registered username and password, they can log in and out from the site as they like.

#### View and create a post
A visitor to the website can view all the posts made on the site. To add a post of their own, they must be a member. When creating a post, the user has to give it a title, choose a category, and write the desired content. The user can also upload a picture with the post.
On the home page, users can see a list of the ten most-liked posts. In that way, users can find new artists, songs, or music genera they have never listened to before.

#### Pagination
The home page also shows the latest post made for the visitors. After fifteen posts, they can go forward to see more posts. The pagination also applies to the other pages for categories and most liked posts.

#### View and post Comments
A website user can see comments to a post and follow the conversation. If users want to post a comment themselves, they must be site members and logged in. To keep the tone of the discussion in the best way, they need to be approved by the admin or staff before users can see it displayed on the website.

#### View Likes and like a post
Any visitor to the website can see how many likes a post has, but a visitor must log in as a user to like a post.

#### Editing content made
A user can choose to edit a post they made. They can edit the title the comment's content and change the image. 

#### Deleting content made
If a user has made a post, they can delete that content if they desire to do so. If they decide to delete content, they will get a message to confirm if they really want to delete it.

#### Footer with Social Media Icons
The footer contains several Social Media Icons that are relevant to a music-oriented website. When a user clicks on one of the icons, the website related to the icons will open in a new tab. 

### Features Left to Implement
#### A Profile page
A profile page for users. This page could show relevant information like their post and their conversations. It could also display a list of posts with the status of draft. At the moment, a user can only post a post directly. If they change their mind and go back to another page of the site, that post will be unable to retrieve it.

#### Edit and Delete Categories
Another thing to implement would be the ability for users to edit and delete the comments they posted.

#### Multiple categories 
A user gets to choose to add multiple categories for a post to make it more visible for others and give the user a bigger chance to start a conversation.

#### Better layout design for the forms
Create better-looking forms for the login, log out and sign up page. The input fields should align with each other to get a better UX.

#### Hero image
Make the current Hero image a carousel with posts or pictures related to new music. 

## Technologies Used
These are the following technologies and packages used to develop this project:

* [HTML](https://html.spec.whatwg.org/): HTML5 are used to build the core structure of the website

* [CSS](https://www.w3.org/TR/css/): CSS is used to style the website with colors, fonts, placement of elements, etc.

* [JavaScript](https://www.javascript.com/): JavaScript are used to make the website more interactive for the user

* [Python](https://www.python.org/): Python is used to build the core structure and code for the project

* [Heroku](https://www.heroku.com/home): Heroku is the deployment environment used to deploy the project and connected with the GitHub repository

* [Gitpod](https://gitpod.io/): Gitpod is the development environment used for developing all the code during this project

* [GitHub](https://github.com/): GitHub are used to store the repository for this project

* [Git](https://atlassian.com/git/): Git is used to create backups of the project and ensure that all versions of the project is pushed to GitHub

* [Canva](https://www.canva.com/): Canva is a web application used to create the wireframes for this project

* [DevTools](https://developer.chrome.com/docs/devtools/): Dev Tools is used to look over the development of the website, debugging problems, and try different approaches to issues that would occur during the process. 

* [Auto Prefixer](https://autoprefixer.github.io/): Auto Prefixer is an application used at the end of the project to give the CSS code some extra properties when used on different browsers.

### Django packages
To build this project the following packages needs to be installed:
<details><summary>CLICK HERE to expand the full requirements.txt file details</summary>

| Package  | Version | Description |
| ------------- | ------------- | ------------- |
| [Django](https://www.djangoproject.com/) | 3.2 | The Django Framework|
| dj_database_url | 0.5.0 | Utilizes the 12factor inspired DATABASE_URL environment variable to configure Django apps  |
| [Django-allauth](https://django-allauth.readthedocs.io/en/latest/) | 0.48.0 | An integrated Django application for addressing authentication, registration, account management, and social account authentication. |
| [Cloudinary](https://cloudinary.com/) | 1.29.0 | A cloud-based storage for and uploading images and videos |
| [Gunicorn](https://gunicorn.org/)  | 20.1.0 | Gunicorn is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model. The server is compatible with various web frameworks and light in server resources |
| [Psycopg2](https://www.psycopg.org/docs/) | 2.9.3 | A PostgreSQL database adapter for the Python programming language |
| [TinyMCE](https://www.tiny.cloud/)  | 3.4.0 | A cloud-based Rich-Text Editor to convert Html text areas to editor instances |

 (((The [requirements.txt](requirements.txt) command for the installed packages is:
- `pip3 install -r requirements.txt`)))

</details>


## Testing
To view all tests for this project, please refer to the [TESTING.md](TESTING.md) file.

## Deployment


The live link can be found here - [https://cosmos.herokuapp.com/](https://cosmos.herokuapp.com/)

### Local Deployment
In order to make a local copy of this project, you can type the following into your IDE Terminal to clone this repository:

- `git clone https://github.com/stroemlind/cosmos.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/stroemlind/cosmos)

## Credits
### Content
For an overall start of the project:
* [CodeMy](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)

For integrating and installing TinyMCE text editor:
* [Geeks for Geeks](https://www.geeksforgeeks.org/how-to-integrate-custom-rich-text-editor-in-your-django-website/)
* [TinyMCE](https://www.tiny.cloud/docs/quick-start/)
* [TinmyMCE Django](https://www.tiny.cloud/docs/integrations/django/)

For footer design:
* [MdBootstrap](https://mdbootstrap.com/docs/standard/navigation/footer/)

For pagination:
* [Webnots](https://www.webnots.com/bootstrap-pagination-tutorial/)
* [Django Projetc](https://docs.djangoproject.com/en/4.0/topics/pagination/)
* [Ordinary Coders](https://ordinarycoders.com/blog/article/django-pagination)
* Nafeesah Younis[GitHub](https://github.com/nafeesahyounis/django-test-blog/blob/master/blog/views.py) and post on [Slack](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1609281135242700)

For footer:
* [Stackoverflow](https://stackoverflow.com/questions/40853952/bootstrap-footer-at-the-bottom-of-the-page)

Populate Slugfiled in add_post.html form
* [The Net Ninja](https://www.youtube.com/watch?v=qO1bgMG7sO8)

Like-button 
* [Dev.to](https://dev.to/radualexandrub/how-to-add-like-unlike-button-to-your-django-blog-5gkg)
* [I think therefor I blog]()

For Comments:
* [Django Central](https://djangocentral.com/creating-comments-system-with-django/)
* [Data-Flair](https://data-flair.training/blogs/discussion-forum-python-django/)
* Tutor Ed from Code Institute

For Most liked page:
* [Stackoweflow](https://stackoverflow.com/questions/65944103/django-order-by-highest-number-of-likes-in-homepage)

Category navbar: 
* Tutor Scott from Code Institute 
* [Boutique Aldo](https://github.com/Code-Institute-Solutions/boutique_ado_v1) walkthrough lessons and githubfiles

Max length of words shown in blog post on index page:
* [Django Projects](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#truncatechars-html)

### Media
* Post Images used during development are created from these pexels images: 
 * [Image one](https://www.pexels.com/sv-se/foto/himmel-natt-rymden-galaxy-956981/)

 * [Image two](https://www.pexels.com/sv-se/foto/himmel-natt-rymden-mork-1252890/)

### Acknowledgements
