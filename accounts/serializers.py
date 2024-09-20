from rest_framework import serializers
from .models import CustomAccount

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAccount
        fields = '__all__'