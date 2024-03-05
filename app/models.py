from django.db import models
from app.models import *

# Create your models here.

class productcategory(models.Model):
    product_categery_id =models.IntegerField(primary_key=True)
    product_categery_name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.product_categery_name


class product(models.Model):
    product_categery_id=models.ForeignKey(productcategory,on_delete=models.CASCADE)
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField()
    product_brand=models.CharField(max_length=100)
