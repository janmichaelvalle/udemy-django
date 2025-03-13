from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):

  def __str__(self):
    return self.item_name
  
  user_name = models.ForeignKey(User,on_delete=models.CASCADE, default=1) #Each Item belongs to a User via a ForeignKey
  item_name = models.CharField(max_length=200)
  item_desc = models.CharField(max_length=200)
  item_price = models.IntegerField()
  item_image = models.CharField(max_length=500, default="https://cdn-icons-png.flaticon.com/512/1377/1377194.png")
