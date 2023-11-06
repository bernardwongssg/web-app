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

### Lesson 6 (11.2.23)
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
- While you can technically make a view/URL html element only visible using the if snippet mentioned in the above section, there's nothing stopping the user from just manually typing out the URL. You can use a login_required declarator that Django provides by default. This can be imported using the following import: from django.contrib.auth.decorators import login_required. You can then put @login_required above any view function that you want requiring a logged in user. Note that this is different for classed based views; you can view these instructions [here](#decorators-in-classes)
- Similar to the login system, you can set up which URL view functions with @login_required redirect to if you're not logged in by going into the settings.py file and using the LOGIN_URL variable. ex) LOGIN_URL = 'login' (where 'login' is the views URL name that loads the login screen)
- What's really neat about Django is that it will still save which URL you were trying to access even when it redirects you to whichever URL you set up as LOGIN_URL. You can see in the website login it will have /?next=/'URL_YOU_WANTED_TO_GO_TO'/ in the URL. Once you enter credentials it will load up the original URL you wanted to navigate to 

### Lesson 8 (11.4.23)
*More about Models: One to One Relationships and Uploaded Files* 
- Say you want to create a profile for each User. You can use the default OneToOneField() from django.db models to set a 1 to 1 relationship
- You can also use ImageField and FileField to upload images and Files. You can set a default image/file and set where the files will be uploaded to in the directory with the upload_to variable

*Configuring Media for Better Organization* 
- if you configure upload_to to a folder, Django will auto-create the folder in the base directory. This can quickly clutter up your Django Project if you have a lot of models saving uploaded items. What you can do is configure a media folder in the settings.py file so that upload folders are generated as a subfolder. This can be done by setting the MEDIA_ROOT and MEDIA_URL
- Typical convention is MEDIA_ROOT = BASE_DIR / 'media' (which is the same as os.path.join(BASE_DIR, 'media') and setting MEDIA_URL = '/media/'. media_root is setting where the uploaded files will be available on the system, while MEDIA_URL is where uploaded files will be available on the browser. While both are not technically required, they're very useful for organization. More info and examples can be found [here](https://stackoverflow.com/questions/72083187/media-root-vs-media-url-django)
- When you set the MEDIA_ROOT, you have to configure some things within the project's url.py file for proper access. You can read more about it [here](https://docs.djangoproject.com/en/4.2/howto/static-files/#serving-files-uploaded-by-a-user-during-development), but note that the settings will differ when in the production environment, so static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) should only be added into urlpatterns when settings.DEBUG is True

*Django Signals*
- signals can be helpful if you need something to occur after something has been done; in short, a sender will send a signal to a receiver that performs an action depending on what the user has done. There are 4 parts to a signal: a sender, a receiver, a condition, and an action. The Sender will send the signal and is what starts off the chain. if the Sender hits a certain 'condition', then the signal will be sent to the receiver. Receiver will receive the signal and perform the action or task. As an example:
```
@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
```
the sender is the model User, the condition is post_save (after the sender has been saved), the receiver is @receiver, and the action is create_profile(). This code will create a new profile every time a User has been made 
- While this can technically be done as a Model, it's sometimes better to make signals to avoid import issues. You can read more about how to set up signals (you'll need a signals.py file and define a read() method in the apps.py file) [here](https://docs.djangoproject.com/en/4.2/topics/signals/). 

### Lesson 9 (11.5.23) 
*Creating a Model Form*
- A model form can be used to update models. Within the forms.py method you can create a class and set what the model is and set a list of fields that you want to take as inputs. Then in views you can save those form objects as key: value pairs in the context dictionary and render them in the HTML using crispy_forms_tags or anything that you'd prefer
- IMPORTANT NOTE: the form and request.FILES will only contain data if the request method was POST, at least one file field was actually posted, and the <form> that posted the request has the attribute enctype="multipart/form-data". Otherwise, request.FILES will be empty. More about this can be read [here](https://docs.djangoproject.com/en/4.2/topics/http/file-uploads/#basic-file-uploads)
- Say you want the request's model info to auto populate the form. You can use the variable instance = request.model_name to get the current model. ex) say you have a User model that you're trying to make updates from, and you have a UserUpdateForm() class that is meant to update the User model. You can do u_form = UserUpdateForm(instance = request.user) to pull the current User info to use in the HTML, and then pass in context = {'u_form': u_form} into the render() method that's returned

*Overriding the Model save() method*
- In this project, we might want to limit the size of the image to save space on the file system and decrease run time on the website (since the website has to send the entire data back and forth). Pillow can be used to auto-resize input images, and we can override the save() method to make this change
- we can go into our models.py file and override the save() method within a model. If we want to still use the model's default save() method we can just call super().save, but then we can do calculations to change saved files or saved items. This would also be an area to delete previous info, only include saves for other stuff, etc. It's not recommended to override the save() method unless you know what you're doing b/c you can cause issues with your database. An example of an overwritten save() method that saves a smaller version of the image can be seen here:
```
def save(self):
    super().save() # parent's method save() will run (in this case, models)

    img = Image.open(self.image.path)

    if img.height > 300 or img.width > 300: 
        output_size = (300, 300)
        img.thumbnail(output_size) # resizes image 
        img.save(self.image.path) # saves the image into self's image path           
```
More about overwritting the save() method can be read [here](https://www.geeksforgeeks.org/overriding-the-save-method-django-models/#)

### Lesson 10 (11.5.23)
*Class Based Views*
- class based methods in the views.py file have a lot of built in functionality that can handle some backend processes. There are a lot of different types of class based views; list_view, create_view, update_view, delete_view, etc. A lot of websites have similar functionality (blogs list bunch of stuff, youtube list subscriptions, etc. These are all examples of list_view). You can import these built in classes from django.views.generic
- You can then use these classes similar to the method based views() in urls.py. Note that you can't directly use the class, but these classes have a method called as_view() that converts the class properly. ex) say we have a PostListView class that inherits ListView from django.views.generic. in the urls.py file you'd have urlpatterns = [path('', PostListView.as_view(), name = 'blog-home'),]. HOWEVER, by default class based views look for a template in the format <app>/<model>_<viewtype>.html (so in this case it's looking for blog/post_list.html). You can set this template by setting the variable template_name. Along with that, you can pass your model items by setting context_object_name. TLDR: you need to set model, template_name, and context_object_name within a class based view. Here is an example of a method based view that loops through all the posts in the Post model:
```
# in views.py
def home(request): 
    posts = Post.objects.all()

    context = {
        'posts':  posts
    }
    return render(request, 'blog/home.html', context)

# in urls.py
urlpatterns = [path('', views.home, name = 'blog-home'),]
```
And here's an example of the same logic in a classed based view: 
```
# in views.py
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'

# in urls.py
urlpatterns = [path('', PostListView.as_view(), name = 'blog-home'),]
```
- in the methods based view() we basically have to create a function (render) and explicitely pass in the info, while for the class based view we're just setting variables
- General stuff about class based views can be seen [here](https://docs.djangoproject.com/en/4.2/topics/class-based-views/)

*More about the ListView Class* 
- you can easily change the ordering of the list in a ListView class by setting the ordering variable. ex) if you want to order by date_posted you can do ordering = ['-date_posted']
- more examples for the LIstView class can be found [here](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)
- Reference for ListView: [here](https://www.youtube.com/watch?v=-s7e_Fy6NRU&t=148s)

*Passing a variable through URLs*
- Django allows you to pull variables through URLs when you use the <> characters within the URL. As an example, if you have path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail') in your urlpatterns, the view PostDetailView will be able to pull the variable pk (which is set to be an integer) and use it within views(). B/c PostDetailView is a DetailView that already has a pk variable (primary key) we don't need to set anything in the view, but you can set it to be whatever variable within the view. More about this can be read [here](https://docs.djangoproject.com/en/4.2/topics/http/urls/#example)
- this URL can be accessed through html by doing href="{% url 'post-detail' post.id %}". post.id is passed into the <> section

*DetailView Class* 
- by default looks for <app>/<model>_detail.html
- good for pulling additional details about a certain item in a model
- expects objects to be called 'object'
- [reference link](https://www.youtube.com/watch?v=-s7e_Fy6NRU&t=639s)

*CreateView Class* 
- by default looks for <app>/<model>_form.html
- good for creating a new item in a model
- set the fields variable for inputs
- expects objects to be called 'form'
- may face IntegrityError if you haven't included all variables needed in the model, make sure everything's included somewhere in the class
- may face ImproperlyConfigured error (full error: No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.), which means the post has been created successfully but there's no direction for where to redirect. This can be set by defining a get_absolute_url() method within the model. ex)
```
class Post(models.Model):
    title = models.CharField(max_length = 100) # characterfield
    content = models.TextField() # similar to char field, unrestricted text
    date_posted = models.DateTimeField(default = timezone.now) # passes in function b/c you don't necessarily want to immediately execute function 
    # on_delete gives instructions on what happens if User gets deleted
    # ForeignKey is used to map many-to-one relationships 
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    # THIS IS THE IMPORTANT CODE
    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk': self.pk})

# urls.py
urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
]
```
You can also just set the variable success_attribute to whatever url you want within the CreateView class 
- [reference link](https://youtu.be/-s7e_Fy6NRU?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&t=1184)

*Decorators in Classes*
- say we want to use a decorator (you can review decorators in Django [here](#creating-routes-that-are-only-accessible-if-you're-logged-in)

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

When should you use Django signals?
- Django signals have their pros and cons. They're particularly useful amongst actions that multiple Apps need to do are might be interested in; say multiple Apps update a particular model, then it might be useful. More examples can be read [here](https://stackoverflow.com/questions/60679719/why-use-signals-in-django#:~:text=The%20Django%20Signals%20is%20a,this%20model%20can%20be%20updated.). It's important to note that signals have downsides where they're pretty hard to debug and follow along. A lot of times you can write functions and do things within models that you're trying to do in signals.py, so most people suggest trying to create methods first and using signals.py as a last resort. More can be read about it [here](https://lincolnloop.com/blog/django-anti-patterns-signals/)

I'm trying to upload a file using form requests but I'm not receiving any files, how come?
- there's a high possibility you forgot about enctype, make sure you have enctype="multipart/form-data" in your form and that method = "POST". Read more [here](https://docs.djangoproject.com/en/4.2/topics/http/file-uploads/#basic-file-uploads)

What's the difference between forms.Form vs forms.ModelForm?
- forms.Form are useful for when you're collecting/using data that doesn't necessarily interact with the models or databases. forms.ModelForm is when you're intereacting with models/databases b/c you avoid duplicating your model description. More about this can be read [here](https://stackoverflow.com/questions/2303268/djangos-forms-form-vs-forms-modelform)

What does the warning the browser gives me about 'reloading and resubmitting the form' mean?
- this occurs when you refresh the page and your page is going to set another POST request. My returning a redirect() method in your request.method == "POST" you submit a GET request instead, avoiding this warning

When should I use image.path or image.url?
- image.url is moreso used in the HTML and front-end/requests, image.path is used for file management and used within Python code. ex) here are some examples of an image's URL and Path. image URL: /media/profile_pics/1071061_oUEIkgY.jpg
image Path: /Github_Repos/Education/djangotutorial/django_project/media/profile_pics/1071061_oUEIkgY.jpg

When should I use CBV (class based views) and when should I use FBV (function based views)?
- CBV are good for organization and repeatability, FBV are very good for niche and unique functionalities. CBV are harder to interpret and harder for new Django users, there's a higher learning curve (learning which variables to set, how to access items in models, etc.). FBV are easier to create but can lead to repeating code that might be better represented in classes

What's the difference between redirect() vs reverse()?
- redirect() redirects you to a specific route, reverse() returns a full URL to that route as a str. reverse() is used when you just need the URL as a string and the view will handle the redirect() for us, reverse() is pretty useful for class based views 
