from rest_framework import serializers  # Import Django REST Framework's serializer module
from .models import Moviedata  # Import the Moviedata model

# Define a serializer for the Moviedata model
class MovieSerializer(serializers.ModelSerializer):
  
  # Meta class provides configuration for the serializer
  class Meta:
    image = serializers.ImageField(max_length=None, use_url=True)
    model = Moviedata  # Specifies which model to serialize
    fields = ['id', 'name', 'duration', 'rating', 'genre', 'image']  # Defines which fields to include in the API response