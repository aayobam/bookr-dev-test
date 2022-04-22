from django.urls import path
from .views import OrderedItemListApiView



urlpatterns = [
    path("orders", OrderedItemListApiView.as_view(), name="orderd-items"),
]
