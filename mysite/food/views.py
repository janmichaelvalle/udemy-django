from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

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

# this is a class based view for create item
"""
CreateView is a Django generic class-based view that:
	•	Displays a form based on the Item model.
	•	Handles form submission and validates user input.
	•	Saves the new object to the database automatically.
"""
class CreateItem(CreateView):
   model = Item # Defines which model to use (Item model)
   fields = ['item_name', 'item_desc', 'item_price', 'item_image'] # Specifies which fields to include in the form
   template_name = 'food/item-form.html'  # The HTML template for the form

   def form_valid(self, form):
      form.instance.user_name = self.request.user  # Assigns the logged-in user as the creator
      return super().form_valid(form) # Calls the default form_valid() method and saves the form. super().method_name(arguments) calls a method from the parent class.

   """
   •	CreateView (Parent Class) already has a form_valid() method.
	•	CreateItem (Child Class) overrides form_valid() to add custom logic.
	•	Calling super().form_valid(form) ensures that Django still handles saving & redirection. form_valid() is already inside CreateView, but we override it inside CreateItem


   Django provides the form_valid() method, which runs after the user submits the form
      1. form.instance.user_name = self.request.user
         - What it does: Sets the user_name field of the Item to the currently logged-in user.
         - Why? Since user_name is a foreign key (linked to the User model), we need to set the currently logged-in user as the owner of the new item.
      2. return super().form_valid(form)
         - What it does: Calls the default form_valid() method from CreateView.
         - Why? It saves the form data to the database and redirects the user to the correct page.

   """


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