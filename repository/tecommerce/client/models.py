from django.db import models


class Abstrata_modelo_base(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True
    )

    active = models.BooleanField(
        db_column='active',
        null=False,
        default=True
    )

    created_at = models.DateTimeField(
        db_column='created_at',
        auto_now_add=True,
        null=True
    )

    modified_at = models.DateTimeField(
        add_colum='modified_at',
        auto_now=True,
        null=True
    )

    class Meta:
        abstract = True
        managed = True


class Cliente(Abstrata_modelo_base):

    name = models.CharField(
        db_column='name',
        max_length=100,
        null=False
    )

    age = models.IntegerField(
        db_column='age',
        null=False
    )

    rg = models.CharField(
        db_column='rg',
        max_length=12,
        null=False
    )

    cpf = models.CharField(
        db_column='cpf',
        max_length=12,
        null=False
    )


class Product(Abstrata_modelo_base):
    description = models.TextField(
        db_column='description',
        null=False
    )

    quantity = models.IntegerField(
        db_column='quantity',
        null=False
    )

class Employee(Abstrata_modelo_base):
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