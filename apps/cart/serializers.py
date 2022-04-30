from apps.orders.models import Order
from rest_framework import serializers
from apps.items.models import OrderedItems
from apps.cart.resmodels import CartProductSerializer



class CartSerializer(serializers.Serializer):
    user = serializers.CharField(read_only=True)
    all_products = CartProductSerializer(write_only=True, many=True)
    
    class Meta:
        fields = ["all_products"]
            
            