
from rest_framework import serializers
from PhoneSearchApi.models import PhoneNumber

class PhoneNumberSerializer(serializers.ModelSerializer):
    
    """
    A serializer class used to represent a Phone Number object that will be used by the REST API
    """
    

    class Meta:
        model = PhoneNumber
        fields = ['countryCode', 'regionCode', 'localExchangeCode', 'number', 'extension']
        
        