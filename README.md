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
