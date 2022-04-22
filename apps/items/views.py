from apps.items.models import OrderedItems
from rest_framework import status, generics
from rest_framework.response import Response
from apps.items.serializers import OrderedItemSerializer




class OrderedItemListApiView(generics.ListAPIView):
    serializer_class = OrderedItemSerializer
    queryset = OrderedItems.objects.all()
    
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)
