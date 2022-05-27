from rest_framework import serializers
from pages.models import Product

class Productserilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'