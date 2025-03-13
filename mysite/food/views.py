from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
def index(request):
  item_list = Item.objects.all() # Retrieve all items from DB
  context = {
    'item_list':item_list, # Pass the list to the template
  }
  return render(request, 'food/index.html',context) 

#ListView for items
class IndexClassView(ListView):
   model = Item;
   template_name = 'food/index.html'
   context_object_name = 'item_list'



# Render the template with context
def item(request):
  return HttpResponse('This is an item view')


def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
       'item':item,
    }
    return render(request, 'food/detail.html', context)


class FoodDetail(DetailView):
   model = Item
   template_name = 'food/detail.html'
   context_object_name = 'item'  # Makes it clear we are dealing with an "Item"


def create_item(request):
   form = ItemForm(request.POST or None)  # Create form instance, passing POST data if available

   if form.is_valid(): #Check if form input is valid
      form.save() #Save the form data as a new Item in the database
      return redirect('food:index') #Redirect back to the item list page
   
   return render(request, 'food/item-form.html', {'form':form})


def update_item(request, id):
   item = Item.objects.get(id=id)
   """
   id is passed from the URL (update/<int:id>/)
   In the parameters of the function that id is passed
   Item.objects.get(id = id) queries the DB to get that exact item
   """
   form = ItemForm(request.POST or None, instance=item)
   # instance=item tells Django that the form should be pre-filled with the existing item’s data. Instead of creating a new record, Django updates the existing item


   if form.is_valid():
      form.save()
      return redirect('food:index')
   
   return render(request, 'food/item-form.html', {'form':form, 'item':item}) # Render form with existing data because of 'item:item'


def delete_item(request, id):
   item = Item.objects.get(id = id)

   if request.method == 'POST':
      item.delete()
      return redirect('food:index')
   
   return render(request, 'food/item-delete.html', {'item': item})