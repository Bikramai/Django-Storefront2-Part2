from rest_framework import serializers
from decimal import Decimal
from store.models import Product, Collection

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    


    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)