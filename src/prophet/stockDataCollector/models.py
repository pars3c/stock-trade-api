from django.db import models

# Create your models here.
class stockData(models.Model):
    symbol_trade = models.CharField(max_length=10)
    date_trade = models.DateTimeField()
    open_trade = models.FloatField()
    close_trade = models.FloatField()
    low_trade = models.FloatField()
    high_trade = models.FloatField()
    volume_trade = models.IntegerField()

class companyNames(models.Model):
    symbol_trade = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)
    show_active = models.BooleanField(null=True)
