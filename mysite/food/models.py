from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):

  def __str__(self):
    return self.item_name

  user_name = models.ForeignKey(User,on_delete=models.CASCADE, default=1) #Each Item belongs to a User via a ForeignKey
  item_name = models.CharField(max_length=200)
  item_desc = models.CharField(max_length=200)
  item_price = models.IntegerField()
  item_image = models.CharField(max_length=500, default="https://cdn-icons-png.flaticon.com/512/1377/1377194.png")


  def get_absolute_url(self):
    """
    The reverse function from django.urls is used to dynamically generate a URL for a given named route (URL pattern). Instead of hardcoding URLs, Django will generate the correct URL based on the URL name and parameters.
      Generates the absolute URL for this Item instance.
      - Uses `reverse` to dynamically generate the URL instead of hardcoding it.
      - `"food:detail"` refers to the named URL pattern in `urls.py` (inside the `food` app).
      - `kwargs={"pk": self.pk}` passes the primary key (`pk`) of the item to the URL.
      Example:
      If an Item has `pk=5`, this method will return `/food/5/`
      instead of manually writing "/food/5/".
      """
    return reverse("food:detail", kwargs={"pk": self.pk})
    """
    - "food:detail" → This is the named URL pattern from urls.py. The namespace "food" means it comes from the food app.
    - kwargs={"pk": self.pk} → This dynamically generates the URL by replacing {pk} in the URL pattern with self.pk (the primary key of the item)
    """
