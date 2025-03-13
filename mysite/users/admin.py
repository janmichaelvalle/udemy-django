from django.contrib import admin
from .models import Profile #import profile model

# Register your models here.
admin.site.register(Profile) #makes the Profile model visible in the Django Admin Panel.