from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata

# ViewSet for handling API operations on Moviedata
class MovieViewSet(viewsets.ModelViewSet):
    """
    MovieViewSet automatically provides API endpoints for Moviedata.
    It includes standard CRUD operations: list, create, retrieve, update, delete.
    """
    queryset = Moviedata.objects.all()  # Retrieves all movie records from the database
    serializer_class = MovieSerializer  # Uses MovieSerializer to convert data to/from JSON


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre='action')
    serializer_class = MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre='comedy')
    serializer_class = MovieSerializer