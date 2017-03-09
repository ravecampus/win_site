from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    
    # name = serializers.CharField(max_length=255)
    # longitude = serializers.FloatField()
    # latitude = serializers.FloatField()


    class Meta:
        model = Account
        fields = ('email','password')
