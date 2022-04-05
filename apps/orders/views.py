from .models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import status, generics, permissions



class OrderListApiView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_class = [permissions.IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        orders = Order.objects.filter(order_by=user)
        return orders

    def get(self, request):
        payload = request.data
        serializer = OrderSerializer(payload, many=True)
        if serializer.data == []:
            return Response({"detail": "you have no existing order"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)
