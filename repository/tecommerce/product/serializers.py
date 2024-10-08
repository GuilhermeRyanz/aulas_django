from rest_framework import serializers
from product import models


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    description = serializers.CharField()
    quantity = serializers.IntegerField()
    dt_modified = serializers.DateTimeField()
    cs_active = serializers.CharField()

    class Meta:
        model = models.Product
        fields = 'id', 'description', 'quantity', 'dt_modified', 'cs_active'

