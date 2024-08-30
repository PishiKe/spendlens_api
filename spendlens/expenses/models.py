from django.db import models
from django.utils import timezone

class Currencies(models.Model):
  name = models.CharField(max_length=50)

  class Meta:
    verbose_name = 'Currency',
    verbose_name_plural = 'Currencies'

  def __str__(self):
    return self.name

class Expenses(models.Model):
  name = models.CharField(max_length=256, null=True, blank=True)
  description = models.CharField(max_length=256, null=True, blank=True)
  date = models.DateTimeField(default=timezone.now)
  amount = models.FloatField(max_length=100, null=True,blank=True)
  currency = models.ForeignKey(Currencies, on_delete=models.PROTECT, related_name='currency', blank=True, null=True)

  class Meta:
    verbose_name = 'Expense'
    verbose_name_plural = 'Expenses'

  def __str__(self):
    return self.description