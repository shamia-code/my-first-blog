# python -m venv .env # starting a virtual environmennt called ".env" in  cmd
#.env\Scripts\activate #activating the virtual environment for use 
#Then install django into .env using pip install django
#django-admin.exe startproject mysite . #The dot(.) at the end tells the script to install django in the current directory in order to start a project 
#django-admin.py is a script that will create the directories and files for you e.g urls.py, wsgi.py etc 
#manage.py is a script that helps with management of the site (helps to start the web server ) 
#settings.py contains the configuration of your website
#urls.py conatins a list of patterns used by urlresolver
#After creating the site , go to settings and change the time-zone to your country time-zone in our case 'UTC+03:00 (EAT)'
#change the language-code to the language you want to use in our case 'en-US'
#Then we add a path for static files right below the static-url ie STATIC_ROOT =os.path.join(BASE_DIR,'static')
#change ALLOWED_HOSTS  to ['127.0.0.1','pythonanywhere.com']
# To add a database for your application , run  the 'python manage.py migrate' command in the terminal while in that directory
# To start the webserver  run the 'python manage.py runserver 
# To check whether the website is running , open the browser and type the 'http://127:0.0.1:8000/' 
# we use objects to store our posts . An object is a collection of properties and actions e.g an object cat has property color and does action purr
# a django model is a special kind of object  which is saved in a database.
#a database is where you store information about users ,your blog posts etc.
#To create an application in the project, run 'python manage.py startapp blog ' in the .env terminal.
# After creating an app,go to settiings -> INSTALLED_APPS and add a line containing 'blog.apps.BlogConfig' inorder to tell Django to use it .
#after creating the models, run 'python manage.py makemigrations blog ' to make django know that we have some changes in the blog app.
# after making the migration ,django prepares a migration file that we now have to apply to our database using 'python  manage.py migrate blog'
# To add , edit , delete the posts we've  just modeled , we use Django admin
# In blog/admin.py , we import the (Post ) and make it visible on the admin page  using 'admin.site.register(Post)'
# In the console, type python manage.py runserver  to  start the server,run the server with http://127.0.0.1:8080/admin/' in the browser.
# To log in , create a superuser account that has control over everything on the site 
# db.sqlite3 is the local database where all your users and posts are stored 