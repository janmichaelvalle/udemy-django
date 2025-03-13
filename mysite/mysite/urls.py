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
from users import views as user_views 	# Imports the views.py module from the users app and renames it as user_views for clarity and avoid conflicts
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static
'''
	1.	from django.conf import settings
    - This imports the Django settings module (settings.py), allowing you to access global configurations like DEBUG, MEDIA_URL, and MEDIA_ROOT.
	2.	from django.conf.urls.static import static
	- This imports Django’s static() helper function, which serves media files (e.g., uploaded images) during development.
'''



urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')), # Connects url.py(food) to this file which is urls.py(mysite),
    path('register/', user_views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile', user_views.profilepage, name='profile'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
	1.	settings.DEBUG Check
	    •	It only runs when DEBUG = True in settings.py.
	    •	This is a development-only feature. In production, media files should be served by a proper web server, not Django.
	2.	static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	    •	settings.MEDIA_URL: Defines the base URL for media files (e.g., /pictures/).
	    •	settings.MEDIA_ROOT: Specifies where uploaded files are stored (BASE_DIR / 'pictures').
	    •	static(): A helper function that tells Django to serve these files.
'''

# urlpatterns += [
#     # ... the rest of your URLconf goes here ...
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)