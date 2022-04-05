from django.urls import path
from .views import (
    OrderListApiView,
)


urlpatterns = [
    path('all', OrderListApiView.as_view(), name="order_list")
]