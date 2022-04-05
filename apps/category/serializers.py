from .models import Category
from rest_framework import serializers




class CategorySerializer(serializers.ModelSerializer):

    detail_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category

    def update(self, instance, validated_data):
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def detail_url(self, obj):
        return obj.get_absolute_url()