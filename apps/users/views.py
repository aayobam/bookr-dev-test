from .models import CustomUser
from apps.common.permissions import (
    IsSuperUserOrReadOnly,
    IsOwnerOrReadOnly,
    CanDeleteUserAccount,
)
from .serializers import UserSerializer, RegisterUserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, permissions, status
from rest_framework.response import Response



class CreateUserApiView(generics.CreateAPIView):
    """
    Users account creattion endpoint
    """
    queryset = CustomUser.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Authenticates user to generate and get access token
    that can be use to grant users access using simplejwt.
    """
    def post(self, request, *args, **kwargs):
        payload = request.data
        serializer = CustomTokenObtainPairSerializer(data=payload)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.validated_data
        return Response(response_data, status=status.HTTP_201_CREATED)


class UserListApiView(generics.ListAPIView):
    """
    Only superuser can view lists of all users registered on
    the system.
    """
    queryset = CustomUser.objects.filter(is_active=True)
    serializer_class = UserSerializer
    permission_classes= [permissions.IsAuthenticated, IsSuperUserOrReadOnly]


class UserDetailApiView(generics.RetrieveAPIView):
    """
    Each user can view his/her detail but can't view other
    users account details.Only the superuser can view all users details.
    """
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_url_kwarg = "user_id"
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_201_CREATED)


class UserUpdateApiView(generics.RetrieveUpdateAPIView):
    """
    Each user can edit/pdate his/her detail but can't edit/update other
    users account details. Only the superuser can edit/update all users details.
    """
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_url_kwarg = "user_id"
    lookup_field = "id"
    
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        response = super().patch(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)
    

class UserDeleteApiView(generics.RetrieveDestroyAPIView):
    """
    Each user can delete his/her detail but can't delete other
    users account details. Only the superuser can delete all users details.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, CanDeleteUserAccount]
    lookup_url_kwarg = "user_id"
    lookup_field = "id"
