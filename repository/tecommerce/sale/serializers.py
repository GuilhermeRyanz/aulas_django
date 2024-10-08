from rest_framework import serializers
from sale import models

class SaleSerializer(serializers.ModelSerializer):
    class EmployeeSerializer(serializers.ModelSerializer):
        id = serializers.CharField(read_only=True)
        rnf = serializers.CharField(read_only=True)
        dt_modified = serializers.DateTimeField()
        cs_active = serializers.CharField()

    class Meta:
        model = models.Sale
        fields = 'id', 'rnf', 'dt_modified', 'cs_active'