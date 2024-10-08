from django.db import models
from client.models import ModelBase

# Create your models here.

class Employee(ModelBase):
    name = models.CharField(
        db_column='name',
        max_length=70,
        null=False

    )

    registraction = models.CharField(
        db_column='registraction',
        max_length=15,
        null=False
    )