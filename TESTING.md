## Testing
There was always a tab open for testing with the website preview through Gitpod port 8000. To check up on my code and see if it worked as I wanted. 
I used DevTools to see how the code would respond if I added or changed properties or values with CSS or Bootstrap. I also took help from DevTools to check the responsiveness when decreasing or increasing the screen size.
To see and test the website's performance, I used Lighthouse, which gave me an updated report to see how well my performance, accessibility, and SEO were for the website. The last test results were these:
![Lighthouse](documentation/testing/.png)

To see that the JavaScript code in the project worked without any bugs, I used the console section of DevTools to know that it rendered as it should. While working with JavaScript, I got an error message that the browser could not render the script.js file. That was because I was using the hard-code, not the Django format, and loading static at the top of the templates.

Several internet browsers, like Chrome, Mozilla Firefox, Microsoft Edge, and Safari, were used during all the testing. It works on all the mentioned internet browsers and mobile devices.

### Code Validation
* HTML
There are no errors form the offical [W3C Validatior](https://validator.w3.org/)
    ![HTML-validation](documentation/testing/html-valid.png)
    Link to the validation: [W3C Validatior](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcosmos-forum.herokuapp.com%2F)

* CSS
There are no errors form the offical [Jigsaw validator](https://jigsaw.w3.org/css-validator/), but warnings that I am aware of.
  ![Css-validation](documentation/testing/cssvalid.png)

  ![Css-validation-warning](documentation/testing/csswarning.png)
    Link to the validation: [Jigsaw validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcosmos-forum.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

* JavaScript
No errors where found when going through the offical [Jshint validator](https://jshint.com/).
 * There is 1 functions in this file.
 * Function with the largest signature take 1 arguments, while the median is 0.
 * Largest function has 18 statements in it, while the median is 3.
 * The most complex function has a cyclomatic complexity value of 5 while the median is 1.

    ![script.js](documentation/testing/.png)

* Python
The code passed through [PEP8 linter](http://pep8online.com/checkresult). The result confirmed there are no problems with the code.

![PEP8-1](documentation/testing/.png)
![PEP8-2](documentation/testing/.png)
![PEP8-3](documentation/testing/.png)

### Browser Compatibility
* Google Chrome
  * The website runs without any issues in the Google Chrome browser

  ![Chrome](documentation/testing/chrome.png)

* Mozilla Firefox
  * The website runs without any issues in the Mozilla Firefox browser

  ![Firefox](documentation/testing/firefox.png)

* Microsoft Edge
  * The website runs without any issues in the Microsoft Edge browser

  ![Edge](documentation/testing/edge.png)

* Safari
  * The website runs without any issues in the Safari browser

  ![Safari](documentation/testing/.png)

### Responsiveness
* For tablet view 
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)

* For mobile view
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)

### Tested Code
The result for the testing with Django testing of the view functions.
![](documentation/testing/test-views.png)

The result for the testing with Django testing of the models.
![](documentation/testing/test-model.png)

### Tested User Stories
This section provides the test done to check the User Stories for this project.

* Posts:
A Verified User/Admin can read, create, edit and delete a post to start a conversation with other Verified Users/Admin. 
An Unverified User/Visitor can only read posts. 

  * Verified User/Admin:
  ![](documentation/testing/.png)
  ![](documentation/testing/.png)
  ![](documentation/testing/.png)
  ![](documentation/testing/.png)

  * Unverified User:
  ![](documentation/testing/.png)
  ![](documentation/testing/.png)
  ![](documentation/testing/.png)
  ![](documentation/testing/.png)

* Choose Category & Categories: 
A verified User/Admin can navigate through the category options available from the categories menu to find the relevant post about that topic.

![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)

* Post Comments: 
A Verified User/Admin can leave comments on posts to start or participate in conversations.

![](documentation/testing/.png)
![](documentation/testing/.png)

* View Comments: 
Any Visitor to the website can view comments on different posts and read the conversation. 

![](documentation/testing/.png)

* Like/Vote/Unlike: 
A Verified User/Admin can Like/Vote and Unlike a post to show their interest in the subject.

![](documentation/testing/.png)
![](documentation/testing/.png)

* View Likes: 
Any Visitor or Verified User/Admin can view the number of Likes/Votes a post has.

![](documentation/testing/.png)

* View popular posts: 
A Visitor or Verified User/Admin can view on a designated page the post with the most Likes/Votes to see which are popular on the forum at the moment.

![](documentation/testing/.png)
![](documentation/testing/.png)

* Account Registration: 
A Visitor/Unverified User can sign up to become a community member/Verified User and access all the website's functionalities.

![](documentation/testing/.png)

* Approve Comments: 
A Verified Admin to the website is the only one with access to approve comments before posting on the website, to filter out objectionable comments.

![](documentation/testing/.png)
![](documentation/testing/.png)

* Deleting of created Content: 
When a Verified User wants to delete made content, they get a notification with an option to change their mind or confirm they want to delete that content.

![](documentation/testing/.png)

### Tested Features
This section shows the tests for the features of the website that are not related to the user stories. Please go to the Tested User Stories section above to see those tests.

* Menu/Navbar 
The first navbar shows the links to the home page through the Logo and 'Home' option, the sign up to become a Verified User and the link to login as Verified User/Admin. If a User verifies through login or signup, the navbar changes its links to 'Add Post' to add content and a 'Log out' link to log out from the website. 
The menu collapses when the screen size is 575px or lower and gets a hamburger icon that the User can click on to open the navbar.

![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)

The second navbar for categories displays all the categories available on the website. When selected for the music genres categories, a drop-down function shows all the genres available. When Users select a category, they are redirected to a page whit all the posts. If there is no post available for that category, a message is displayed to the User to either login, create on themself or become a Verified User to make a post.
The menu collapses when the screen size is 575px or lower and gets a 'Categories'-button that the User can click on to open the navbar.
If the User is verified on the website and clicks on either the login link or signup link, they will get redirected to the 'Home' page. If they select the add post link, the User gets redirected to the 'Add Post' page.
When Unverified Users select either the login link or signup link, they will get redirected to those pages. If they choose to click on the add post link, a message will display, letting the User know that they need to Verify themself as a registered User to add a post to that category.

![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)

* SignUp/LogIn/LogOut
  * SignUp: 
When Unverified User signup, the fields for Username and Password are required to fill in; if requirements do not meet the necessary input, a message displays above the input field, notifying the error. The User is also required to write the password twice when signing up. When the form requirements are correct, the User gets redirected to the 'Home' page.
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)

  * LogIn: 
The login form requires a valid username and password to log in to the website. If the required fields are not populated or username and password do not match, a notification will show above the input fields, telling the User what the error is. When the form requirements are correct, the User gets redirected to the 'Home' page.
![](documentation/testing/.png)
![](documentation/testing/.png)

  * LogOut: 
When a Verified User chooses to log out from the website, a message displays on the screen, asking if they are sure they want to log out or stay logged in on the website. When the User logs out, they get redirected to the 'Home' page. If a User chooses to stay logged in, they get redirected to the 'Home' page.
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)


* Pagination
The home page and categories pages do not have working pagination. See Unfixed Bugs down belove to get the information regarding that matter.
The pagination for 'Most Liked Post' shows no errors. After fifteen posts, a 'Next' button appears and, when selected, takes the User to the next page. If there are more pages than two, both the 'Next' and 'Back' buttons will appear on the page. If the User is on the last page, only the 'Back' button will show and take the User back to the previous page.

![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)

* Footer with Social Media Icons
The Social Media Icons in the footer takes the User to that icon's Social Media home page and opens up in a new tab. 
If a User clicks on the Logo below the Social Media Icons, they get redirected to the Cosmos home page.

![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)

### Unfixed Bugs
* Pagination
When trying to implement pagination to the function-based views, such as the home view and category view, the website would only show one post for that view. When writing the code for the pagination for that view, I tried to put the variables for pagination on different levels in the code but only managed to make it work by showing one post. For the templates, I tried other inputs for the ifs- and for-statements with the result as above. I'm sure that I can make it work as I practice. 

![](documentation/testing/.png)