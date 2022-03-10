# team13-socialmedia
social media project for b461/561 class - team 13

Frontend is hosted at http://koobecaffrontend.herokuapp.com/

# Technology Stack:

NextJS, Django Rest Framework, PostgreSQL, Redux Toolkit, Redux Persist, JWT, Python

# Features of the app include:

* Login and Registration:
  - When the user signs up, a validation email is sent with an activation link. Only, when the user clicks on this link he/she will be able to log in.
  - Forgot password functionality implemented.
  - For authentication, JWT is used

* Posts and User Profile:
  - After login, a landing page is displayed with all the user's posts and a navigation menu on the left side.
  - Used can make posts, which will be seen by all the other users
  - User can edit their own profile and view their own posts. He can also visit other users' profiles and view their posts.

* Search System:
  - Users can search for other users and posts

* Pages, Events, and Notifications:
  - Users can create Pages that other users can follow.
  - This Page can create Events. All the users following the Page will get notifications about the event. 

* Chat: 
  - Users can chat with other users on a real-time basis

* Dark Mode:
  - Users can toggle between Dark mode and normal mode while using the app.

