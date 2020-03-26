
from rest_framework import serializers
from PhoneSearchApi.models import PhoneNumber

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['countryCode', 'regionCode', 'localExchangeCode', 'number', 'extension']
        
        