from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
  if request.method == 'POST': #Checks if the form was submitted via POST method (meaning the user is trying to create an account)
    form = RegisterForm(request.POST) #Creates a new instance of UserCreationForm, populating it with user-submitted data (request.POST)
    if form.is_valid(): #Validates the form (e.g., checks if passwords match and username is unique)
      form.save()
      username = form.cleaned_data.get('username') #Retrieves the username from the form.cleaned_data -- a dictionary-like object that contains the validated and sanitized data from the form. get('username') -> Extracts the value of the ‘username’ field that the user entered.
      messages.success(request, f'Welcome {username}, your account is created') #Saves a success message that will be displayed to the user after registration. messages.success(request, message) -- a built-in Django messaging framework method that stores temporary success messages. 
      return redirect('login') #Redirects the user to logic page after successful registration
  else: #If the request is NOT POST (i.e., the user just opened the registration page), an empty form is created.
    form = RegisterForm() 
  return render(request, 'users/register.html', {'form' : form}) #Renders register.html, passing the form as context ({'form': form}) to be displayed in the template.

@login_required
def profilepage(request):
  return render(request, 'users/profile.html')
