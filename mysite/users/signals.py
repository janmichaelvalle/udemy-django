from django.db.models.signals import post_save  # Signal that runs after saving a model
from django.contrib.auth.models import User  # Django's built-in User model
from django.dispatch import receiver  #Decorator to register signal handlers
from .models import Profile  #Import Profile model to create/update when a User is saved

# 🔹 Signal to create a Profile when a new User is created
@receiver(post_save, sender=User)  #Listens for post_save signal on the User model
def build_profile(sender, instance, created, **kwargs):
    if created:  # Check if this is a new User (not an update)
        Profile.objects.create(user=instance)  # Create a Profile linked to this User

# 🔹 Signal to save the Profile when the User is updated
@receiver(post_save, sender=User)  # Listens for post_save signal on the User model
def save_profile(sender, instance, **kwargs):
    instance.profile.save()  # Ensure Profile is saved when User is saved

'''
Paramaters
1. sender - The model that sent the signal (in this case, User)
2. instance - The specific instance  of the model that was saved (i.e., the specific user)
3. created - A boolean (True or False) that indicates if the object was created (True) or updated (False)
4. **kwargs - Stands for "keyword arguments" allows passing additional data if needed (e.g., signal metadata).
'''