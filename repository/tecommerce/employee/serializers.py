from rest_framework import serializers
from employee import models
from employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=70)
    registractions = serializers.CharField(read_only=True)
    dt_modified = serializers.DateTimeField()
    cs_active = serializers.CharField()

    class Meta:
        model = models.Employee
        fields = 'id', 'name', 'registractions', 'dt_modified', 'cs_active'