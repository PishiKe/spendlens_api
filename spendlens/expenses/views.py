from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework import viewsets, views
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Sum
from . import serializers
from . import models

class ExpenseFilter(filters.FilterSet):
  month = filters.CharFilter(method='filter_by_month')

  def filter_by_month(self, queryset, name, value):
    try:
      year, month = map(int, value.split('-'))
      return queryset.filter(date__year=year, date__month=month)
    except ValueError:
      return queryset.none()

class ExpenseViewset(viewsets.ModelViewSet):
  serializer_class = serializers.ExpenseSerializer
  queryset = models.Expense.objects.all()
  filter_backends = [DjangoFilterBackend]
  filterset_class = ExpenseFilter
  filterset_fields = ['user', 'date']

class MonthlyExpenseView(views.APIView):
  def get(self, request):
    now = timezone.now()
    current_month_expenses = models.Expense.objects.filter(
      date__year=now.year, date__month=now.month, user=request.user
      ).aggregate(total_expense=Sum('amount'))

    return Response({"total_expense": current_month_expenses["total_expense"] or 0})