from django.urls import path
from .views import (
    CreateProductApiView,
    ProductListApiView,
    ProductDetailApiView,
    ProductUpdateApiView,
    ProductDeleteApiView,
)


urlpatterns = [
    path('create', CreateProductApiView.as_view(), name="create_product"),
    path('all', ProductListApiView.as_view(), name="product_list"),
    path('detail/<uuid:product_id>', ProductDetailApiView.as_view(), name="product_detail"),
    path('update/<uuid:product_id>', ProductUpdateApiView.as_view(), name="product_update"),
    path('delete/<uuid:product_id>', ProductDeleteApiView.as_view(), name="product_delete"),
]