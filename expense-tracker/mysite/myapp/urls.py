from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Homepage where expenses are listed and new ones can be added.
    path('edit/<int:id>/', views.edit, name='edit'),  # Edit page, dynamically fetching expense by its ID.
    path('delete/<int:id>/', views.delete, name='delete'),
]
