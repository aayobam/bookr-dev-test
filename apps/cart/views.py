import uuid
from pyparsing import identbodychars
from rest_framework import permissions
from .serializers import CartSerializer
from apps.products.models import Product
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from apps.cart.resmodels import CartProductSerializer
from rest_framework import status, generics, serializers




class CreateCartApiView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartSerializer
    queryset = CartProductSerializer

    def create(self, request):
        cart_total_price = 0.00
        payload = request.data.copy()
        payload["user_id"] = self.request.user.id

        if payload["all_products"] == []:
            raise ValidationError("Your cart in empty.")

        for item in payload["all_products"]:
            product = get_object_or_404(Product, id=item["product_id"])

            if not product:
                raise ValidationError("Product not found.")
                
            if item["quantity"] < 1: 
                raise ValidationError("Product quantity cannot be lesser than 1.")

            item["name"] = product.name
            item["price"] = product.price
            item["total_price"] = item["price"] * item["quantity"]

            if item in payload["all_products"]:
                pass
            payload["all_products"].append(item)
            cart_total_price = cart_total_price + float(item["total_price"])
            payload["cart_total_price"] = cart_total_price

            response = self.serializer_class(data=payload)

            print(f"\n Response = {response.initial_data}")
            return Response(response.initial_data, status=status.HTTP_200_OK)