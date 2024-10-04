from django.db import models


class Cliente(models.Model):
    name = models.CharField(
        db_column='tx_name',
        max_length=100,
        null=False
    )

    agr = models.IntegerField(
        db_column='tx_age',
        null=False
    )