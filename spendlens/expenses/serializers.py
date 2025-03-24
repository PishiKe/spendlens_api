from rest_framework import serializers
from . import models

class ExpenseSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Expense
    fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Budget
    fields = '__all__'