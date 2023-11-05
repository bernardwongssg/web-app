"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 

# for the MEDIA_ROOT config
from django.conf import settings
from django.conf.urls.static import static

# good practice to rename views import 
from django.contrib.auth import views as auth_views 
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # views from user 
    path('register/', user_views.register, name = 'register'),
    path('profile/', user_views.profile, name = 'profile'),
    # logging in/out
    # by default auth_views.LoginView and auth_views.LogoutView look for a registration folder in templates, 
    # so we change to users folder instead 
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    # navigating through blogs 
    path('', include('blog.urls')), # use include to map which route should have which URLs. in this case, blog/ uses blog/urls.py 

]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
