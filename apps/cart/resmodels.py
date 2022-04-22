from rest_framework import serializers



def validate_quantity(value):
    if value < 1:
        raise serializers.ValidationError("Quantity cannot be less than 1.")
    return value


def validate_price(value):
    if value < 5 :
        raise serializers.ValidationError("Price cannot be less than $5.")
    return value


class CartProductSerializer(serializers.Serializer):
    product_id = serializers.CharField(required=True)
    product_name = serializers.CharField(required=True)
    quantity = serializers.IntegerField(validators=[validate_quantity], required=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, validators=[validate_price], required=True)
    # url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='id', read_only=True)