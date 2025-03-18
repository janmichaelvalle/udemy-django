"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from movies.views import MovieViewSet, ActionViewSet, ComedyViewSet  # Importing relevant viewsets

# Creating a router to automatically generate API routes for ViewSets
router = routers.SimpleRouter()
router.register('movies', MovieViewSet)  # Registers 'movies/' endpoint with MovieViewSet
router.register('action',ActionViewSet, basename="action_movies")
router.register('comedy',ComedyViewSet, basename='comedy_movies')

urlpatterns = [
    path('', include(router.urls)),  # Mounts all API routes handled by the router
    path('admin/', admin.site.urls),  # Django Admin Panel
]+static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

# Now, the following API endpoints are automatically generated:
# GET /movies/       -> List all movies
# POST /movies/      -> Create a new movie
# GET /movies/<id>/  -> Retrieve a specific movie
# PUT /movies/<id>/  -> Update a specific movie
# DELETE /movies/<id>/ -> Delete a specific movie
