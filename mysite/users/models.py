from django.db import models
from django.contrib.auth.models import User #import user model

# Create your models here.
class Profile(models.Model):
  '''
  EXTENDING USER WITH ONETOONEFIELD
  •	The User parameter refers to Django's built-in User model, meaning each profile is linked to a specific user.
	•	One-to-One Relationship: Each user gets exactly one profile.
	•	on_delete=models.CASCADE: If the user is deleted, the profile is deleted as well.
  '''
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  '''
  ADD A PROFILE PICTURE
  •	ImageField: Allows users to upload profile pictures.
	•	default='profilepic.jpg': If the user doesn’t upload a picture, 'profilepic.jpg' is used as the default.
	•	upload_to='profile_pictures': Images will be stored in the media/profile_pictures/ directory
  '''
  image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
  # if you are using image field, you need to install pillow (pip install pillow)


  location = models.CharField(max_length=100) #Stores the user’s location as text (up to 100 characters).

  def __str__(self):
    return self.user.username #Returns the username when querying Profile objects in Django’s admin panel or shell.

'''
python3 manage.py makemigrations
python3 manage.py migrate
'''
