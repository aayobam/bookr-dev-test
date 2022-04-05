from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Product
        fields = fields = '__all__'

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        return product

    def update(self, instance, validated_data):
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def get_detail_url(self, obj):
        return obj.get_absolute_url()