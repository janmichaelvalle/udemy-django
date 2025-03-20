from django.shortcuts import render
from .forms import Expenseform
from .models import Expense

# Create your views here.
def index(request):
  if request.method == "POST":
    expense = Expenseform(request.POST)
    if expense.is_valid():
      expense.save()
  expenses = Expense.objects.all()
  expense_form = Expenseform()  # Creates an empty form instance. It’s like initializing an empty form so the template can render it.
  return render(request, 'myapp/index.html', {'expense_form': expense_form, 'expenses': expenses})
