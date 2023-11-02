# djangotutorial
Following along Corey Schafer's tutorial to get a better understanding of Django concepts. Reference playlist: https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p

# General Comments 
### Lesson 1 (10.22.23)
- learned how to start up a project (django-admin startproject ____) and add an app within the project (python manage.py startapp ____)
- learned about the files that automatically get generated along with how to start up the project (python manage.py runserver)

### Lesson 2 (10.22.23)
- learned about creating the urls.py file for an app, which maps a URL to a a function in the views.py file
- learned about the process of URLS: first django looks through the projects url.py file and sees if the URL has any pattern matches. if there are and the url has an include() method, it'll chop off the match and then continue looking for urlpatterns in the urls.py file in the include() method. eventually the URL will point to a method in a views.py file
- learned that the benefit of searching project urls and then app urls is that it allows us to quickly change batches of app urls without needing to change each individual one; we just simply have to change the url pattern in the project urls.py file
- learned that we can set an application to be the main page by leaving the url pattern to an empty string '' in the project urls.py file

### Lesson 3 (10.28.23)
*Setting Up Templates Folder*
- by default Django will look within each installed app for a Templates folder
- press shift + 1 in an HTML file to auto generate the basic HTML template
- remember to add an application within the settings.py file. This will ensure that templates are properly searched for, databases are properly set, etc. Add the class within an applications apps.py file into the 'INSTALLED_APPS' list in your project's settings.py file

*Rendering Templates Using Functions in views.py*
- you can properly render a template and pass it as an HttpResponse using the render() function from django.shortcuts. This takes in the request, the file path to the template, and context which is a dictionary of values to pass into the template
- views always need to return an HttpResponse or an exception
*Using the data dynamically that's passed into render()*
- a dictionary of values can be passed into a template for data to dynamically displayed
- logic code is written in within {% %} blocks, variables access is written in {{ }} blocks. Dictionary values can be accessed using .
- note that for logic code you always have to include an {% end_ %} block to signify end of logic. You can do basic stuff like for loops, if/else, while

*Template Inheritance*
- Template inheritance is useful when you have multiple templates sharing similar HTML code. Things like headers, footers, etc. will oftentimes get carried over. Using the block function you can create a section that child templates can override.
- block sections can be created with {% block blockname %} and closed with {% endblock %}. Then for each child template you can just include {% extends filepath_to_parent %} and the included block section functions 

*Static Folder*
- CSS and JS need to be located in a static folder located within each app
- you can import static files by including {% load static %} at the beginning of your code
- you can then load in certain files uing '{% static 'filepath_to_file'%}' in href. The static statement generates the absolute URL of the file

*URL Etiquette*
- Any time you use URLs in a template, it's a good idea to use {% url 'url_name' %} so that if you ever change URL names or functions it will transfer over everywhere. This is also why setting a name for each urlpattern in urls.py is a good idea

### Lesson 4 (10.31.23)
*Setting Up the Admin Page*
- Before you can create a user for the admin page you have to make migrations so the default tables are built
- you can use the command 'python manage.py createsuperuser' to create credentials for the admin page
- each user has different permissions, staff allows the user to log into the admin site and superuser allows the user to make changes

### Lesson 5 (11.1.23)
*Basics about the Database*
- Django has a built in ORM (object relational mapping) that allows for you to use different databases without changing your code. All the code to query ANY database remains the same, you just connect different databases in the settings.py file
- The ORM is represented as models in models.py which is extremely similar to classes
- when creating a model there are differetn data types and fields that you can use (example list can be found [here]([https://duckduckgo.com](https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/#))). ForeignKey() is used when mapping a many-to-one relationship (more about this can be found [here](https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_one/))
- remember to call manage.py makemigrations (to make the migration file) and manage.py migrate (to actually run the migration file and make the models)
- if you're more comfortable interpretting SQL, you can call python manage.py sqlmigrate 'app_name' 'migration_number'

*Playing around with the Shell*
- you can use the python shell to play around with making models; these would be similar to the functions made in views.py. You can use the command 'python manage.py shell' to run python commands
- remember that model objects are saved into the database until you call the save() method
- if you want to find all the items mapped to a foreignkey, you can take the foreign key and call the function 'modelname_set' to get the query. ex) say you have a ForeignKey User in the model Post, where a User can have multiple Posts but not vice versa. You can select a user (say user_1) and call user_1.post_set.all() to get all the Posts that user_1 is connected to (the attribute is called post_set b/c the model is named Post)
- you can also use 'modelname_set' to add into the model. ex) user_1 could make a post by doing user_1.post_set.create('insert Post attributes here'). You don't need to include the foreign key into the model set's attributes (b/c the foreign key is the one creating it) and you don't need to save the model, it's done automatically

*Using the Database in views.py*
- in the views.py file make sure you import whatever Model you're using from the models.py file. You can then use the same querying code mentioned in the previous section

*Changing the format of Database Attributes* 
- Django has some built in filters for some of the database attributes that can prove to be useful. If you want to make changes, go to the html file pulling the attribute and call the filter with '|'. ex) if I have a Post model with the date_posted attribute, I can filter just the date by doing {{ post.date_posted|date:"F d, Y" }}. More about built in filters can be found [here](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#filter)

*Viewing Databases on the Admin Page*
- In order to view your newly created Models/Databases you have to register your models in the app's admin.py page. You can do this by importing the model in admin.py and calling the method admin.site.register('model_name')

### Lesson 6 (11.1.23)
*Creating a User Creation Form* 
- Django has some built in classes that you can import and use, especially for forms
- Note that you can extend templates from other apps, this is why the internal folder with the app name is useful
- Django requires that all forms have a CRSF token, which is just built in security that helps prevent malicious attacks. This can be included in the form using the code snippet {% csrf_token %}
- you can render certain items as paragraph tags using the .as_p method; ex) say you're passing in a form, form.as_p will render it using paragraph tags and most likely make it look better

*Understanding Requests*
- there are different types of HTTP requests but the most basic kinds are get requests and post requests. get requests are typically for navigating pages, post requests pass in information.

Understanding Messages* 
- theres a default class called messages that you can import from django.contrib that allows for 'flash messages', or messages that display as a one time notification. The framework allows you to save a message in one request and retrieve it for display in a different request (typically the next one). More can be found out about it [here](https://docs.djangoproject.com/en/4.2/ref/contrib/messages/)
- messages options include .add_message, .debug, .info, .success, .warning, .error

*Modifying Models* 
- Model Meta is basically the inner class of your model class. Model Meta is basically used to change the behavior of your model fields like changing order options, verbose_name, and a lot of other options. It’s completely optional to add a Meta class to your model. More can be read about it [here](https://www.geeksforgeeks.org/meta-class-in-models-django/#)

### Lesson 7 (11.2.23) 
*Setting up a Login System* 
- Django has default views that you can use to make logins and logouts. These are in django.contrib.auth
- You can figure out where Django's looking for URLs or views in the 404 error page; look for the request URL portion of the error
- If you don't want the login to redirect to your account info, you can set it up in the settings.py file using LOGIN_REDIRECT_URL and setting the variable to your intended url. ex) LOGIN_REDIRECT_URL = 'blog-home'

*Changing the HTML Based on Who's Logged In* 
- django has a user variable that contains the current user. This user variable has an attribute is_authenticated that allows you to determine if the user is logged in or not. You can set things using the snippet {% if user.is_authenticated %}. Note that you don't have to pass in user or anything in the requests context or anything, this is something that's built into Django

*Creating Routes That Are Only Accessible If You're Logged In*
- While you can technically make a view/URL html element only visible using the if snippet mentioned in the above section, there's nothing stopping the user from just manually typing out the URL. You can use a login_required declarator that Django provides by default. This can be imported using the following import: from django.contrib.auth.decorators import login_required. You can then put @login_required above any view function that you want requiring a logged in user. Note that this is different for classed based views
- Similar to the login system, you can set up which URL view functions with @login_required redirect to if you're not logged in by going into the settings.py file and using the LOGIN_URL variable. ex) LOGIN_URL = 'login' (where 'login' is the views URL name that loads the login screen)
- What's really neat about Django is that it will still save which URL you were trying to access even when it redirects you to whichever URL you set up as LOGIN_URL. You can see in the website login it will have /?next=/'URL_YOU_WANTED_TO_GO_TO'/ in the URL. Once you enter credentials it will load up the original URL you wanted to navigate to 

# Interesting Q&A
Why isn't the urls.py auto-generated? 
- sometimes apps only do internal things, urls.py is only useful routing users to pages specific to that app 
- reference: https://stackoverflow.com/questions/59480290/why-is-the-urls-py-file-not-created-automatically
Why use include() instead of importing apps?
- include() is used primarily for using urls.py files for each app, if the app doesn't have a urls.py file then importing might be ideal. However, importing for urls.py will lead to cyclical imports of the app which isn't ideal
What's the purpose of the nested app name folder structure for templates?
- it's just good practice, if you have two templates that are named the same but are meant to be used for two different applications, Django will select the first matched html file. By creating an internal folder with the app name, it'll look for the folder first and select the proper template
- reference: https://stackoverflow.com/questions/52231294/what-is-the-reason-for-the-nested-template-directory-structure-in-django
Why don't you need to download the files for some of the extra CSS/JS packages (bootstrap, dropzone, etc.)?
- the files are served from a content delivery network so we don't need to download any files
Why do my CSS changes not appear?
- Sometimes you have to close out of the server or reset browser cache. for mac it's cmd + shift + r, for windows it's ctrl + F5
How do you deal with importing views from multiple applications?
- In general it's good etiquette to always change the name of a views import since there's a high chance you'll import multiple views files. ex) if you want to import functions from app 'Users' and you want to import functions from app 'Blog' you'd want to do 'from users import views as user_views' and 'from blog import views as blog_views' or something similar  
What happens if I move templates over from one templates folder to another templates folder?
- What Django does is it looks through all the 'templates' folders, starting at the app but traversing through everything if the template isn't found. That's why having the internal folder with the application name is common practice, it prevents any issues with similar named html files. If I have two applications, Blog and User, and a 'templates' folder in both, proper HTML files will be found whether the 'blog' folder and 'users' folder are within their respective Blog and Users 'template' folder or if Blog has both the 'blog' and 'users' folder in its 'template' folder and Users has nothing (or vice versa). You can change the way Django looks for the templates folder as well. Read more about this interesting Django characteristic [here](https://learndjango.com/tutorials/template-structure#:~:text=Option%201%3A%20App%20Level,before%20adding%20your%20template%20file.)
