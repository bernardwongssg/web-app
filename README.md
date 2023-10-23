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

# Interesting Q&A
Why isn't the urls.py auto-generated? 
- sometimes apps only do internal things, urls.py is only useful routing users to pages specific to that app 
- reference: https://stackoverflow.com/questions/59480290/why-is-the-urls-py-file-not-created-automatically
Why use include() instead of importing apps?
- include() is used primarily for using urls.py files for each app, if the app doesn't have a urls.py file then importing might be ideal. However, importing for urls.py will lead to cyclical imports of the app which isn't ideal
