from django.db import models
from django.contrib.auth.models import User

from PIL import Image

# Create your models here.
# creating profile with 1 to 1 relationship; 1 user can have 1 profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) # when user gets deleted, profile also gets deleted, but NOT vice versa 
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics') # directory that images get uploaded to

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save() # parent's method save() will run (in this case, models)

        img = Image.open(self.image.path)
        print(self)
        print('image URL: ' + str(self.image.url))
        print('image Path: ' + str(self.image.path))

        if img.height > 300 or img.width > 300: 
            output_size = (300, 300)
            img.thumbnail(output_size) # resizes image 
            img.save(self.image.path) # saves the image into self's image path           