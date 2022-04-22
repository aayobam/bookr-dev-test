from django.urls import path
from .views import CreateCartApiView



urlpatterns = [
    path("cart_items/", CreateCartApiView.as_view(), name="cart-items"),
]
