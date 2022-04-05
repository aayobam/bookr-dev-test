from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import CategorySerializer
from .models import Category
from django.shortcuts import get_object_or_404



class CreateCategoryApiView(generics.CreateAPIView):
    queryset = Category.objects.all()
    permission_class = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        response =  super().post(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)


class CategoryListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    permission_class = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)


class CategoryDetailApiView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_class = [permissions.IsAuthenticated]
    lookup_url_kwarg = "category_id"
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)


class CategoryUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_class = [permissions.IsAuthenticated]
    lookup_url_kwarg = "category_id"
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        response = super().patch(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)


class CategoryDeleteApiView(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = "category_id"
    lookup_field = "id"

    def delete(self, request, **kwargs):
        category = get_object_or_404(Category, id=kwargs["category_id"])
        if category is not None:
            category.delete()
            return Response({"detail":"category Deleted"}, status=status.HTTP_200_OK)