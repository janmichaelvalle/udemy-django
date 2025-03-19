from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator  # Import Django's built-in Paginator for pagination

# Create your views here.
def movie_list(request):
  """
  This view retrieves all movie objects from the database and paginates them.
  """
  movie_objects = Movies.objects.all()  # Retrieve all movie objects

  movie_name = request.GET.get('movie_name')  # Get the movie name from the request's GET parameters

  if movie_name != '' and movie_name is not None:
    # Filter the movie objects to include only those whose name contains the search query
    movie_objects = movie_objects.filter(name__icontains=movie_name)
    # name__icontains is a Django QuerySet filter lookup used to search for case-insensitive matches within a text field.

  # Create a Paginator instance with 2 movies per page
  paginator = Paginator(movie_objects, 2)  

  # Get the current page number from the request parameters
  page = request.GET.get('page')  

  # Retrieve the corresponding page from the paginator
  movie_objects = paginator.get_page(page)  

  # Render the template with the paginated movie objects
  return render(request, 'newapp/movie_list.html', {'movie_objects' : movie_objects})