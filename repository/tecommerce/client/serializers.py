from rest_framework import serializers
from client import models


class ClientSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=70)
    age = serializers.CharField(max_value=0, min_value=100)
    rg = serializers.CharField()
    cpf = serializers.CharField()
    dt_modified = serializers.DateTimeField()
    cs_active = serializers.CharField()
    class Meta:
        model = models.Client
        fields = 'id','name', 'age', 'rg', 'cpf', 'dt_modified', 'cs_ative'