from django.db import models


class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True
    )

    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )

    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True
    )

    modified_at = models.DateTimeField(
        db_column='dt_modified',
        auto_now=True,
        null=True
    )

    class Meta:
        abstract = True
        managed = True


class Client(ModelBase):

    name = models.CharField(
        db_column='name',
        max_length=70,
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


class Product(ModelBase):
    description = models.TextField(
        db_column='description',
        null=False
    )

    quantity = models.IntegerField(
        db_column='quantity',
        null=False,
        default=()
    )