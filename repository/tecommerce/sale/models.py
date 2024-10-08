from django.db import models
from client.models import ModelBase
from employee.models import Employee
from product.models import Product
from client.models import Client


# Create your models here.

class Sale(ModelBase):
    id_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    nrf = models.CharField(
        max_length=255,
        null=False,)