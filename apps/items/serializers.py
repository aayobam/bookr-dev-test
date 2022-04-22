from apps.items.models import OrderedItems
from rest_framework import serializers




class OrderedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderedItems
        fields = '__all__'