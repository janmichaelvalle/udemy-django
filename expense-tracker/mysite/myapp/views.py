from django.shortcuts import render, redirect
from .forms import Expenseform
from .models import Expense
import datetime
from django.db.models import Sum


# View for the homepage where users can add expenses
def index(request):
  if request.method == "POST":  # If form is submitted
    expense = Expenseform(request.POST)  # Create form instance with submitted data
    if expense.is_valid():  # Validate form data
      expense.save()  # Save new expense to the database
  
  expenses = Expense.objects.all()  # Retrieve all expenses
  total_expenses = expenses.aggregate(Sum('amount'))

  # Logic to calculate 365 days expenses
  last_year = datetime.date.today() - datetime.timedelta(days=365)
  last_year_expenses = Expense.objects.filter(date__gt=last_year)
  total_yearly_expenses = last_year_expenses.aggregate(Sum('amount'))

  # Logic to calculate 30 days expenses
  last_month = datetime.date.today() - datetime.timedelta(days=30)
  last_month_expenses = Expense.objects.filter(date__gt=last_month)
  total_monthly_expenses = last_month_expenses.aggregate(Sum('amount'))

  # Logic to calculate 7 days expenses
  last_week = datetime.date.today() - datetime.timedelta(days=7)
  last_week_expenses = Expense.objects.filter(date__gt=last_week)
  total_weekly_expenses = last_week_expenses.aggregate(Sum('amount'))


  daily_sums = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))

  expense_form = Expenseform()  # Create an empty form instance for new expenses
  return render(request, 'myapp/index.html', {'expense_form': expense_form, 'expenses': expenses, 'total_expenses': total_expenses, 'total_yearly_expenses': total_yearly_expenses, 'total_monthly_expenses': total_monthly_expenses, 'total_weekly_expenses': total_weekly_expenses, 'daily_sums': daily_sums})

# View for editing an existing expense
def edit(request, id):
  expense = Expense.objects.get(id=id)  # Retrieve the specific expense by ID

  # Pre-populate the form with existing data
  expense_form = Expenseform(instance=expense)

  if request.method == "POST":  # If form is submitted
    expense = Expense.objects.get(id=id)  # Fetch the same expense again
    form = Expenseform(request.POST, instance=expense)  # Bind submitted data to the existing expense
    
    if form.is_valid():  # Validate form data
      form.save()  # Save the updated expense
      return redirect('index')  # Redirect back to the main page

  return render(request, 'myapp/edit.html', {'expense_form': expense_form})  # Render the edit page


def delete(request, id):
  if request.method == 'POST' and 'delete' in request.POST:
    expense = Expense.objects.get(id=id)
    expense.delete()
    return redirect('index')