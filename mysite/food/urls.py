
from . import views # Import views from the current directory
from django.urls import path

app_name = 'food'

urlpatterns = [
  # /food/
  path('', views.IndexClassView.as_view(),name='index'), #Maps the root URL ('/') to the 'index' view in views.py

  #food/1
  path('<int:pk>/', views.FoodDetail.as_view(),name='detail'),

  #/food/add
  path('add/', views.CreateItem.as_view(), name='create_item'),

  #edit
  path('update/<int:id>/', views.update_item, name ='update_item'),

  #delete
  path('delete/<int:id>/', views.delete_item, name='delete_item'),
]