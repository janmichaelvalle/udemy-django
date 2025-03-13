from django import forms  # Import Django forms
from django.contrib.auth.models import User # Import Django's built-in User mode
from django.contrib.auth.forms import UserCreationForm # Import Django's pre-built UserCreationForm

class RegisterForm(UserCreationForm): #Extending UserCreationForm
  email = forms.EmailField() # Creates an email input field in the form.

  class Meta: # Meta class to define model-related configurations
    model = User  # Specify that this form is based on Django's User model
    fields = ['username', 'email', 'password1', 'password2'] # Fields to be used in the form

