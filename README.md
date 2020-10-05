# IvyHacks 2020

This project was created to participate in Ivyhacks 2020. It is build by Henry Kuo, Mark Jabbour, and Masaoud Haidar. It was created using python, django, html, and css. We used a template from w3schools for the css. 

## Description of the Project:

### Inspiration 
The more we move to online learning, the less we are getting engaged with our classroom, and the more difficult students find it to relate their coursework to the real world.

### What it does
HAMMA is a platform that brings together corporations, professors and students. Corporations can post day to day challenges that their employees face. Students can discuss these problems. And finally, professors can design interactive courses that connect these challenges to their theoretical background.

### How we built it
We built it with Django, Python, HTML, and CSS. While building, we referred a lot to w3schools' online material and their css templates.
We used django HTML templates to make it easier to update the general design of our website when necessary.
We used django to built the following three apps, and integrate them:

__courses__: <br>
supports our home page (the page that displays all courses), as well as adding problems and displaying them. The views of the problem pages were a bit involved, in order to allow different kinds of users to see different things (students, do not see and add a problem button, etc..)

__users__: <br>
 ___models___: 
 specifies three kinds of users Student, Professor and Company. The users are linked to default instances of django's  AbstractUser to allow for interfacing with default user construction and login forms. <br>
___urls___: 
This app has to pages signup, and login. they are accessible with prefix authenticate/page_name (signup or login). <br>
___forms___: 
	We use the default login form, and add a choice field to user creation form. The 

### Challenges we ran into
Since we all had no prior experience with web development, we had to divide the work and learn on the fly. This also made it hard to understand and edit each other's codes. 
In addition we had to do some extra work to have different account types in the backend and to add styles to Django's login and register forms. 

### Accomplishments that we're proud of
This is our first web development project. We are happy that we managed to create both the frontend and backend and make them work well together.

### What we learned
We learned a lot about how web applications are created and maintained. We also learned a lot about django, HTML, CSS and java script.


### What's next for HAMMA

Instead of professors just posting an explanation, we'd like to offer them a platform to design full interactive courses, with flexible demos, videos, and quizzes.
We also would like to have different tags for each problem, and allow the users to search for problems by their tags. We would also like to allow companies to view the profiles of students and view their accomplishments and their discussions. 

### Quick Demo: 
https://youtu.be/TZAsjzyBZbs
