from django.db.models.signals import post_save # fired after object is saved
from django.contrib.auth.models import User # sender, sends the signal 
from django.dispatch import receiver # receiver, receives the signal and performs the task 
from .models import Profile 

'''
when a User is saved, send signal post_save to receiver @receiver. post_save will send all the arguments 
needed in the receiver's task (in this case create_profile() is the task) and run the task 
'''
# we want a user profile to be made every time a user is made
@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

# we want a user profile to be saved every time changes are made 
@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()