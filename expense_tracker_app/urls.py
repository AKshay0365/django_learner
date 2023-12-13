from django.urls import path
from .views import display_menu, add_expense, view_expenses, calculate_total_expenses

urlpatterns = [
    path('', display_menu, name='display_menu'),
    path('add/', add_expense, name='add_expense'),
    path('expenses/', view_expenses, name='view_expenses'),
    path('total/', calculate_total_expenses, name='calculate_total_expenses'),
]
