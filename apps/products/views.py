from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.products.paginator import CustomPageNUmberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, permissions, filters



class CreateProductApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    permission_class = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_201_CREATED)


class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    permission_class = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
    pagination_class = CustomPageNUmberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', "name"]
    search_fields = ['category', "name"]
    ordering_fields = ['category', "name"]

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)


class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_class = [permissions.IsAuthenticated]
    lookup_url_kwarg = "product_id"
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)


class ProductUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_class = [permissions.IsAuthenticated]
    lookup_url_kwarg = "product_id"
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        response = super().patch(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)


class ProductDeleteApiView(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = "product_id"
    lookup_field = "id"

    def delete(self, request, **kwargs):
        product = get_object_or_404(Product, id=kwargs["product_id"])
        if product is not None:
            product.delete()
            return Response({"detail": "Product Deleted"}, status=status.HTTP_200_OK)