from django.db import models

class Expense(models.Model):
    category = models.CharField(max_length=255)
    amount = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.category} - ₹{self.amount:.2f} on {self.date}"

class Meta:
    app_label = 'expense_tracker_app'
