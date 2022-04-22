from uuid import UUID
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

        for product in payload["all_products"]:

            print(f"PRODUCTS LIST = {payload['all_products']}")

            product_info = get_object_or_404(Product, id=product["product_id"])

            # if product in payload["all_products"]:
            #     raise ValidationError("You cannot have multiple instance of a product in cart.")

            if not product_info:
                raise ValidationError("Product not found.")
            
            if product["quantity"] < 1:
                raise ValidationError("Product quantity cannot be lesser than 1.")

            product["name"] = product_info.name
            product["price"] = product_info.price

            product_total_price = product["price"] * product["quantity"]
            product["total_price"] = float(product_total_price)
            cart_total_price = cart_total_price + product["total_price"]

            payload["all_products"].append(product)
            
            payload["cart_total_price"] = cart_total_price
            print(f"PAYLOAD = {payload}\n")

            response = self.serializer_class(data=payload)
            print(f"RESPONSE DATA = {response.initial_data}\n")
            return Response(response.initial_data, status=status.HTTP_201_CREATED)
