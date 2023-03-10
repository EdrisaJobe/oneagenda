# About One Agenda
Ever wanted to plan out a trip and store crucial information with ease without the need or hassle of paying a premium just to store your data in a simple table format? Well this app is designed to make that easy, I made this app as a way to store important information fast and without the need of having to use multiple apps to store individual data regarding Fligth and Hotel information. Simply make an account, sign in, and store simple useful information that you can then grab later on or simply discard if no longer needed.

<a href="https://oneagenda.herokuapp.com/"><img src="https://img.shields.io/badge/Link-One_Agenda-2ea44f?style=for-the-badge" alt="Link - One Agenda"></a>
## Technology Used :hammer_and_wrench:

Frontend :gear:| Description|
-------|------------|
CSS    | Everything within the pages were styled using CSS, the design again is very minimilistic but clean and easy to use. Also, used it as a way to make it responsive to phones and other devices. 
Django + Bootstrap| Visual aspects such as the textfield and button elements.
HTML   | Stores the Home/About pages, also used it to template tag all the necessary elements such as displaying the weather conditions which I defined via the Django application.
Crispy | A Django module which allows us to style our input fields to look much nicer than that of the default HTML fields which don't have much of an appearance to them, this is more so of a UI improvement than anything else.
JavaScript | Used to implement the basic functionality of the graph when the user ineracts with it, the form is posted via a mthod which then appends the given data to the JavaScript chart to dynamically display the given infomation.

Backend :toolbox:| Description|
-------|------------|
Django | Django is a well known Python backend web framework which I used to gather all the necessary information. Mainly used for template tagging and connecting all the HTML pages as well as migrating my project to a database. Also used as a form of site/token protection from malicious intruders.
Python | All the script was written in Python alongside Django for backend implementation primarily functions regarding the logic for how the user logs into the website and logouts.
SQLLite | Used SQL to save save user input within the database which can then be retrieved thus being able to see the dynamic graph changes in real time. The database can also be resetted using the "Reset" button within the input area.
requests | Allows grabbing of the api which we can then display the information to the user with ease. When implementing this we grab the submitted data which can then later be maipulated for ease of access via the database.

Libraries :books:| Description|
-------|------------|
whitenoise| Due to the fact Django does not have a way of supporting static files into production, whitenoise clears this barrier by placing all the required information into it's own separate folder which the web host (Heroku) can read from and apply any new changes.
gunicorn| [Gunicorn](https://github.com/benoitc/gunicorn) known as 'Green Unicorn' is a Python specific web server gateway. I used it as a way to pass requests data to my web application all through Heroku.
sqlparse | When posting some data to the database we must make sure that it has proper input being sent via the fields, this allows us to retrieve any bad data and convert it to the correct format preventing any breaks within our database and thus allowing for a stable workflow.

Web-services :spider_web:| Description|
-------|------------|
Heroku | Heroku is a cloud platform for hosting and maintaining website information which I used to later connect the platform with GoDaddy. 
GoDaddy| Domain was registered from GoDaddy alongside all DNS setup.

# Visual Example
<img width="1674" alt="Screen Shot 2023-01-11 at 2 45 51 PM" src="https://user-images.githubusercontent.com/48189579/211903447-a2c9431e-716b-40e3-8a97-1d1da75184f7.png">

<img width="1674" alt="Screen Shot 2023-01-11 at 2 46 05 PM" src="https://user-images.githubusercontent.com/48189579/211903470-29d40c9a-2be2-4c43-91e9-1ed1675cd48e.png">

<img width="1674" alt="Screen Shot 2023-01-11 at 2 47 18 PM" src="https://user-images.githubusercontent.com/48189579/211903496-2bfc8735-4521-4525-8c32-10a9fc428516.png">

<img width="1674" alt="Screen Shot 2023-01-11 at 2 47 33 PM" src="https://user-images.githubusercontent.com/48189579/211903519-757eda5f-a6d8-4fa8-b39a-ff7911251099.png">

