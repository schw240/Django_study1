from rest_framework.serializers import ModelSerializer, Serializer
from .models import Customer, Country
from rest_framework import serializers


class CountrySerializer(ModelSerializer):
    
    class Meta:
        model = Country
        fields = '__all__'

class CustomerSerializer(ModelSerializer):
    # seq = serializers.ReadOnlyField(source='seq')
    # age = serializers.ReadOnlyField(source='age')
    # sex = serializers.ReadOnlyField(source='sex')
    # name = serializers.ReadOnlyField(source='name')
    nation = serializers.ReadOnlyField(source='nation.country_name')
    class Meta:
        model = Customer
        fields = '__all__'
