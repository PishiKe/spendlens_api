from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Sum
from rest_framework import viewsets, views
from . import serializers
from . import models

class ExpenseViewset(viewsets.ModelViewSet):
  serializer_class = serializers.ExpenseSerializer
  queryset = models.Expense.objects.all()


class MonthlyExpenseView(views.APIView):
  def get(self, request):
    now = timezone.now()
    current_month_expenses = models.Expense.objects.filter(
      date__year=now.year, date__month=now.month, user=request.user
      ).aggregate(total_expense=Sum('amount'))

    return Response({"total_expense": current_month_expenses["total_expense"] or 0})