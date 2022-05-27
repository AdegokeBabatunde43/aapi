from datetime import datetime
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)
    price = models.IntegerField()
    created_date = models.DateTimeField(default = datetime.now)
    
    def __str__(self):
        return self.name