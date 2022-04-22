from apps.orders.models import Order
from rest_framework import serializers
from apps.items.models import OrderedItems
from apps.cart.resmodels import CartProductSerializer





class CartSerializer(serializers.Serializer):
    user = serializers.CharField(read_only=True)
    all_products = CartProductSerializer(write_only=True, many=True)
    
    def create(self, validated_data):
        cart_products = validated_data.copy()
        return cart_products

    def update(self, instance, validated_data):
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        return instance
            
            