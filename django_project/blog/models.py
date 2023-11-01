from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # default users from django 

class Post(models.Model):
    title = models.CharField(max_length = 100) # characterfield
    content = models.TextField() # similar to char field, unrestricted text
    date_posted = models.DateTimeField(default = timezone.now) # passes in function b/c you don't necessarily want to immediately execute function 
    # on_delete gives instructions on what happens if User gets deleted
    # ForeignKey is used to map many-to-one relationships 
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
    
