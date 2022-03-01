## Testing
### Code Validation
### Browser Compatibility
### Responsiveness

### Tested Code
The view functions that got tested with Django testing and the result.

![](documentation/testing/.png)
![](documentation/testing/.png)

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
The menu collapses when the screen size is 990px or lower and gets a hamburger icon that the User can click on to open the navbar.

![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)
![](documentation/testing/.png)

The second navbar for categories displays all the categories available on the website. When selected for the music genres categories, a drop-down function shows all the genres available. When Users select a category, they are redirected to a page whit all the posts. If there is no post available for that category, a message is displayed to the User to either login, create on themself or become a Verified User to make a post.

![](documentation/testing/.png)
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