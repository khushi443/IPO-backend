# ipo_app/models.py
from django.db import models

class IPO(models.Model):
    company_name = models.CharField(max_length=100)
    ipo_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.company_name