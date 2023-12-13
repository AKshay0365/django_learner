# expense_tracker_app/views.py
from django.db import models
from django.shortcuts import render
from .models import Expense
from django.http import HttpResponseRedirect
from .forms import ExpenseForm

def display_menu(request):
    return render(request, 'menu.html')

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/expenses/')
    else:
        form = ExpenseForm()

    return render(request, 'add_expense.html', {'form': form})

def view_expenses(request):
    expenses = Expense.objects.all()
    return render(request, 'view_expenses.html', {'expenses': expenses})

def calculate_total_expenses(request):
    total = Expense.objects.aggregate(models.Sum('amount'))['amount__sum'] or 0
    return render(request, 'total_expenses.html', {'total': total})
